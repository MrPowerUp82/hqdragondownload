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
print('Coloque a url do capitulo desejado')
url=input("Url-> ")
print('Nome da pasta a ser criada')
name=input("Nome-> ")
cap=input("Cap-> ")
os.system("mkdir {}-{}".format(name,cap))
page=requests.get(url, headers=headers)
tree=html.fromstring(page.content)
ns=tree.xpath('//*[@id="paginas"]/option[last()]/text()')
n=int(ns[0].replace('Pag. ',''))
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

print("[+]Download finish[+]")
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

