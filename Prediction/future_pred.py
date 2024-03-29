import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
style.use("ggplot")

#things to also check
    #trading volume,

#predicts weither the stock was an outperformer (1) or underperformer (0)

FEATURES =  ['DE Ratio',
             'Trailing P/E',
             'Price/Sales',
             'Price/Book',
             'Profit Margin',
             'Operating Margin',
             'Return on Assets',
             'Return on Equity',
             'Revenue Per Share',
             'Market Cap',
             'Enterprise Value',
             'Forward P/E',
             'PEG Ratio',
             'Enterprise Value/Revenue',
             'Enterprise Value/EBITDA',
             'Revenue',
             'Gross Profit',
             'EBITDA',
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior ',
             'Company Type']

def Build_Data_Set():
    data_df = pd.DataFrame.from_csv("Data/key_stats_acc_WITH_TYPE_NA.csv")
    data_df = data_df.replace("Energy",0).replace("Consumer Discretionary",1).replace("Financials",2).replace("Consumer Staples",3).replace("Information Technology",4).replace("Industrials",5).replace("Health Care",6).replace("Real Estate",7).replace("Utilities",8).replace("Materials",9).replace("Telecommunication Services",10)
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    # hi = hi.replace("NaN",0).replace("N/A",0)

    #figure out tomorrow

    ######################
    # time.sleep(1500)
    X = np.array(data_df[FEATURES]).tolist()
    X = np.nan_to_num(X)

    y = (data_df["Status"].replace("underperform",0).replace("outperform",1).values.tolist())

    X = preprocessing.scale(X)

    Z = np.array(data_df[["stock_p_change","sp500_p_change"]])
    Z = np.nan_to_num(Z)
    return X,y,Z

def Analysis():

    test_size = 1000

    invest_amount = 10000
    total_invests = 0
    if_market = 0
    if_strat = 0

    X, y, Z = Build_Data_Set()
    print(len(X))
    clf = svm.SVC(kernel="linear", C=1.0)
    clf.fit(X[:-test_size],y[:-test_size])
    correct_count = 0.00

    for x in range(1, test_size + 1):
        if clf.predict(X[-x].reshape(1,-1))[0] == y[-x]:
            correct_count += 1
        if clf.predict(X[-x].reshape(1,-1))[0] == 1:
            invest_return = invest_amount + (invest_amount * (Z[-x][0]/100))
            market_return = invest_amount + (invest_amount * (Z[-x][1]/100))

            total_invests += 1
            if_market += market_return
            if_strat += invest_return

    print("Total Trades:",total_invests)
    print("If invested:", if_strat)
    print("If market", if_market)
    print("Correct Count: ",correct_count,"Test Size: ",float(test_size))
    print("Accuracy:", (correct_count/test_size) * 100.00)

    compared = ((if_strat - if_market) / if_market) * 100.0
    do_nothing = total_invests * invest_amount
    #-------
    avg_market = ((if_market - do_nothing) / do_nothing) * 100.0
    avg_strat = ((if_strat - do_nothing) / do_nothing) * 100.0
    #--------



    print("Compared to market, we earn",str(compared)+"% more")
    print("Average investment return:", str(avg_strat)+"%")
    print("Average market return:", str(avg_market)+"%")

    data_df = pd.DataFrame.from_csv("Data/pull_data_W_NA.csv")
    data_df = data_df.replace("Energy",0).replace("Consumer Discretionary",1).replace("Financials",2).replace("Consumer Staples",3).replace("Information Technology",4).replace("Industrials",5).replace("Health Care",6).replace("Real Estate",7).replace("Utilities",8).replace("Materials",9).replace("Telecommunication Services",10)
    X = preprocessing.scale(X)
    X = np.array(data_df[FEATURES].values).tolist()
    X = np.nan_to_num(X)

    Z = data_df["Ticker"].values.tolist()

    invest_list = []

    for i in range(len(X)):
        p = clf.predict(X[i].reshape(1,-1))[0]
        if p == 1:
             invest_list.append('Buy: '+Z[i])
    print("Projected One-Year outperformers: ",invest_list)
    print(len(invest_list))



Analysis()
