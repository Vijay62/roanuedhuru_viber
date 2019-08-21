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
from urllib.request import Request, urlopen
from utils.mvnews import News
from utils.properties import Property
from utils.ytdl import ytdl
from utils.criminalcourt import getpdf
from utils.radeef import radeef

import time
import logging
import sched
import threading
import tldextract
import re
import os

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
            
            if re.match(command, "start", re.IGNORECASE) or re.match(command, "menu", re.IGNORECASE):
                menu_button_list = [['mvnews','News Headlines'],['mvjobs','Job Announcements'],['criminalcourt','Criminalcourt.gov.mv Schedule'],['faithoora','Faithoora Publications'],['radeef','Radeef'],['yt_audio','Youtube to Audio']]
                default_keyboard = Property.create_menu(menu_button_list)
                viber.send_messages(viber_request.sender.id, [KeyboardMessage(keyboard= default_keyboard, min_api_version=6)])
                
            elif re.match(command, "mvnews", re.IGNORECASE):
                menu_button_list = [['sun.mv','sun.mv'],['rajje.mv','Rajje.mv'],['vaguthu.mv','Vaguthu.mv'],['mihaaru.com','Mihaaru.com'],['start','Back']]
                mvnews_keyboard = Property.create_menu(menu_button_list)
                viber.send_messages(viber_request.sender.id, [KeyboardMessage(keyboard= mvnews_keyboard, min_api_version=6)])

            elif re.match(command, "mvjobs", re.IGNORECASE):
                menu_button_list = [['jobmaldives','job-maldives.com'],['vazeefa.mv','vazeefa.mv'],['gazette','gazette.mv'],['start','Back']]
                mvjobs_keyboard = Property.create_menu(menu_button_list)
                viber.send_messages(viber_request.sender.id, [KeyboardMessage(keyboard= mvjobs_keyboard, min_api_version=6)])

            elif re.match(command, "radeef", re.IGNORECASE):
                menu_button_list = [['dv_radeef','Search in Dhivehi'],['lt_radeef','Search in Latin'],['en_radeef','Search in English'],['start','Back']]
                mvjobs_keyboard = Property.create_menu(menu_button_list)
                viber.send_messages(viber_request.sender.id, [KeyboardMessage(keyboard= mvjobs_keyboard, min_api_version=6)])

            elif re.match(command, "sun.mv", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from sun.mv:")])
                sun_rich_media = Property.create_richmedia(News.sun())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= sun_rich_media, min_api_version=6)])
            
            elif re.match(command, "rajje.mv", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from rajje.mv:")])
                rajje_rich_media = Property.create_richmedia(News.raajje())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= rajje_rich_media, min_api_version=6)])

            elif re.match(command, "vaguthu.mv", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from vaguthu.mv:")])
                vaguthu_rich_media = Property.create_richmedia(News.vaguthu())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= vaguthu_rich_media, min_api_version=6)])
  
            elif re.match(command, "mihaaru.com", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest headlines (book) from mihaaru.mv:")])
                mihaaru_rich_media = Property.create_richmedia(News.mihaaru())
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= mihaaru_rich_media, min_api_version=6)])

            elif re.match(command, "jobmaldives", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest listings (paperclip) from job-maldives.com:")])
                jobs_rich_media = Property.create_jobmv_rich_media()
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= jobs_rich_media, min_api_version=6)])

            elif re.match(command, "vazeefa.mv", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest listings (paperclip) from vazeefa.mv:")])
                vazeefa_rich_media = Property.create_vazeefa_rich_media()
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= vazeefa_rich_media, min_api_version=6)])

            elif re.match(command, "gazette", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest listings (paperclip) from gazette.mv:")])
                gazette_rich_media = Property.create_gazette_rich_media()
                viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media= gazette_rich_media, min_api_version=6)])

            elif re.match(command, "criminalcourt", re.IGNORECASE):
                court_schedule = getpdf()
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Latest schedule (time) available from criminlcourt.gov.mv - [{0}]:".format(court_schedule[0]))]) 
                pdf_message = FileMessage(media=court_schedule[1], size=court_schedule[2], file_name=court_schedule[3])
                viber.send_messages(viber_request.sender.id, [pdf_message])
            
            elif re.match(command, "faithoora", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Kindly send me the Publication Number of the Faithoora you would like to read. \n\nFor example send me a message with the number: 200\n\nI will reply you with the 200th Publication of Faithoora.\n\nCurrently I have details of 300 Faithoora Publications in my database.", tracking_data="faithoora")])

            elif re.match(command, "en_radeef", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Kindly send me the English Word that you would like to search in Radeef.", tracking_data="en_radeef")])

            elif re.match(command, "lt_radeef", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Kindly send me the Latin Word that you would like to search in Radeef.", tracking_data="lt_radeef")])

            elif re.match(command, "dv_radeef", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Kindly send me the Dhivehi Word that you would like to search in Radeef.", tracking_data="dv_radeef")])

            elif re.match(command, "yt_audio", re.IGNORECASE):
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Kindly send me the YouTube Link that you would like to convert to Audio", tracking_data="yt_audio")])
        
        if message.tracking_data == "yt_audio" and viber_request.sender.name is not "roanuedhuru":
            if token != last_token_track:
                last_token_track = token
                
                domain = tldextract.extract(message.text)
                if domain.domain == 'youtube' or domain.domain == 'youtu':
                    viber.send_messages(viber_request.sender.id, [TextMessage(text="Ok! Allow me to convert it and come back to you with an Audio File. (yo)", tracking_data=None)])
                    ytdl_data = ytdl.ytdl_audio(message.text)

                    if ytdl_data is not False:
                        file_size = ytdl_data[0]
                        media_link = ytdl_data[1]
                        file_name = ytdl_data[2]

                        aud_message = FileMessage(media=media_link, size=file_size, file_name=file_name)
                        viber.send_messages(viber_request.sender.id, [aud_message])
                    else:
                        viber.send_messages(viber_request.sender.id, [TextMessage(text="Well Viber is stupid! And it has limitations. (depressed) \nMax file size that can be shared is 50MB and the file we just downloaded is larger than that, well tell you a secret I could send you the same file on telegram - try our partner bot on telegram @megadlbot (eek)")])                    
                else:
                    viber.send_messages(viber_request.sender.id, [TextMessage(text="Invalid Link (eyeroll), Kindly resend me the command yt_audio and send me a proper YouTube link to convert it to Audio.", tracking_data=None)])
                
        elif message.tracking_data == "faithoora" and viber_request.sender.name is not "roanuedhuru":
            if (message.text).isdigit() and float(message.text) <= 300:
                faithoora_link = "http://viber.eyaadh.net/faithoora/pdf/{0}.pdf".format(message.text)
                faithoora_size = os.path.getsize("/var/www/html/faithoora/pdf/{0}.pdf".format(message.text))
                file_name = "{0}.pdf".format(message.text)
                
                if faithoora_size < 50000000:
                    viber.send_messages(viber_request.sender.id, [TextMessage(text="Ok! Here is the {0}th Publication of Faithoora. (yo):".format(message.text), tracking_data=None)])
                    faithoora_message = FileMessage(media=faithoora_link, size=faithoora_size, file_name=file_name)
                    viber.send_messages(viber_request.sender.id, [faithoora_message])
                else:
                    faithoora_link = "http://viber.eyaadh.net/download.php?file={0}".format(message.text)
                    viber.send_messages(viber_request.sender.id, [TextMessage(text="Well Viber has limitations. (depressed) \nMax file size that can be shared is 50MB and the publication I have is larger than that therefore I cannot send it as a pdf file however I have shared the link to download it.", tracking_data=None)])

                    faithoora_keyboard = {
                        "Type":"keyboard",
                        "DefaultHeight":True,
                        "Buttons": [
                            {
                                "Columns": 6,
                                "Rows": 1,
                                "BgColor": "#FFFAFA",
                                "ActionType": "open-url",
                                "ActionBody":faithoora_link,
                                "Text":"<font color='#000000'><b>Download Faithoora Publication: {0}</b></font>".format(file_name),
                                "TextVAlign": "middle",
                                "TextHAlign": "center",
                                "TextOpacity": 90,
                                "TextSize":"regular",
                                "Frame": {
                                    "BorderWidth" : 2,
                                    "BorderColor" : "#708090",
                                    "CornerRadius" : 4
                                }
                            },
                            {
                                "Columns": 6,
                                "Rows": 1,
                                "BgColor": "#FFFAFA",
                                "ActionType": None,
                                "ActionBody": "menu",
                                "Text":"<font color='#000000'><b>Back</b></font>",
                                "TextVAlign": "middle",
                                "TextHAlign": "center",
                                "TextOpacity": 90,
                                "TextSize":"regular",
                                "Frame": {
                                    "BorderWidth" : 2,
                                    "BorderColor" : "#708090",
                                    "CornerRadius" : 4
                                }
                            }
                        ]
                    }

                    viber.send_messages(viber_request.sender.id, [KeyboardMessage(keyboard= faithoora_keyboard, min_api_version=6)])

            elif float(message.text) > 300:
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Invalid Publication Number (eyeroll), Kindly resend me the command faithoora and send me a proper Publication Number. I only have details of the first 300 Publications", tracking_data=None)])
            else:
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Invalid Publication Number (eyeroll), Kindly resend me the command faithoora and send me a proper Publication Number(only numerical values are accepted).", tracking_data=None)])

        elif message.tracking_data == "en_radeef" and viber_request.sender.name is not "roanuedhuru":
            data_obj = radeef.radeef_english(message.text)
            if not data_obj:
                viber.send_messages(viber_request.sender.id, [TextMessage(text="I am sorry (sad), I could not find that word in Radeef.", tracking_data=None)])
            else:
                data_message = "Dhivehi: {0}\nDefinition: {1}\nLatin: {2}\nEnglish:{3}".format(data_obj[3], data_obj[2], data_obj[1], data_obj[0])
                viber.send_messages(viber_request.sender.id, [TextMessage(text=data_message, tracking_data=None)])

        elif message.tracking_data == "lt_radeef" and viber_request.sender.name is not "roanuedhuru":
            data_obj = radeef.radeef_latin(message.text)
            if not data_obj:
                viber.send_messages(viber_request.sender.id, [TextMessage(text="I am sorry (sad), I could not find that word in Radeef.", tracking_data=None)])
            else:
                data_message = "Dhivehi: {0}\nDefinition: {1}\nLatin: {2}\nEnglish:{3}".format(data_obj[3], data_obj[2], data_obj[1], data_obj[0])
                viber.send_messages(viber_request.sender.id, [TextMessage(text=data_message, tracking_data=None)])
        
        elif message.tracking_data == "dv_radeef" and viber_request.sender.name is not "roanuedhuru":
            data_obj = radeef.radeef_dhivehi(message.text)
            if not data_obj:
                viber.send_messages(viber_request.sender.id, [TextMessage(text="I am sorry (sad), I could not find that word in Radeef.", tracking_data=None)])
            else:
                data_message = "Dhivehi: {0}\nDefinition: {1}\nLatin: {2}\nEnglish:{3}".format(data_obj[3], data_obj[2], data_obj[1], data_obj[0])
                viber.send_messages(viber_request.sender.id, [TextMessage(text=data_message, tracking_data=None)])

    if isinstance(viber_request, ViberConversationStartedRequest) :
        viber.send_messages(viber_request.user.id, [TextMessage(text="Hello {0}, \nI came to life from telegram. I am the Raonueudhuru_bot from Telegarm and the same family who developed the telegram bot develop me on viber, currently I am at my beta source however we will be there in no time. \n\nSend me Start or Menu to begin with.".format(viber_request.user.name))])

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