#pip3 install lxml
#pip3 install beautifulsoup4
# pip install pymsteams

import time
import requests
from bs4 import BeautifulSoup
import pymsteams
rrr = ""
z = ""
repres1 = ""



#########################################  webhook  ############################################
conhook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/9a99f6916bdf49ecaaad44fe3df51be5/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
cicdhook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/3596153ae8c94242b55f0bcd9612ef92/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
cloudhook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/3810c89c769249e59dfdeda17faa7b71/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
iachook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/2f93b868505f422babcdbf41e2fa3f36/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
nethook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/9eacb5a1c23e4532a5fabf980301bbd1/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
sechook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/f022aba5e807471b82ff3d984a012e48/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
kasohook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/7877639d19d94ba5873e0b47a44449eb/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"
kansihook = "https://smetrocit.webhook.office.com/webhookb2/58cf3a31-f9f6-4b00-b0bf-ebf58845ed65@a2c3e6fc-a959-4d2f-b374-4593a068ff9c/IncomingWebhook/a29338171ec048f692e2aeca66823046/4e1c6fc9-4bcc-46e5-9fb5-40d14d4ef248"


####################################### SOURCE URL ######################################
su1 = "https://thinkit.co.jp/search/site/"
su2 = "https://qiita.com/search?page=1&q=kubernetes"

sulist = ["https://thinkit.co.jp/search/site/", "https://qiita.com/search?&sort=created&q=", "https://qiita.com/search?q="]




#########################################KEYWORD#########################################
##containers

keylist = []

conk = {"conk1":"docker", "conk2":"kubernetes", "conk3":"docker-compose", "conk4":"open shift", "conk5":"tanzu", "conk6":"rancher"}
conknum = len(conk) 
conknum = int(conknum)
keylist.append(conk)

cicdk = {"cicdk1":"circle ci"}
cicdnum = len(cicdk) 
cicdnum = int(cicdnum)
keylist.append(cicdk)

cloudk = {"cloudk1":"gcp", "cloudk2":"aws", "cloudk3":"cncf", "cloudk4":"oracle", "cloudk5":"cloudstack", "cloudk6":"openstack"}
cloudknum = len(cloudk) 
cloudknum = int(cloudknum)
keylist.append(cloudk)

iack = {"iack1":"ansible", "iack2":"ansible", "iack3":"terraform", "iack4":"pulumi", "iack5":"vagrant"}
iacknum = len(iack) 
iacknum = int(iacknum)
keylist.append(iack)

netk = {"netk1":"vxlan", "netk2":"netflow"}
netknum = len(netk) 
netknum = int(netknum)
keylist.append(netk)

seck = {"seck1":"nmap"}
secknum = len(seck) 
secknum = int(secknum)
keylist.append(seck)

kasok = {"kasok1":"kvm","kasok2":"vmware", "kasok3":"xen", "kasok4":"proxmox", "kasok5":"esxi"}
kasoknum = len(kasok) 
kasoknum = int(kasoknum)
keylist.append(kasok)

kansik = {"kansik1":"zabbix", "kansik2":"prometheus", "kansik3":"prometheus expoter", "kansik4":"grafana", "kansi5":"elk", "kansik6":"elastic search", "kansik7":"kibana", "kansik8":"logstash", "kansik9":"Loki"}
kansiknum = len(kansik) 
kansiknum = int(kansiknum)
keylist.append(kansik)


conlist = []


######################################## sc #################################################


def coll():
    global repres1
    global i
    global conurl1
    global z
    
    res1 = requests.get(conurl1)
    soup1 = BeautifulSoup(res1.text, 'html.parser')
    
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
        repres1 = str(repres1)

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
    
    if count <= conknum*zn:
        myTeamsMessage = pymsteams.connectorcard(conhook)
        
    if count > conknum*zn and count <= (conknum + cicdnum)*zn:
        myTeamsMessage = pymsteams.connectorcard(cicdhook)
        
    if count > (conknum + cicdnum)*zn and count <= (conknum + cicdnum + cloudknum)*zn:
        myTeamsMessage = pymsteams.connectorcard(cloudhook)
        
    if count > (conknum + cicdnum + cloudknum)*zn and count <= (conknum + cicdnum + cloudknum + iacknum)*zn:
        myTeamsMessage = pymsteams.connectorcard(iachook)
        
    if count > (conknum + cicdnum + cloudknum + iacknum)*zn and count <= (conknum + cicdnum + cloudknum + iacknum + netknum)*zn:
        myTeamsMessage = pymsteams.connectorcard(nethook)
        
    if count > (conknum + cicdnum + cloudknum + iacknum + netknum)*zn and count <= (conknum + cicdnum + cloudknum + iacknum + netknum + secknum)*zn:
        myTeamsMessage = pymsteams.connectorcard(sechook)
        
    if count > (conknum + cicdnum + cloudknum + iacknum + netknum + secknum)*zn and count <= (conknum + cicdnum + cloudknum + iacknum + netknum + secknum + kasoknum)*zn:
        myTeamsMessage = pymsteams.connectorcard(kasohook)
        
    if count > (conknum + cicdnum + cloudknum + iacknum + netknum + secknum + kasoknum)*zn and count <= (conknum + cicdnum + cloudknum + iacknum + netknum + secknum + kasoknum + kansiknum)*zn:
        myTeamsMessage = pymsteams.connectorcard(kansihook)

        
    myTeamsMessage.title(str(i) + "関係のnewsが更新されました")
    repres1 = str(repres1)
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
    global rrr
    
    fir = 0




    while True:
        aaa = 0
        print("スクレイピング開始します")
        for rrr in keylist:
            for z in sulist:
                for i in rrr.values():
                    print(rrr)
                    if fir == 0:
                        conlistka.append("a")
                    else:    
                        path
                    
                    conurl1 = str(z) + str(i)
                    print(conurl1)
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
        print("時間待機")     
        time.sleep(3600)        


maincon()