
import requests



def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/products')
    print(r.status_code)
    #print(r.text)
    categories = r.json()
    for i in categories:
        print(i['title'])
