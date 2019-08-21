#libraries
import json
import urllib
import re
class radeef:
    @staticmethod
    def radeef_english(search_term):
        url = urllib.request.urlopen("http://viber.eyaadh.net/radeef.json")
        db = json.load(url)
        return_data = []
        for dict in db:
            try:
                if re.match(search_term, dict['English'], re.IGNORECASE):
                    return_data.extend((dict['English'], dict['Latin'], dict['Definition'], dict['Dhivehi']))
            except:
                pass
        return return_data

    @staticmethod
    def radeef_latin(search_term):
        url = urllib.request.urlopen("http://viber.eyaadh.net/radeef.json")
        db = json.load(url)
        return_data = []
        for dict in db:
            try:
                if re.match(search_term, dict['Latin'], re.IGNORECASE):
                    return_data.extend((dict['English'], dict['Latin'], dict['Definition'], dict['Dhivehi']))
            except:
                pass
        return return_data

    @staticmethod
    def radeef_dhivehi(search_term):
        url = urllib.request.urlopen("http://viber.eyaadh.net/radeef.json")
        db = json.load(url)
        return_data = []
        for dict in db:
            try:
                if re.match(search_term, dict['Dhivehi'], re.IGNORECASE):
                    return_data.extend((dict['English'], dict['Latin'], dict['Definition'], dict['Dhivehi']))
            except:
                pass
        return return_data