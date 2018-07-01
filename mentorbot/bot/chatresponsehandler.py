from django.views import View

class ResponseText(View):
    '''this class sends back texts containing different things'''
    def what_do_you_want_to_do(self):
        return("find a mentor")

    def find_a_mentor(self):
        return("In what field would you like to be mentored in?")

    def become_a_mentor(self):
        return("lets get you registered then!!")

    def response(self):
        return 'Hello World'

    def info(self):
        return 'Mentor_Bot is a FaceBook Developer Challenge Award Winning Bot \n that will help you find a mentor in a field that you wish to level up on.'

    def help(self):
        return 'What would you like to do?'

class ResponseFormat(View):
    # def get_started_menu(self, fbid):
    #     {
    #     "persistent_menu":[
    #     {
    #         "locale":"default",
    #         "composer_input_disabled": "true",
    #         "call_to_actions":[
    #             {
    #             "title":"Mentor_Bot",
    #             "type":"nested",
    #             "call_to_actions":[
    #                 {
    #                 "type":"web_url",
    #                 "title":"Latest News",
    #                 "url":"http://www.messenger.com/",
    #                 "webview_height_ratio":"full"
    #                 },
    #                 {
    #                 "type":"web_url",
    #                 "title":"Latest News",
    #                 "url":"http://www.messenger.com/",
    #                 "webview_height_ratio":"full"
    #                 }
    #     ]}
    #         ]}]}

    def messenger_plain_text_format(self, fbid, response):
        return {
        'messaging_type': 'RESPONSE',

        'recipient': {
            'id': fbid
            },
        'message': {
            'text': response
        }
    }

    def messenger_button_link(self, fbid, URL, button_title):
        return {
            "message_type": "web_url",
            'recipient': {
                'id': fbid
                },
            "url": URL,
            "title": button_title,
            }

    def messenger_button(self, fbid, button_title, payload ):
        return {
                "message_type": "postback",
                "title": button_title,
                "payload": payload
                }

    def mentor_card(self):
        pass



def Response(fbid, payload):
    RF = ResponseFormat()
    RT = ResponseText()
    payload_type = {'find a mentor', 'become a mentor', 'get started', 'info', 'help', 'menu', 'exit'}
    response = ''
    print('-----x', payload)
    print('------id', fbid)
    if payload in payload_type:
        if payload is 'find_a_mentor':
            response = RF.messenger_plain_text_format(fbid, RT.find_a_mentor() )
        elif payload is 'become_a_mentor':
            response = RF.messenger_plain_text_format(fbid, RT.find_a_mentor())
        print('-----r', response)
        return response
