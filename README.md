#### Overview
Here i have developed some of standard scripts to process each stocks 5 year History price and find correct buy level for NSE stocks. 

packages used are:

    1.datetime
    2.nsepy
    3.numpy
    4.pandas
    5.sys

#####
install all the required packages by running below command.

    pip install -r requirements.txt

- Here we will process historical data for around 5 year.
- we will try to get some insight from Stock Moving average
- Validate history price and predict this week price action using signal.
- Output of the file can be consumed by different applications for future prediction model creation

-------------------------------------------------------
Over the time we have considered different combinations and have validated result/price against historical values.

#### Next action items
   - add RSI indicator to give more insight like: over buy / under buy
      - here is a good example to integrate https://handsoffinvesting.com/calculate-and-analyze-rsi-using-python/
   - add files into S3 or Read files from a file system to automate the process. 
   - add script into AWS Lambda and then enable AWS watch to monitor the Daily processing of data.
   - add AWS watch to monitor usage.
   - store every day execution data with below format in s3 bucket.
      - yyyy-mm-dd hh:mm     
   - remove hardcoded stock names from files.
   

#### Sample Output
    Once you run application will give output signal on which trade to buy next from the attribute named as 'Signal' we also can modify example accordingly
    then we can filter .txt files with something similar to  "1.0       1.0" or "Today Date"  and find some insight of the current data
    Example:

    Line 558: 2021-*****  SHREECEM     EQ  30663.35   28668  28068.2650   27975.261     1.0       1.0
    Line 638: 2021-*****  EICHERMOT     EQ   2805.00   287427   2656.9625    2652.001     1.0       1.0
    Line 978: 2021-*****  DALBHARAT     EQ  2409.40  466844   2108.2275    2098.420     1.0       1.0
    Line 302: 2021-*****  RECLTD     EQ  158.05   4433719    149.8375     149.752     1.0       1.0
