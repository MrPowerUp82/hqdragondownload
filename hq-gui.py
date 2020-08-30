from appJar import gui
from time import sleep
import requests
import os
from lxml import html
#Download https://chromedriver.storage.googleapis.com/index.html?path=
def press(button):
    if button == "Submit":
        headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        a=app.getEntry("addr")
        url=str(app.getEntry("Url"))
        n=int(app.getEntry("N de pags"))
        name=app.getEntry("Nome")
        cap=app.getEntry("Capítulo")
        os.system("cd {} && mkdir {}-{}".format(a,name,cap))
        page=requests.get(url, headers=headers)
        tree=html.fromstring(page.content)

        i=1

        print("[+]Downloading...[+]")
        while i <= n:
            hq=tree.xpath('//img[@pag="{}"]/@src'.format(i))
            src=str(*hq)
            img= requests.get(src, headers=headers)
            img_data=img.content
            arq=open("{}-{}\\image{}.jpg".format(name,cap,i), 'wb')
            arq.write(img_data)
            arq.close()
            i=i+1

        print("[+]Download finish[+]")  
        app.infoBox("ok", "Download finish")
        app.stop()
    else:
        app.stop()

app=gui("Download HQ", "720x620")
app.setBg("black")
app.setFg("red")
app.setFont(14)
app.addLabel("Download HQ em https://hqdragon.com/")
app.addLabel("Exemplo da Url:")
app.addLabel("https://hqdragon.com/leitor/Motoqueiro_Fantasma_Cosmico_(2018)/01")
app.addDirectoryEntry("addr")
app.addLabelEntry("Url")
app.addLabelEntry("N de pags")
app.addLabelEntry("Nome")
app.addLabelEntry("Capítulo")
app.addLabel("Criador", text="by MrPowerUp", column=4)
app.addButtons(["Submit", "Cancel"], press)


app.go()