# Streaming Finance Data with AWS Lambda

This project aims to provision Lambda functions to generate near real time finance data records for downstream processing and interactive querying. 

Lambda URL: https://pugc7ko1ba.execute-api.us-east-2.amazonaws.com/default/STA9760-P3-DataCollector

**Infrastructure**

This project consists of three major infrastructure elements that work in tandem:
- A lambda function that collects our data (DataCollector)
- A lambda function that transforms and places data into S3 (DataTransformer)
- A serverless process that allows us to query our s3 data (DataAnalyzer)

![Infrastructure](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/infrastructure.png?raw=true)


In the collector lambda, using the yfinance module, I grabbed one full day’s worth of stock HIGH and LOW prices for each company listed above on Thursday, May 14th 2020, at an one minute interval. Note that by “full day” we mean one day of stock trading, which is not 24 hours.

- Facebook (FB)
- Shopify (SHOP)
- Beyond Meat (BYND)
- Netflix (NFLX)
- Pinterest (PINS)
- Square (SQ)
- The Trade Desk (TTD)
- Okta (OKTA)
- Snap (SNAP)
- Datadog (DDOG)

## DataCollector Lambda Configuration Page 

![Lambda](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/lambda.png?raw=true)

## Kinesis Data Firehose Delivery Stream Monitoring

![Firehose](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/firehose.png?raw=true)



## [Analysis](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/Analysis.ipynb)


***Jack Yang Copy Right 2020***
https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda
