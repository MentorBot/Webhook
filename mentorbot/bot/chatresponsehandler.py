import re
from decouple import config

def help(fbid):
       return {
        "recipient":{
            "id":fbid
            },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"How can i help you?",
                    "buttons":[
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/find_mentor",
                        "title":"Help me find a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                    },
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/become_mentor",
                        "title":"Help me become a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                    }
                    ]}}}}

def messenger_plain_text_format(fbid, response):
    return {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": fbid
        },
        "message": {
            "text": response
        }
    }

def messenger_quick_replies(fbid):
    return {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": fbid
        },
        "message": {
            "quick_replies": [{
                "content_type": "text",
                "title": "Find a Mentor",
                "payload": "FIND_A_MENTOR_PAYLOAD"
            },
                {
                "content_type": "text",
                "title": "Become a Mentor",
                "payload": "BECOME_A_MENTOR_PAYLOAD"
            },
                {
                "content_type": "text",
                "title": "HELP!",
                "payload": "HELP_PAYLOAD"
            }
            ]}}

def get_started_button_link(fbid):
    return {
        "recipient":{
            "id":fbid
            },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Hi there! I am Mentor_Bot!! \n My mission is to help you find a mentor in the field of your interest, as fast as possible!! sounds good?  \n Let's get you started. What would you like to do today?",
                    "buttons":[
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/find_mentor",
                        "title":"Find a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                    },
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/become_mentor",
                        "title":"Become a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                    },
                    {
                        "type": "postback",
                        "title":"Help!!!",
                        "payload": "help"
                    }
                    ]}}}}

def messenger_menu(fbid, ):
        return {
        "recipient":{
            "id":fbid
            },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Menu",
                    "buttons":[
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/find_mentor",
                        "title":"Find a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                    },
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/become_mentor",
                        "title":"Become a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                    },
                    {
                        "type": "postback",
                        "title":"Help!!!",
                        "payload": "help"
                    }
                    ]}}}}

def Response(fbid, payload):
    payload = re.sub(r"[^a-zA-Z0-9\s]", ' ', payload).lower().split()
    payload = ''.join(payload)
    payload_type = ['info', 'help', 'menu', 'exit']
    if payload not in payload_type:
        return get_started_button_link(fbid)
    else:
        for x in payload_type:
            if x == 'help':
                response = help(fbid)
            elif x == 'info':
                text = 'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.'
                response = messenger_plain_text_format(fbid, text)
            elif x == 'menu':
                response = messenger_menu(fbid)
            return response
