RESPONSE = {
    'get-started': {
        'search-type': 'get started',
        'keywords': ['hi', 'hello'],
    },
}

def get_response():
    return RESPONSE

def response_exists(response_type):
    for res in RESPONSE:
        if res == response_type:
            return True
    return False
