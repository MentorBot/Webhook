import re
from decouple import config


def what_do_you_want_to_do():
    return("find a mentor")

def find_a_mentor():
    return("In what field would you like to be mentored in?")

def become_a_mentor():
    return("lets get you registered then!!")

def info():
    return 'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.'

def help():
    return ('What would you like to do?', '')

def get_started_menu():
    return {
  "persistent_menu":[
    {
      "locale":"default",
      "composer_input_disabled": "true",
      "call_to_actions":[
        {
          "title":"Menu",
          "type":"nested",
          "call_to_actions":[
            {
              "title":"Find a Mentor",
              "type":"postback",
              "payload":"FIND_A_MENTOR_PAYLOAD"
            },
            {
              "title":"Become a Mentor",
              "type":"postback",
              "payload":"BECOME_A_MENTOR_PAYLOAD"
            },
            {
              "title":"Info",
              "type":"postback",
              "payload":"INFO_PAYLOAD"
            }
          ]
        },
      ]
    },
  ]
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
            'text': response
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
    payload_type = {'findamentor', 'becomeamentor', 'getstarted', 'info', 'help', 'menu', 'exit'}
    response = ''
    print('-----payload', payload)
    for x in payload_type:
        if x is payload:
            print('-----x', x)
            if x is 'findamentor':
                response = messenger_plain_text_format(find_a_mentor())
            elif payload is 'becomeamentor':
                response = messenger_plain_text_format(become_a_mentor())
            print('-----r', response)
        else:
            response = get_started_menu()
    return response
