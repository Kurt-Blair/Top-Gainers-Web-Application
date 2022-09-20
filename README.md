# flask-s3-web-application by Kurt Blair

Web application created with flask and bootstrap to display top gainers in the stock market today.

I have a separate AWS lambda function to call a financial markets API and store then manipulate the response in a pandas dataframe, then upload it it to S3 as a CSV file.
The job lambda function is scheduled to run every 2 minutes during trading hours.

I have an AWS EC2 instance to hosting Flask web application which reads the S3 file above as displays it on the webpage as an HTML table: https://bit.ly/3Uk5E0l  


