#libraries
from utils.mvnews import News
from utils.mvjobs import Jobs
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
                            "BgColor": "#708090",
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
            "BgColor": "#DCDCDC",
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
                    "BgColor": "#778899",
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

    @staticmethod
    def create_jobmv_rich_media():
        jobs_list = Jobs.jobmv()
        jobs_buttons = []
        for jobs in jobs_list:
            if len(jobs_buttons) < 12:
                jobs_buttons.extend(
                    [{
                        "Columns": 6,
                        "Rows": 6,
                        "BgColor": "#FFFAFA",
                        "ActionType": "open-url",
                        "ActionBody":jobs[1],
                        "Image": "http://viber.eyaadh.net/roanu/job-opportunity.png",
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 90,
                        "TextSize":"small" 
                    },    
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "BgColor": "#FFFAFA",
                        "ActionType": "open-url",
                        "ActionBody":jobs[1],
                        "Text":"<font color='#000000'><b>{0}</b></font>".format(jobs[0]),
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 90,
                        "TextSize":"small" 
                    }]
                )
        jobs_rich_media = {
            "Type": "rich_media",
            "BgColor": "#DCDCDC",
            "Buttons": jobs_buttons                    
        }

        return jobs_rich_media

    @staticmethod
    def create_vazeefa_rich_media():
        vazeefa_list = Jobs.vazeefa()
        vazeefa_buttons = []
        for vazeefa in vazeefa_list:
            if len(vazeefa_buttons) < 36:
                vazeefa_buttons.extend(
                    [{
                        "Columns": 6,
                        "Rows": 2,
                        "BgColor": "#FFFAFA",
                        "ActionType": "open-url",
                        "ActionBody":vazeefa[1],
                        "Image": "http://viber.eyaadh.net/roanu/job-opportunity.png",
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 90,
                        "TextSize":"small" 
                    },
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "BgColor": "#FFFAFA",
                        "ActionType":"open-url",
                        "ActionBody": vazeefa[1],
                        "Text":"<font color='#000000'><b>Title: {0}</b></font>".format(vazeefa[0][0:80]),
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 100,
                        "TextSize":"regular"
                    },
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "BgColor": "#FFFAFA",
                        "ActionType":"open-url",
                        "ActionBody": vazeefa[1],
                        "Text":"<font color='#000000'><i>Employer: {0}</i></font>".format(vazeefa[2][0:80]),
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 100,
                        "TextSize":"small"
                    },
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "BgColor": "#FFFAFA",
                        "ActionType":"open-url",
                        "ActionBody": vazeefa[1],
                        "Text":"<font color='#000000'><i>Location: {0}</i></font>".format(vazeefa[3][0:80]),
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 100,
                        "TextSize":"small"
                    },
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "BgColor": "#FFFAFA",
                        "ActionType":"open-url",
                        "ActionBody": vazeefa[1],
                        "Text":"<font color='#000000'><i>Apply Before: {0}</i></font>".format(vazeefa[4][0:80]),
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 100,
                        "TextSize":"small"
                    },
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "BgColor": "#FFFAFA",
                        "ActionType":"open-url",
                        "ActionBody": vazeefa[1],
                        "Text":"<font color='#000000'><i>Salary: {0}</i></font>".format(vazeefa[5][0:80]),
                        "TextVAlign": "middle",
                        "TextHAlign": "center",
                        "TextOpacity": 100,
                        "TextSize":"small"
                    }]
                )
        vazeefa_rich_media = {
            "Type": "rich_media",
            "BgColor": "#FFFAFA",
            "Buttons": vazeefa_buttons,                    
        }

        return vazeefa_rich_media

    @staticmethod
    def create_gazette_rich_media():
        gazette_list = Jobs.gazette()
        gazette_buttons = []
        for gazette in gazette_list:
            if len(gazette_buttons) < 26:
                gazette_buttons.extend(
                    [
                        {
                            "Columns": 6,
                            "Rows": 3,
                            "BgColor": "#FFFAFA",
                            "ActionType": "open-url",
                            "ActionBody":gazette[1],
                            "Image": "https://storage.googleapis.com/presidency.gov.mv/Photos/gazette.png",
                            "TextVAlign": "middle",
                            "TextHAlign": "center",
                            "TextOpacity": 90,
                            "TextSize":"small" 
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "BgColor": "#FFFAFA",
                            "ActionType":"open-url",
                            "ActionBody": gazette[1],
                            "Text":"<font color='#000000'><b>{0}</b></font>".format(gazette[0][0:80]),
                            "TextVAlign": "middle",
                            "TextHAlign": "center",
                            "TextOpacity": 100,
                            "TextSize":"regular"
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "BgColor": "#FFFAFA",
                            "ActionType":"open-url",
                            "ActionBody": gazette[1],
                            "Text":"<font color='#000000'><i>{0}</i></font>".format(gazette[2][0:80]),
                            "TextVAlign": "middle",
                            "TextHAlign": "center",
                            "TextOpacity": 100,
                            "TextSize":"small"
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "BgColor": "#FFFAFA",
                            "ActionType":"open-url",
                            "ActionBody": gazette[1],
                            "Text":"<font color='#000000'><i>{0}</i></font>".format(gazette[3][0:80]),
                            "TextVAlign": "middle",
                            "TextHAlign": "center",
                            "TextOpacity": 100,
                            "TextSize":"small"
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "BgColor": "#FFFAFA",
                            "ActionType":"open-url",
                            "ActionBody": gazette[1],
                            "Text":"<font color='#000000'><i>{0}</i></font>".format(gazette[4][0:80]),
                            "TextVAlign": "middle",
                            "TextHAlign": "center",
                            "TextOpacity": 100,
                            "TextSize":"small"
                        }
                    ]
                )
        gazette_rich_media = {
            "Type": "rich_media",
            "BgColor": "#FFFAFA",
            "Buttons": gazette_buttons,                    
        }

        return gazette_rich_media

    
    