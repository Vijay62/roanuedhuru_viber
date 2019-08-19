#libraries
from __future__ import unicode_literals
import youtube_dl
import binascii
import shutil
import os
import urllib.parse

class ytdl:
    @staticmethod
    def ytdl_audio(dl_link):
        yt_dl_data = []
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
            ydl.extract_info(dl_link, download=True) 

            if os.path.exists('/var/www/daisy/ytdl/{0}/'.format(sub_directory)):
                for root, dirs, files in os.walk(os.path.abspath('/var/www/daisy/ytdl/{0}/'.format(sub_directory))):
                    for file in files:
                        total_size = os.path.getsize('/var/www/daisy/ytdl/{0}/{1}'.format(sub_directory,file))

                        if total_size < 50000000:
                            file_encoded = urllib.parse.quote('{0}'.format(file))
                            media_link = 'https://daisy.eyaadh.net/ytdl/{0}/{1}'.format(sub_directory,file_encoded)
                            file_name = '{0}'.format(file)
                            yt_dl_data.extend((total_size, media_link, file_name))

                            return yt_dl_data
                        else:
                            shutil.rmtree('/var/www/daisy/ytdl/{0}/'.format(sub_directory))
                            return False

