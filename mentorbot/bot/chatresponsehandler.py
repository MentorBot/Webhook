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

def get_started_menu():
    return {
    "persistent_menu":[
    {
        "locale":"default",
        "composer_input_disabled": "true",
        "call_to_actions":[
            {
            "title":"Mentor_Bot",
            "type":"nested",
            "call_to_actions":[
                {
                "type":"web_url",
                "title":"Latest News",
                "url":"http://www.messenger.com/",
                "webview_height_ratio":"full"
                },
                {
                "type":"web_url",
                "title":"Latest News",
                "url":"http://www.messenger.com/",
                "webview_height_ratio":"full"
                }
    ]}
        ]}]}

def messenger_plain_text_format(response):
    return {
    'message': {
        'text': response
    }
}

def messenger_button_link(URL, button_title):
    return {
        "message_type": "web_url",
        "url": URL,
        "title": button_title,
        }

def messenger_button(button_title, payload ):
    return {
            "message_type": "postback",
            "title": button_title,
            "payload": payload
            }

def mentor_card():
    pass



def Response(payload):
    payload = re.sub(r"[^a-zA-Z0-9\s]",' ',payload).lower().split()
    payload_type = {'find a mentor', 'become a mentor', 'get started', 'info', 'help', 'menu', 'exit'}
    response = ''
    print('-----payload', payload)
    for x in payload_type:
        if x is payload:
            if x is 'find_a_mentor':
                response = messenger_plain_text_format(find_a_mentor() )
            elif payload is 'become_a_mentor':
                response = messenger_plain_text_format(find_a_mentor())
            print('-----r', response)
        else:
            response = get_started_menu()
    return response
