import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from my CICD project Lambda - this is the upgraded version 2 after I fixed Node.js 24 compatibility')
    }