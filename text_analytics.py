import requests
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('configuration.txt')
KEY = config.get('text', 'key')
API_URL = config.get('text', 'url')

def select_service(service, text_to_detect, language=None):
    if service == 'languages':
        message = { 'documents': [{'id': text_to_detect,
                           'text': text_to_detect}]
                  }
    else:
        message = { 'documents': [{'id': text_to_detect,
                                   'text': text_to_detect,
                                   'language': language}]
                  }
    return API_URL + service, message


def consume_API(url, json_object):
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = KEY
    headers['Content-Type'] = 'application/json'
    response = requests.request('post', url, json=json_object, headers=headers)
    return response.json()


if __name__ == '__main__':
    url, message = select_service('languages', 'Iba por el campo muy contento')
    print consume_API(url, message)
    url, message = select_service('sentiment', 'Iba por el campo muy contento', 'es')
    print consume_API(url, message)
    url, message = select_service('sentiment', 'Me dijo que era muy inteligente. De manera totalmente ironica', 'es')
    print consume_API(url, message)
    url, message = select_service('keyPhrases', 'Me dijo que era muy inteligente. De manera totalmente ironica. El rey caminaba por'
                                                ' la hacienda', 'es')
    print consume_API(url, message)