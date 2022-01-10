#pip3 install lxml
#pip3 install beautifulsoup4
# pip install pymsteams

import time
import requests
from bs4 import BeautifulSoup
import pymsteams

z = ""
repres1 = ""



#########################################  webhook  ############################################
conhook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/ce5049bfeffb44f6870e25b7d6ad1a55/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"





####################################### SOURCE URL ######################################
su1 = "https://thinkit.co.jp/search/site/"
su2 = "https://qiita.com/search?page=1&q=kubernetes"

sulist = ["https://thinkit.co.jp/search/site/", "https://qiita.com/search?page=1&q="]




#########################################KEYWORD#########################################
##containers


conk = {"conk1":"docker", "conk2":"kubernetes", "conk3":"docker-compose", "conk4":"open shift", "conk5":"tanzu"}
conknum = len(conk) 
conknum = int(conknum)
conlist = []


######################################## sc #################################################


def coll():
    global repres1
    global i
    global conurl1
    global z
    
    res1 = requests.get(conurl1)
    soup1 = BeautifulSoup(res1.text, 'html.parser')
    
    print(sulist[0])
    if z == "https://thinkit.co.jp/search/site/":
        class1 = soup1.find_all(["h3", "h2"], class_="list")

        class1 = str(class1)

        class1 = class1.replace('</h3>', '')
        class1 = class1.replace('</a>', '')
        class1 = class1.replace('<h3 class="list">', '')
        class1 = class1.replace('<h2 class="list">','')
        class1 = class1.replace('</h2>','')
        class1 = class1.replace('[', '')
        class1 = class1.replace(']', '')
        class1 = class1.replace('[', '')
        class1 = class1.replace('<a href=', '')
        class1 = class1.replace('"', '')
        class1 = class1.replace(',', '')
        class1 = class1.replace('>', ' ')
        class1 = class1.split(' ')
        
        
        repres1 = [s.replace('/article', 'https://thinkit.co.jp/article')for s in class1]
        repres1 = [s.replace('/topics', 'https://thinkit.co.jp/topics')for s in repres1]
        repres1 = [s.replace('/news/bn/', 'https://thinkit.co.jp/news/bn/')for s in repres1]
        repres1 = str(repres1)
        repres1 = repres1.replace('[', '')
        repres1 = repres1.replace(']', '')
        repres1 = repres1.replace('[', '')
        repres1 = repres1.replace('<a href=', '')
        repres1 = repres1.replace('"', '')
        repres1 = repres1.replace('\'', '')
        repres1 = repres1.replace(',', '')
        repres1 = repres1.replace('>', ' ')
        repres1 = repres1.replace('http', '\r \nhttp')

    elif z == sulist[1]:
        class1 = soup1.find_all("h1", class_="searchResult_itemTitle")
        class1 = str(class1)
        
        class1 = class1.replace('<em>', '')
        class1 = class1.replace('</em>', '')
        class1 = class1.replace('</h1>', '')
        class1 = class1.replace('</a>', '')
        class1 = class1.replace("'",'')
        class1 = class1.replace('<h1 class="searchResult_itemTitle">','')
        class1 = class1.replace('>', ' ')
        class1 = class1.replace('[', '')
        class1 = class1.replace(']', '')
        class1 = class1.replace(',', '\r \n')
        class1 = class1.replace('<a href="',' https://qiita.com')
        class1 = class1.replace('"','')
        repres1 = class1


    else:
        print("ひっかかってない")
        

    print(repres1)






##############################  teams  #####################################################
def send():
    global conhook
    global repres1
 
 
    myTeamsMessage = pymsteams.connectorcard(conhook)
    myTeamsMessage.title(str(i) + "関係のnewsが更新されました")
    myTeamsMessage.text(repres1)
    myTeamsMessage.send()
    
    

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
    
    fir = 0

    for i in range(conknum):
        conlistka.append("a")


    while True:
        aaa = 0
        print("スクレイピング開始します")
        for z in sulist:
            for i in conk.values():
                if fir == 0:
                    conlistka.append("a")
                else:    
                    path
                
                conurl1 = str(z) + str(i)
                coll()
                conlist.append(repres1)
                print(repres1)
                
                ccc = conlist[aaa]
                ddd = conlistka[aaa]
                
                print(ccc)
                print(ddd)
                
            if ccc == ddd:
                print("同じ")
                    
            else:
                send()
                conlistka[aaa] = conlist[aaa]
            
                aaa = aaa + 1        
        print("時間待機")     
        time.sleep(3600)        


maincon()