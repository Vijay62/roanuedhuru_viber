from __future__ import unicode_literals
from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.file_message import FileMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.request import Request, urlopen
from utils.mvnews import News
from utils.properties import Property

import time
import logging
import sched
import threading
import os
import binascii
import tldextract
import shutil
import urllib.parse
import youtube_dl


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
last_token = 0
last_token_track = 0

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='roanuedhuru',
    avatar='http://viber.eyaadh.net/roanu/roanu.jpg',
    auth_token='4a2703710a67d7ee-b3985afaa004d22f-baa00d62b0090499'
))

@app.route('/', methods=['POST'])
def incoming():
    global last_token
    global last_token_track
    logger.debug("received request. post data: {0}".format(request.get_data()))

    viber_request = viber.parse_request(request.get_data().decode('utf8'))
    

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        token = viber_request.message_token

        command = message.text

        if token != last_token:
            last_token = token
            if command == "start" or command == "menu":
                menu_button_list = [['mvnews','News Headlines'],['mvjobs','Job Announcments']]
                default_keyboard = Property.create_menu(menu_button_list)

                viber.send_messages(viber_request.sender.id, [KeyboardMessage(keyboard= default_keyboard)])
                
            elif command == "mvnews":
                menu_button_list = [['sun.mv','sun.mv'],['rajje.mv','Rajje.mv'],['vaguthu.mv','Vaguthu.mv'],['mihaaru.com','Mihaaru.com'],['start','Back']]
                mvnews_keyboard = Property.create_menu(menu_button_list)

                viber.send_messages(viber_request.sender.id, [KeyboardMessage(keyboard= mvnews_keyboard)])
            
            elif command == "sun.mv":
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from sun.mv:")])
                sun_rich_media = Property.create_richmedia(News.sun())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= sun_rich_media, min_api_version=6)])
            
            elif command == "rajje.mv":
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from rajje.mv:")])
                rajje_rich_media = Property.create_richmedia(News.raajje())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= rajje_rich_media, min_api_version=6)])

            elif command == "vaguthu.mv":
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from vaguthu.mv:")])
                vaguthu_rich_media = Property.create_richmedia(News.vaguthu())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= vaguthu_rich_media, min_api_version=6)])
  
            elif command == "mihaaru.com":
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from mihaaru.mv:")])
                mihaaru_rich_media = Property.create_richmedia(News.mihaaru())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= mihaaru_rich_media, min_api_version=6)])

            elif command == "yt_audio":
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Kindly send me the YouTube Link that you would like to convert to Audio", tracking_data="yt_audio")])
        
        if message.tracking_data == "yt_audio" and viber_request.sender.name is not "roanuedhuru":
            if token != last_token_track:
                last_token_track = token
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Ok! Allow me to convert it to Audio and come back to you with the Audio file.", tracking_data=None)])

                sub_directory=binascii.b2a_hex(os.urandom(4)).decode('utf-8')

                ydl_opts = {
                    'writethumbnail': True,
                    'format': 'bestaudio/best',
                    'outtmpl': '/var/www/daisy/ytdl/{0}/%(title)s.%(ext)s'.format(sub_directory),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                    },
                    {'key': 'EmbedThumbnail'},
                    {'key': 'FFmpegMetadata'},],
                }

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.extract_info(message.text, download=True) 

                    if os.path.exists('/var/www/daisy/ytdl/{0}/'.format(sub_directory)):
                        for root, dirs, files in os.walk(os.path.abspath('/var/www/daisy/ytdl/{0}/'.format(sub_directory))):
                            for file in files:
                                total_size = os.path.getsize('/var/www/daisy/ytdl/{0}/{1}'.format(sub_directory,file))
                                if total_size < 50000000:
                                    file_encoded = urllib.parse.quote('{0}'.format(file))
                                    aud_message = FileMessage(media='https://daisy.eyaadh.net/ytdl/{0}/{1}'.format(sub_directory,file_encoded), size=total_size, file_name='{0}'.format(file))

                                    viber.send_messages(viber_request.sender.id, [aud_message])
                                else:
                                    viber.send_messages(viber_request.sender.id, [TextMessage(text="Well Viber is stupid! And it has limitations. (depressed) \nMax file size that can be shared is 50MB and the file we just downloaded is larger than that, well tell you a secret I could send you the same file on telegram - try our partner bot on telegram @megadlbot (eek)")])
                                    shutil.rmtree('/var/www/daisy/ytdl/{0}/'.format(sub_directory))

    
    if isinstance(viber_request, ViberConversationStartedRequest) :
        viber.send_messages(viber_request.user.id, [TextMessage(text="Hello {0}, \nI came to life from telegram. I am the Raonueudhuru_bot from Telegarm and the same family who developed the telegram bot develop me on viber, currently I am at my beta source however we will be there in no time. \n\nSend me Start to begin with.".format(viber_request.user.name))])

        


    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

def create_webhook(viber, webhookURL):
    viber.set_webhook("https://daisy.eyaadh.net:3408")


if __name__ == "__main__":    
    #viber.set_webhook("")
    time.sleep(1)
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(5, 1, create_webhook, (viber, "https://daisy.eyaadh.net:5050",))
    t = threading.Thread(target=scheduler.run)
    t.start()

    context = ('/etc/letsencrypt/live/daisy.eyaadh.net/fullchain.pem', '/etc/letsencrypt/live/daisy.eyaadh.net/privkey.pem')
    app.run(host='0.0.0.0', port=3408, debug=True, ssl_context=context)