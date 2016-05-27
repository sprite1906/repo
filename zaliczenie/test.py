import boto3

bucket_name = '167429-sprite'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.put_object(Key='przeslany.txt', Body=open('test.txt', 'rb'))
