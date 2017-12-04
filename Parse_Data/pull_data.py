import urllib
import os
import time

path = "/Users/mattruddy/Desktop/intraQuarter"

def Check_Yahoo():
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]
    for e in stock_list[1:]:
        try:
            e = e.replace("/Users/mattruddy/Desktop/intraQuarter/_KeyStats/","")
            link = "https://finance.yahoo.com/quote/"+str(e)+"/key-statistics?p=AAPL"
            resp = urllib.urlopen(link).read()
            save = "/Users/mattruddy/Desktop/intraQuarter/_KeyStats/"+str(e)+"/"+str(e)+".html"
            store = open(save,"w")
            store.write(str(resp))
            store.close()

        except:
            pass
Check_Yahoo()
