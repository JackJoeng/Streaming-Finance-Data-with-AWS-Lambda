# Streaming Finance Data with AWS Lambda

This project aims to provision Lambda functions to generate near real time finance data records for downstream processing and interactive querying. 

Lambda URL: https://pugc7ko1ba.execute-api.us-east-2.amazonaws.com/default/STA9760-P3-DataCollector

## Technologies

- AWS Lambda
- AWS Kinesis
- AWS S3
- AWS Glue
- AWS Athena

## Infrastructure

This project consists of three major infrastructure elements that work in tandem:
- A lambda function that collects our data (DataCollector)
- A lambda function that transforms and places data into S3 (DataTransformer)
- A serverless process that allows us to query our s3 data (DataAnalyzer)

![Infrastructure](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/infrastructure.png?raw=true)


In the collector lambda, using the yfinance module ([documentation ](https://github.com/ranaroussi/yfinance)here), I grabbed one full day’s worth of stock HIGH and LOW prices for each company listed above on Thursday, May 14th 2020, at an one minute interval. Note that by “full day” we mean one day of stock trading, which is not 24 hours.

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

## Athena Ad-Hoc Queries

![Firehose](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/athena.png?raw=true)

## [Analysis - Check it out ](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/Analysis.ipynb)
https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/Analysis.ipynb


### * Lambda Deployment Package

In order to run lambda functions that also manage dependencies, a "deployment package" must be leveraged, basically a zip file containing your lambda code and all the dependencies it needs all packaged into a single artifact.

This [repo](https://github.com/mottaquikarim/STA9760_simple_deployment_package) from Taq Karim provides a few tools that will help you manage your lambda functions and the dependencies.


***Jack Yang Copy Right 2020***
https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda

