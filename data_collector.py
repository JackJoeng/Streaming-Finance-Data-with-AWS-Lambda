import json
import boto3
import random
import os
import subprocess
import sys

def install(package):
    subprocess.check_call([
        sys.executable, 
        "-m", 
        "pip", 
        "install", 
        "--target",
        "/tmp",
        package])
        
install('yfinance')

sys.path.append('/tmp')

import yfinance as yf

def lambda_handler(event, context):

    stocks = ['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']
    start_date = '2020-05-14'
    end_date = '2020-05-15'
    interval = '1m'
    period = '1d'

    download = yf.download(
            tickers = ' '.join(stocks),
            start = start_date,
            end = end_date,
            period = period,
            interval = interval,
            group_by = 'ticker'
        ) 

    data = []

    for stock in stocks:
        for index, rows in download[stock].iterrows():
            data += [{
                "high": rows['High'], 
                "low": rows['Low'], 
                "ts": str(index), 
                "name": stock
                }]
    
    fh = boto3.client("firehose", "us-east-2")
    as_jsonstr = json.dumps(data)
    
    for row in data:
        as_jsonstr_row = json.dumps(row)

        fh.put_record(
            DeliveryStreamName="STA9760-P3-Delivery-Stream", 
            Record={"Data": as_jsonstr_row.encode('utf-8')})

    # return
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }