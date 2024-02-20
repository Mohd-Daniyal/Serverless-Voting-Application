import boto3
from decimal import Decimal
import json

dynamo_table_name = 'VotingTable'
dynamo = boto3.resource('dynamodb').Table(dynamo_table_name)

ALLOWED_LANGUAGES = {'CShar', 'Python', 'JavaScript', 'Go', 'Java', 'Swift'}

def get_language_info(language):
    if language not in ALLOWED_LANGUAGES:
        raise ValueError(f'Invalid language: {language}. Allowed languages are: {ALLOWED_LANGUAGES}')

    response = dynamo.get_item(Key={'Language': language})
    item = response.get('Item', {})
    return {
        'language': item.get('Language', ''),
        'image': item.get('Image', ''),
        'documentation_url': item.get('Documentation', ''),
        'total_votes': str(item.get('Votes', 0))
    }

def lambda_handler(event, context):
    try:
        print("Event:", json.dumps(event))
        language = event['pathParameters']['language']
        print("Language:", language)
        language_info = get_language_info(language)
        return {'statusCode': 200, 'body': json.dumps(language_info)}
    except ValueError as ve:
        return {'statusCode': 400, 'body': str(ve)}
    except Exception as e:
        return {'statusCode': 500, 'body': f'Error: {str(e)}'}
