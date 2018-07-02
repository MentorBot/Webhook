import re
from decouple import config


# def what_do_you_want_to_do():
#     return "find a mentor"

# def find_a_mentor():
#     return "In what field would you like to be mentored in?"

# def become_a_mentor():
#     return "lets get you registered then!!"

# def info():
#     return 'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.'

# def help():
#     return ('What would you like to do?', 'Find a mentor', 'Become a mentor', 'What is this bot about?')

def get_started_menu():
    return {
  "text": "Greetings! I am MentorBot!!And i am here to help you find a mentor a field you would like to level up as well as become a mentor and give back to the community."
}

def become_a_mentor_button():
    WEBVIEW_URL = config('WEBVIEW_URL')
    return {
        "type":"web_url",
        "url": WEBVIEW_URL,
        "title":"Sign Up!!",
        "webview_height_ratio": "full",
        "messenger_extensions": "false",
        "fallback_url": "http://mentorbot-prod.herokuapp.com/"
}

def become_a_mentor_webview():
    return{
        "<html>"
       "<head>"
            "<title>My Awesome Webview</title>"
        "</head>"
        "</html>"
    }


def messenger_plain_text_format(response):
    return {
    {
           "text": response
    }
}

def messenger_quick_replies(response, value):
    return {
        "quickReplies": [{
        "content_type": "text",
        "title": "Find a Mentor",
        "payload":"<FIND_A_MENTOR_PAYLOAD>"
        },
        {
        "content_type": "text",
        "title": "Become a Mentor",
        "payload":"<BECOME_A_MENTOR_PAYLOAD>"
        },
        {
        "content_type": "text",
        "title": "HELP!!",
        "payload":"<HELP_PAYLOAD>"
        }
        ]}


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

def messenger_button_link(URL, button_title):
    return {
        "type": "web_url",
        "url": URL,
        "title": button_title,
        }

def messenger_button(button_title, payload ):
    return {
            "type": "postback",
            "title": button_title,
            "payload": payload
            }

def mentor_card():
    pass



def Response(payload):
    payload = re.sub(r"[^a-zA-Z0-9\s]",' ',payload).lower().split()
    payload = ''.join(payload)
    payload_type = ['findamentor', 'becomeamentor', 'getstarted', 'info', 'help', 'menu', 'exit']
    response = ''

    for x in payload_type:
        if payload not in payload_type:
            return get_started_menu()
        elif x is payload:
            if x is 'findamentor':
                response = messenger_plain_text_format('In what field would you like to be mentored in?')
            elif payload is 'becomeamentor':
                response = messenger_plain_text_format('lets get you registered then!!')
            elif payload is 'help':
                response = messenger_button_link('try !', 'try 2')
            elif payload is 'info':
                response = messenger_plain_text_format('Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.')
            elif payload is 'menu':
                response = messenger_plain_text_format('Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.')
            elif payload is 'exit':
                response = messenger_plain_text_format('Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.')
            elif payload is 'getstarted':
                response = messenger_plain_text_format('Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.')
            print('-----r', response)

    return response
