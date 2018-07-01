import re

'''this class sends back texts containing different things'''
def what_do_you_want_to_do():
    return("find a mentor")

def find_a_mentor():
    return("In what field would you like to be mentored in?")

def become_a_mentor():
    return("lets get you registered then!!")

def response():
    return 'Hello World'

def info():
    return 'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.'

def help():
    return 'What would you like to do?'

def get_started_menu(fbid):
    return {
        "recipient": {
            "id": fbid
             },
        "message": {
        "type": "persistent_menu",
        "locale":"default",
        "call_to_actions":[
                {
                "title":"Mentor_Bot",
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
                    }
                ]}]}}


def messenger_plain_text_format(fbid, response):
    return {
        "recipient": {
            "id": fbid
             },
        'message': {
            'text': response
    }
}

def messenger_button_link(fbid, URL, button_title):
    return {
        "recipient": {
            "id": fbid
             },
        "type": "web_url",
        "url": URL,
        "title": button_title,
        }

def messenger_button(fbid, button_title, payload ):
    return {
            "recipient": {
            "id": fbid
             },
             "message": {
            "message_type": "postback",
            "title": button_title,
            "payload": payload
            }}

def mentor_card():
    pass



def Response(fbid, payload):
    payload = re.sub(r"[^a-zA-Z0-9\s]",' ',payload).lower().split()
    payload = ''.join(payload)
    payload_type = {'findamentor', 'becomeamentor', 'getstarted', 'info', 'help', 'menu', 'exit'}
    response = ''
    print('-----payload', payload)
    for x in payload_type:
        if x is payload:
            print('-----x', x)
            if x is 'find_a_mentor':
                response = messenger_plain_text_format(fbid, find_a_mentor() )
            elif payload is 'become_a_mentor':
                response = messenger_plain_text_format(fbid, find_a_mentor())
            print('-----r', response)
        else:
            response = get_started_menu(fbid)
    return response
