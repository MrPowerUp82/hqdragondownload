import requests
from fpdf import FPDF
from lxml import html
import os
import time
import sys

headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

try:
    if sys.argv[1]=='all':
        print('Coloque a url do capitulo 1')
        url=input("Url-> ")
        print('Nome da pasta a ser criada')
        name=input("Nome-> ")
        page=requests.get(url, headers=headers)
        tree=html.fromstring(page.content)
        caps=tree.xpath('//option[@class="listCap"]/@value')
        print("[+]Downloading...[+]")
        for cap in caps:
            page=requests.get(url[:-2]+cap, headers=headers)
            tree=html.fromstring(page.content)
            pags=[x.replace('Pag. ','') for x in tree.xpath('//*[@id="paginas"]/option/text()')]
            os.system("mkdir {}-{}".format(name,cap))
            for pag in pags:
                img_src=tree.xpath('//img[@pag="{}"]/@src'.format(pag))[0]
                img_data = requests.get(img_src,headers=headers).content
                if int(pag) < 10:
                    with open("{}-{}\\image0{}.jpg".format(name,cap,pag), 'wb') as arq:
                        arq.write(img_data)
                else:
                    with open("{}-{}\\image{}.jpg".format(name,cap,pag), 'wb') as arq:
                        arq.write(img_data)
                time.sleep(0.5)

            pdf = FPDF()
            files = [x for x in os.listdir(f'./{name}-{cap}')]
            for image in files:
                pdf.add_page()
                pdf.image(f'{name}-{cap}/{image}',0,0,210,297)
            pdf.output(f'{name}-{cap}.pdf',"F")
            time.sleep(0.5)
            [os.remove(f'{name}-{cap}/{x}') for x in os.listdir(f'{name}-{cap}')]
            os.rmdir(f'{name}-{cap}')

    if sys.argv[1] == 'one':
        print('Coloque a url do capitulo')
        url=input("Url-> ")
        print('Nome da pasta a ser criada')
        name=input("Nome-> ")
        cap=url.split("/")[-1]
        page=requests.get(url, headers=headers)
        tree=html.fromstring(page.content)
        pags=[x.replace('Pag. ','') for x in tree.xpath('//*[@id="paginas"]/option/text()')]
        os.mkdir("{}-{}".format(name,cap))
        print("[+]Downloading...[+]")
        for pag in pags:
            img_src=tree.xpath('//img[@pag="{}"]/@src'.format(pag))[0]
            img_data = requests.get(img_src,headers=headers).content
            if int(pag) < 10:
                with open("{}-{}\\image0{}.jpg".format(name,cap,pag), 'wb') as arq:
                    arq.write(img_data)
            else:
                with open("{}-{}\\image{}.jpg".format(name,cap,pag), 'wb') as arq:
                    arq.write(img_data)
            time.sleep(0.5)

        pdf = FPDF()
        files = [x for x in os.listdir(f'./{name}-{cap}')]
        for image in files:
            pdf.add_page()
            pdf.image(f'{name}-{cap}/{image}',0,0,210,297)
        pdf.output(f'{name}-{cap}.pdf',"F")
        time.sleep(0.5)
        [os.remove(f'{name}-{cap}/{x}') for x in os.listdir(f'{name}-{cap}')]
        os.rmdir(f'{name}-{cap}')
except:
    print("Exemplo:\npython main.py all\npython main.py one")