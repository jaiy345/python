from email.mime import image
from logging import exception
import bs4
import requests
import os

def folder_make(images):
    try:
        f=input("enter your folder name")
        os.mkdir(f)
    except:
        print("the folder name is already exist")


def download_img(images,folder):
    try:
        count=0
        print(f"the image is {len(images)}")
        if len(image)!=0:
            for i,images in enumerate(images):
                try:
                    img_link=image["data-srcset"]
                except:
                    try:
                        img_link=image["data-src"]
                    except:
                        try:
                            img_link= image["data-fallbacksrc"]
                        except:
                            try:
                                img_link=image["src"]
                            except:
                                pass                 

    except exception as e:
        print(e)

    #after getting url you have to download 
    try:
        r=requests.get(img_link).content #in this code we have send http//1.1 why i don't know
        try:
            r=str(r,"utf-8")
        except UnicodeDecodeError:
            #we start downloading img from web
            with open (f"{folder_make}/images{i+1}.jpg","wb+")  as f:
                f.write(r)

            count+=1
    except:
        pass

    if count==len(images):
        print("all image is downloaded")
    else:
        print(f"toatl{count} out of {len(images)}")

def main(url):
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    img=soup.findAll("image")
     
    folder_make(img)

url=input("enter your url :")

main(url)

        
                        
                
    

        

