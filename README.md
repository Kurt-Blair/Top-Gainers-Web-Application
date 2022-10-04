# flask-s3-web-application

Web application created with Flask and Bootstrap to display top gainers in the stock market today.

I have a separate AWS lambda function to call a financial markets API and store/manipulate the response in a pandas dataframe, then upload it to S3 as a CSV file.

I have an AWS EC2 instance hosting my Flask web application which reads the S3 file and displays it on a webpage as an HTML table: http://tinyurl.com/top-gainers
