"""session = boto3.Session(
aws_access_key_id = 'AKIATOBQW6JXZW2N6SGC'
aws_secret_access_key = '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'
)
s3 = session.resource('s3')
import boto3"""
import boto3
client = boto3.client('s3')
response = client.list_objects_v2(
Bucket = 'aws-lambda-trigger-sample1',
)

for key in(response['Contents']):
    print(key)
