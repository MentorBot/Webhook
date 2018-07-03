import re
from decouple import config

def get_started_text(fbid):
    return {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": fbid
        },
        "message":{
            "text": "Hi there! I am Mentor_Bot!! \n My mission is to help you find a mentor in the field of your interest, as fast as possible!! sounds good?  \n Let's get you started. What would you like to do today? ",
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
            }]}
    }

def become_a_mentor_button(fbid):
    WEBVIEW_URL = config('WEBVIEW_URL')
    return {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": fbid
        },
        "message":{
            "attachment":{
                "type":"template",
                        "payload":{
                        "template_type":"button",
                        "text":"Register to become a mentor",
                        "button":[{
                            "type":"web_url",
                            "url": WEBVIEW_URL,
                            "title":"Sign Up!!",
                            "webview_height_ratio": "full",
                            "messenger_extensions": "false",
                            "fallback_url": "http://mentorbot-prod.herokuapp.com/"
                            }]}
}}}

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


def messenger_cards():
    return {
        "type": 'card',
        "content": {
            "title": 'CARD_TITLE',
            "subtitle": 'CARD_SUBTITLE',
            "imageUrl": 'IMAGE_URL',
            "buttons": [
            {
                "title": 'BUTTON_TITLE',
                "type": 'BUTTON_TYPE',
                "value": 'BUTTON_VALUE'
      }
    ]
  }
}

def get_started_button_link(fbid):
    WEBVIEW_URL = config('WEBVIEW_URL')
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
                        "url":"https://www.messenger.com",
                        "title":"Find a Mentor"
                    },
                    {
                        "type":"web_url",
                        "url":"https://www.messenger.com",
                        "title":"Become a Mentor"
                    },
                    {
                        "type":"web_url",
                        "url": WEBVIEW_URL,
                        "title":"Sign Up!!",
                        "webview_height_ratio": "compact",
                        "messenger_extensions": "true",
                        "fallback_url": "https://mentorbot-prod.herokuapp.com/"
                    }
                    ]}}}}

def messenger_button(fbid, ):
    return {
        "messaging_type": "RESPONSE",
        "recipient":{
                 "id": fbid
            },
        "message":{
            "attachment":{
                "type":"template",
                        "payload":{
                        "template_type":"button",
                        "text":"What would you like to do?",
                        "buttons":[
                                {
                            "type":"button",
                            "title":"Find a Mentor"
                                },
                                {
                            "type":"web_url",
                            "url":"https://www.messenger.com",
                            "title":"Visit Messenger"
                                },
                                {
                            "type":"web_url",
                            "url":"https://www.messenger.com",
                            "title":"Visit Messenger"
                                }]
                                }}}}

def mentor_card():
    pass



def Response(fbid, payload):
    payload = re.sub(r"[^a-zA-Z0-9\s]",' ',payload).lower().split()
    payload = ''.join(payload)
    payload_type = ['findamentor', 'becomeamentor', 'getstarted','info', 'help', 'menu', 'exit']
    for x in payload_type:
        print('-----payload1-----', payload)
        if payload in payload_type:
            response = ''
            if x is 'findamentor':
                text = "In what field would you like to be mentored in?"
                response = messenger_plain_text_format(fbid, text)
                print('-----response1-----', response)
            # if x is 'becomeamentor':
            #     text = "lets get you registered then!!"
            #     response = messenger_plain_text_format(fbid, text)
            #     print('-----response1-----', response)
            #     # return response
            # elif x is 'help':
            #     response = messenger_button(fbid)
            #     print('-----response1-----', response)
            #     # return response
            # elif x is 'info':
            #     response = messenger_plain_text_format(fbid,'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.')
            #     print('-----response1-----', response)
            #     # return response
            # elif x is 'menu':
            #     response = messenger_button(fbid)
            #     print('-----response1-----', response)
            #     # return response
            # elif x is 'exit':
            #     response = messenger_plain_text_format(fbid,'Bye!!')
            #     print('-----response1-----', response)
            #     # return response
            # elif x is 'getstarted':
            #     response = messenger_plain_text_format(fbid,'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.')
            # print('-----r', response)
            return response
        else:
            return get_started_button_link(fbid)
