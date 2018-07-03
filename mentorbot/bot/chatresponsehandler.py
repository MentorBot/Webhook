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
                        "url": "https://mentorbot-prod.herokuapp.com/bot/search",
                        "title":"Help me find a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                        "fallback_url": "https://mentorbot-prod.herokuapp.com/"
                    },
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/bot/register",
                        "title":"Help me become a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                        "fallback_url": "https://mentorbot-prod.herokuapp.com/"
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
        "payload":"FIND_A_MENTOR_PAYLOAD"
        },
        {
        "content_type": "text",
        "title": "Become a Mentor",
        "payload":"BECOME_A_MENTOR_PAYLOAD"
        },
        {
        "content_type": "text",
        "title": "HELP!",
        "payload":"HELP_PAYLOAD"
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
                        "url": "https://mentorbot-prod.herokuapp.com/bot/search",
                        "title":"Find a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                        "fallback_url": "https://mentorbot-prod.herokuapp.com/"
                    },
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/bot/register",
                        "title":"Become a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                        "fallback_url": "https://mentorbot-prod.herokuapp.com/"
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
                        "url": "https://mentorbot-prod.herokuapp.com/bot/search",
                        "title":"Find a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                        "fallback_url": "https://mentorbot-prod.herokuapp.com/"
                    },
                    {
                        "type":"web_url",
                        "url": "https://mentorbot-prod.herokuapp.com/bot/register",
                        "title":"Become a Mentor",
                        "webview_height_ratio": "full",
                        "messenger_extensions": "true",
                        "fallback_url": "https://mentorbot-prod.herokuapp.com/"
                    },
                    {
                        "type": "postback",
                        "title":"Help!!!",
                        "payload": "help"
                    }
                    ]}}}}

def mentor_card():
    pass



def Response(fbid, payload):
    payload = re.sub(r"[^a-zA-Z0-9\s]",' ',payload).lower().split()
    payload = ''.join(payload)
    payload_type = ['info', 'help', 'menu', 'exit']
    print('-----payload1-----', payload)
    if payload in payload_type:
        response = ''
        for x in payload_type:
            if x == 'help':
                response = help(fbid)
                return response
            if x == 'info':
                text = 'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.'
                response = messenger_plain_text_format(fbid, text)
                print('-----response2-----', response)
                return response
            if x == 'menu':
                response = messenger_menu(fbid)
                print('-----response1-----', response)
                return response
            if x == 'exit':
                response = messenger_plain_text_format(fbid,'Bye!!')
                print('-----response1-----', response)
                return response
    else:
        return get_started_button_link(fbid)
