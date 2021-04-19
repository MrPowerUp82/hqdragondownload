import requests
from fpdf import FPDF
from lxml import html
import os
from time import sleep
from os import walk
import time
headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
print('Coloque a url do capitulo 1')
url=input("Url-> ")
print('Nome da pasta a ser criada')
name=input("Nome-> ")
page=requests.get(url, headers=headers)
tree=html.fromstring(page.content)
caps=tree.xpath('//option[@class="listCap"]/@value')
j=1
url=url.replace('01','')
while j < (len(caps)):
    url_hq=url + caps[j-1]
    page=requests.get(url_hq, headers=headers)
    tree=html.fromstring(page.content)
    ns=tree.xpath('//*[@id="paginas"]/option[last()]/text()')
    n=int(ns[0].replace('Pag. ',''))
    cap=j
    os.system("mkdir {}-{}".format(name,cap))
    i=1

    print("[+]Downloading...[+]")
    while i <= n:
        if i < 10:
            hq=tree.xpath('//img[@pag="{}"]/@src'.format(i))
            src=str(*hq)
            img= requests.get(src, headers=headers)
            img_data=img.content
            arq=open("{}-{}\\image0{}.jpg".format(name,cap,i), 'wb')
            arq.write(img_data)
            arq.close()
            time.sleep(0.5)
        else:
            hq=tree.xpath('//img[@pag="{}"]/@src'.format(i))
            src=str(*hq)
            img= requests.get(src, headers=headers)
            img_data=img.content
            arq=open("{}-{}\\image{}.jpg".format(name,cap,i), 'wb')
            arq.write(img_data)
            arq.close()
            time.sleep(0.5)
        i=i+1

    pdf = FPDF()
    files = []
    pasta="./{}-{}/".format(name,cap)
    path = pasta
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break

    for image in files:
        pdf.add_page()
        pdf.image('{}-{}/{}'.format(name,cap,image), 0, 0, 210, 297)                           # 210 and 297 are the dimensions of an A4 size sheet.

    pdf.output("{}-{}.pdf".format(name,cap), "F")  
    j+=1
    time.sleep(0.5)
