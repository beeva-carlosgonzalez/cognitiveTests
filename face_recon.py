import requests
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('configuration.txt')
KEY = config.get('face', 'key')
API_URL = config.get('face', 'url')


def select_service(service):
    return API_URL + service


def consume_API(url, file):
    data = open(file, 'rb').read()
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = KEY
    headers['Content-Type'] = 'application/octet-stream'
    response = requests.request('post', url, data=data, headers=headers)
    return response.json()


if __name__ == '__main__':
    url = select_service('detect')
    print consume_API(url, 'sergio_fajardo_alcalde_medellin.jpg')
