import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': '<html><head></head><h1>Hello, CDK! You have hit {}\n</h1></html>'.format(event['path'])
    }