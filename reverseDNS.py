#reverse dns example by SiberianHacker (Shwepsik)
import requests
from threading import Thread
import urllib.request
import random

def findTitle(url):
    try:
        webpage = urllib.request.urlopen(url).read()
        title = str(webpage, "utf-8").split('<title>')[1].split('</title>')[0]
    except:
        pass
    else:
        return title

def writer(String, fileName):
    gg = open(fileName, mode='a')
    gg.write(String + '\n')
    print("Writed! " +String)

def scan():
    while True:
        reg = "http://"+ str(random.randrange(1, 255)) + "." + str(random.randrange(1, 255)) + "." + str(random.randrange(1, 255)) + "." + str(random.randrange(1, 255)) + ":80"
        try:
            req = requests.get(reg)
        except:
            pass
        else:
           writer(req.url + " " + findTitle(req.url), "ReverseDNS.TXT")
    print("Работа никогда не завершена")
 
for thr in range(500):
    Thread(target=scan).start()