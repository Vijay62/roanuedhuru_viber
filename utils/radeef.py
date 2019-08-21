#libraries
import json
import urllib
class radeef:
    @staticmethod
    def radeef_english(search_term):
        url = urllib.request.urlopen("http://viber.eyaadh.net/radeef.json")
        db = json.load(url)
        return_data = []
        for dict in db:
            try:
                if dict['English'] == search_term:
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
                if dict['Latin'] == search_term:
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
                if dict['Dhivehi'] == search_term:
                    return_data.extend((dict['English'], dict['Latin'], dict['Definition'], dict['Dhivehi']))
            except:
                pass
        return return_data