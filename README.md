# Stock-Predictor

This Stock Predictor uses SciKit-Learn and Pandas in order to test and and analyze data.

To use, download the the zip file, open up on terminal and run python -i Prediction/future_pred.py

RESULTS:
- this will return a list of companies, using machine learning, that are projected to outperform for a year long hold.
- this also returns testing data on how accurate the algrarithm is, after adding the Company Type (Industrials, IT, ect..) to   the list of features,the accuracy stayed around the same, but the investment return increated by around 5%.
  I beleive this is a good sign since the predicted investments are having a very strong outperformance compared and ones that
  that it predicts to underperform.
- Ones that it predicts to underperform, but ends up overforming, are normally overperforming by a low margin.

DATA:

-The testing data is taken off of Yahoo Finance and dating back to the year 2000.
-present data is also taken off of Yahoo Finance for future predictions.
