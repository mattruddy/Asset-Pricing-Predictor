import pandas as pd
import os
import time
from datetime import datetime
from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")



def Key_Stats(gather=['Company Type','Ticker']):
    df = pd.DataFrame(columns = ['Company Type','Ticker'])

    file_list = os.listdir("/Users/mattruddy/Desktop/intraQuarter/_KeyStats")

    for each_file in file_list[1:]:
        ticker = each_file.split(".html")[0]
        try:
            full_file_path = "/Users/mattruddy/Desktop/intraQuarter/List of S&P 500 companies - Wikipedia.htm"
            source = open(full_file_path,"r").read()
        except Exception as e:
            pass
        try:
            comp_type = source.split('href="https://www.sec.gov/cgi-bin/browse-edgar?CIK='+ticker.upper()+'&amp;action=getcompany">reports</a></td>\n<td>')[1].split('</td>')[0]
        except Exception as e:
            pass
        df = df.append({'Company Type':comp_type,'Ticker':ticker,},ignore_index = True)
    df.to_csv("company_type.csv")
