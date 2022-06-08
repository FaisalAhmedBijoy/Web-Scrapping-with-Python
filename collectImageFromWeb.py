from itertools import count
from bs4 import BeautifulSoup
import requests
import os
import glob
import cv2
import matplotlib.pyplot as plt
import PIL

def download_image(url,given_image_numbers):
    print('Website link: ', url)

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    # print(soup)
    images = soup.find_all('img')
    # print(images)
    print('Total images found: ', len(images))
    if(given_image_numbers>len(images)):
        print("The expected number of download is exceeded")
    else:
        print("website contaiun more image than expected given inpu image")
    if len(images) != 0:
        for i, image in enumerate(images):  
            image_link = image['src']
            try:
                request_img = requests.get(image_link).content
            except:
                print('request image error ')
                
            with open('images/images'+str(i+1)+'.jpg', 'wb+') as f:
                f.write(request_img)
            
    else:
        print("No images found")


def preproessing_image(path):
    #print(os.listdir(path))
    WIDTH=224
    HEIGHT=224

    try:
        os.mkdir('resized_image')
    except:
        print("Folder already exist")

    for i,filename in enumerate(glob.glob(path+'/*')):
        image=PIL.Image.open(filename)
        image=image.resize((WIDTH,HEIGHT),PIL.Image.ANTIALIAS)
        image.save('resized_image/image'+str(i)+'.png')

if __name__ == '__main__':
    url = 'https://www.kuet.ac.bd/'
    print("Enter the number of expected download images")
    image_number_download=int(input())
    download_image(url,image_number_download)
    image_file='images'
    preproessing_image(image_file)
