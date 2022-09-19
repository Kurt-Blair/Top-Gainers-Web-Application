from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import boto3
import sys
import pandas
from filters import datetimeformat, file_type
from io import StringIO

s3 = boto3.client(
    's3',
    aws_access_key_id="X",
    aws_secret_access_key="X")


app = Flask(__name__)
Bootstrap(app)
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/files')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket('gainerbucket')
    summaries = my_bucket.objects.all()

    return render_template('files.html', files=summaries)


@app.route('/gainers')
def gainers():

    client = boto3.client('s3')
    bucket_name = 'gainerbucket'
    object_key = 'gainers.csv'
    csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    df = pandas.read_csv(StringIO(csv_string))
    result = df.to_html(classes='table table-striped')

    return render_template('gainers.html', table=result)


if __name__ == '__main__':
    app.run()
