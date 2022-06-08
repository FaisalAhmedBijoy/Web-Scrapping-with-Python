from itertools import count
from bs4 import BeautifulSoup
import requests


def download_image(url):
    print('Website link: ', url)

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    # print(soup)
    images = soup.find_all('img')
    # print(images)
    print('Total images found: ', len(images))
    if len(images) != 0:
        for i, image in enumerate(images):  
            image_link = image['src']
            try:
                request_img = requests.get(image_link).content
            except:
                print('request image error ')
                
            with open('kuet/images'+str(i+1)+'.jpg', 'wb+') as f:
                f.write(request_img)
            
    else:
        print("No images found")


if __name__ == '__main__':
    url = 'https://www.kuet.ac.bd/'
    download_image(url)
