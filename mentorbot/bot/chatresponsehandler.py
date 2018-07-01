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
          "title":"My Account",
          "type":"nested",
          "call_to_actions":[
            {
              "title":"Pay Bill",
              "type":"postback",
              "payload":"PAYBILL_PAYLOAD"
            },
            {
              "title":"History",
              "type":"postback",
              "payload":"HISTORY_PAYLOAD"
            },
            {
              "title":"Contact Info",
              "type":"postback",
              "payload":"CONTACT_INFO_PAYLOAD"
            }
          ]
        },
        {
          "type":"web_url",
          "title":"Latest News",
          "url":"http://www.messenger.com/",
          "webview_height_ratio":"full"
        }
      ]
    },
    {
      "locale":"zh_CN",
      "composer_input_disabled":"false",
      "call_to_actions":[
        {
          "title":"Pay Bill",
          "type":"postback",
          "payload":"PAYBILL_PAYLOAD"
        }
      ]
    }
  ]
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
            if x is 'find_a_mentor':
                response = messenger_plain_text_format(find_a_mentor() )
            elif payload is 'become_a_mentor':
                response = messenger_plain_text_format(find_a_mentor())
            print('-----r', response)
        else:
            response = get_started_menu()
    return response
