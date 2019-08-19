#libraries
from utils.mvnews import News
class Property:
    @staticmethod
    def create_richmedia(news_channel):
        news = news_channel
        news_buttons = []
        for article in news:
            if len(news_buttons) < 12:
                news_buttons.extend(
                    [
                        {
                            "Columns": 6,
                            "Rows": 6,
                            "ActionType":"open-url",
                            "ActionBody": article[1],
                            "Image": article[2],
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "BgColor": "#780c59",
                            "BgMediaType": "picture",
                            "BgMedia": "http://viber.eyaadh.net/roanu/button_bg4.png",
                            "BgMediaScaleType": "fill",
                            "ActionType":"open-url",
                            "ActionBody": article[1],
                            "Text":"<font color='#ffffff'><b><i>{0}...</i></b></font>".format(article[0][0:80]),
                            "TextVAlign": "middle",
                            "TextHAlign": "center",
                            "TextOpacity": 100,
                            "TextSize":"small"
                        }
                    ]
                )

        new_rich_media = {
            "Type": "rich_media",
            "BgColor": "#FFFFFF",
            "ButtonsGroupColumns":6,
            "ButtonsGroupRows":7,
            "Buttons": news_buttons,                    
        }
        
        return new_rich_media

    @staticmethod
    def create_menu(menu_button_list):
        menu_buttons = []
        for button in menu_button_list:
            menu_buttons.append(
                {
                    "Columns": 6,
                    "Rows": 1,
                    "BgColor": "#ffffff",
                    "BgMediaType": "picture",
                    "BgMedia": "http://viber.eyaadh.net/roanu/button_bg3.png",
                    "BgMediaScaleType": "fill",
                    "BgLoop": True,
                    "ActionType": None,
                    "ActionBody":button[0],
                    "Text":"<font color='#ffffff'><b>{0}</b></font>".format(button[1]),
                    "TextVAlign": "middle",
                    "TextHAlign": "center",
                    "TextOpacity": 90,
                    "TextSize":"regular"
                }
            )
        menu = {
            "Type":"keyboard",
            "DefaultHeight":True,
            "Buttons": menu_buttons
        }

        return menu

    