import requests
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('configuration.txt')
KEY = config.get('vision', 'key')
API_URL = config.get('vision', 'url')



unable_to_detect = 'http://www.franklincountydogs.com/adopt/assets/images/adoptable-size.jpg'
params = { 'visualFeatures' : 'Color,Categories'}

def select_service(service):
    return API_URL + service


def consume_API(url, urlImage):
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = KEY
    headers['Content-Type'] = 'application/json'
    json = { 'url': urlImage }
    data = None
    response = requests.request('post', url, json=json, data=data, headers=headers, params=params)
    return response.json()

def buy_bot(urlImage):
    url = 'http://thebuybot.proxy.apiversity.com/utils/1/rekognition?app_id=app.thebuybot.bot'
    headers = dict()
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    response = requests.request('post', url, data={'url': urlImage}, headers=headers)
    return response.json()

if __name__ == '__main__':
    urlImage = ['http://www.patatero.com/wp-content/uploads/2015/05/551_i0wBX0_Iui.jpeg',
                'http://img.timeinc.net/time/photoessays/2009/ugly_dogs/ugly_dogs_01.jpg',
                'https://www.recreoviral.com/wp-content/uploads/2014/10/perro-feoo.jpg',
                'https://i.ytimg.com/vi/qUw92_I4sSI/maxresdefault.jpg',
                'http://i.imgur.com/NjLCmgY.jpg',
                'http://breadingcats.co.uk/sites/default/files/styles/large/public/field/image/563363_10151860371915471_1356443_n%5B1%5D.jpg?itok=0qvceHL0',
                'http://all-that-is-interesting.com/wordpress/wp-content/uploads/2012/08/ugly-cat-sphynx-2.jpg',
                'https://pmctvline2.files.wordpress.com/2012/01/mice-and-men-snake120120092752.jpg?w=600&h=800',
                'https://s-media-cache-ak0.pinimg.com/564x/69/03/1b/69031b162faded627130f93f661d851c.jpg',
                'http://assets.nydailynews.com/polopoly_fs/1.1455102.1379115974!/img/httpImage/image.jpg_gen/derivatives/gallery_1200/blob-fish.jpg',
                'https://s-media-cache-ak0.pinimg.com/236x/29/90/f6/2990f68ee9cf440702e623b196fb9606.jpg',
                'https://metrouk2.files.wordpress.com/2006/12/snakemanap_450x614.jpg',
                'http://www.doglost.co.uk/images/dog-with-puppies.jpg',
                'http://www.franklincountydogs.com/adopt/assets/images/adoptable-size.jpg'] # PERRO FEO

    url = select_service('describe')
    print consume_API(url, urlImage[2])['description']
    url = select_service('analyze')
    analyze = consume_API(url, urlImage[2])
    if 'categories' in analyze :
        print analyze['categories']
    print buy_bot(urlImage[2])