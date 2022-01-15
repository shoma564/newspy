#pip3 install lxml
#pip3 install beautifulsoup4
# pip install pymsteams

import re
import time
import requests
from bs4 import BeautifulSoup
import pymsteams
rrr = ""
z = ""
repres1 = ""



#########################################  webhook  ############################################
souhook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/0cdc813484f04da0ba3147779a8979eb/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
sikanhook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/eeb6b416490c42bdbaad8d9c024f9dcc/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"

####################################### SOURCE URL ######################################


sulist = ["https://www.gizmodo.jp/", "https://www.lifehacker.jp/articles/"]
#"https://newspicks.com/theme-news/technology/"


conlist =[]

######################################## sc #################################################


def coll():
    global repres1
    global i
    global conurl1
    global z
    
    res1 = requests.get(conurl1)
    print(conurl1)
    soup1 = BeautifulSoup(res1.text, 'html.parser')


    if z == sulist[0]:
        class1 = soup1.find_all("h3")
        class1 = str(class1)
        class1 = class1.replace('[', '')
        class1 = class1.replace(']', '')
        class1 = class1.replace('<h3 class="p-slider1-cardTitle">', '\r \n')
        class1 = class1.replace('<h3 class="p-timeline-cardTitle">', '\r \n')
        class1 = class1.replace('<h3 class="s-Ranking_ListItemPostTitle">', '\r \n')
        class1 = class1.replace('<h3 class="p-post-reviewList-CardTitle">', '\r \n') 
        class1 = class1.replace('<h3 class="s-body-cardList3CardTitle', '\r \n') 
        class1 = class1.replace('">', ' ')
        class1 = class1.replace('<a href="/', 'https://www.gizmodo.jp/')
        class1 = class1.replace('<a href="', '')
        class1 = class1.replace('</a></h3>', '')
        class1 = class1.replace(',', '')        
        repres1 = class1

    elif z == sulist[1]:
        
        class1 = soup1.find_all(["object"])
        
#        class1 = soup1.find_all(class_=[re.compile("nav_st"), re.compile("hotkeyword"), re.compile("article")])
        class1 = str(class1)
        class1 = class1.replace('[', '')
        class1 = class1.replace(']', '')
        class1 = class1.replace('<object>', '')
        class1 = class1.replace('</object>', '')
        class1 = class1.replace('<a class=', '')
        class1 = class1.replace('</a>', '')
        class1 = class1.replace('#<!-- -->', '')
        class1 = class1.replace('href="', 'https://www.lifehacker.jp')
        class1 = class1.replace('<a class=', '')
        class1 = class1.replace('<svg class="articles_pArticles_ItemCatIcon__3xf0f" height="8" viewbox="0 0 20 8" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M20.5,5.48A1.139,1.139,0,0,0,19.571,5L4.143,5.006A1.141,1.141,0,0,0,3,6.143v5.714a1.141,1.141,0,0,0,1.143,1.137L19.571,13a1.139,1.139,0,0,0,.931-.48L23,9,20.5,5.48Z" data-name="パス 776" fill="#1B9B6F" id="パス_776" transform="translate(-3 -5)"></path></svg>', '')
        class1 = class1.replace('"hotkeyword_sHotkeyword_ItemTag__3iVQY" ', '')
        class1 = class1.replace('" type="button">', ' ')        
        class1 = class1.replace('<svg height="28" viewbox="0 0 28 28" width="28" xmlns="http://www.w3.org/2000/svg"><path class="articles_pArticles_HeroCatIcon__39toJ" d="M21.5,10.48a1.12,1.12,0,0,0-.92-.48H5.14A1.15,1.15,0,0,0,4,11.14v5.72A1.15,1.15,0,0,0,5.14,18H20.58a1.15,1.15,0,0,0,.93-.48L24,14Z" data-name="icon category"', '')
        class1 = class1.replace('"articles_pArticles_ItemCat__1sXyg"', '')
        class1 = class1.replace(',', '\r \n')
        class1 = class1.replace('hotkeyword_sHotkeyword_ItemTitleLink__1Jr-n', '')
        class1 = class1.replace('', '')
        class1 = class1.replace('">', ' ')                
        class1 = class1.replace('"', '')
        
        
        
        class1 = str(class1)
        repres1 = class1

    else:
        print("ひっかかってない")




count = 0

##############################  teams  #####################################################
def send():
    global conhook
    global repres1
    global count
    count = count +1
    global i
    global myTeamsMessage
    
    zn = len(sulist)
    zn = int(zn)
    
    myTeamsMessage = pymsteams.connectorcard(souhook)    
    myTeamsMessage.title("newsが更新されました\r \n" + str(z))
    repres1 = str(repres1)
    myTeamsMessage.text(repres1)
    myTeamsMessage.send()
    

def sikan():
    myTeams = pymsteams.connectorcard(sikanhook)        
    myTeams.title("監視結果")
    myTeams.text("総合ニューススクレイピングは正常に動作しています。")
    myTeams.send()
    
    

####################################### change ur  ######################################

aaa = 0
conurl1 = ""
conlistka = []

def maincon():
    global repres1
    global conlist
    global su1
    global conk
    global conknum
    global conurl1
    global i
    global aaa
    global conlistka
    global sulist
    global z
    global rrr
    
    fir = 0




    while True:
        aaa = 0
        print("スクレイピング開始します")
        for z in sulist:
            
            if fir == 0:
                conlistka.append("a")
            else:    
                path
            conurl1 = z
            coll()
            conlist.append(repres1)               
            ccc = conlist[aaa]
            ddd = conlistka[aaa]
                    
                    
            if ccc == ddd:
                print("同じ")
                        
            else:
                print(repres1)
                send()
                conlistka[aaa] = conlist[aaa]
            time.sleep(2)
            aaa = aaa + 1
              
        sikan() 
        print("時間待機")           
        time.sleep(3600)        


maincon()