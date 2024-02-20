import boto3
from decimal import Decimal
import json
import decimal

dynamo_table_name = 'VotingTable'
dynamo = boto3.resource('dynamodb').Table(dynamo_table_name)

ALLOWED_LANGUAGES = {'CSharp', 'Python', 'JavaScript', 'Go', 'Java', 'Swift'}

def update_vote_count(language):
    if language not in ALLOWED_LANGUAGES:
        raise ValueError(f'Invalid language: {language}. Allowed languages are: {ALLOWED_LANGUAGES}')

    response = dynamo.update_item(
        Key={'Language': language},
        UpdateExpression='SET Votes = if_not_exists(Votes, :start) + :incr',
        ExpressionAttributeValues={':incr': 1, ':start': Decimal(0)},
        ReturnValues='UPDATED_NEW'
    )
    
    # Convert Decimal to float for JSON serialization
    updated_votes = int(response.get('Attributes', {}).get('Votes', 0))

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': json.dumps({'updated_votes': updated_votes, 'message': 'Vote count updated successfully'})
    }

def lambda_handler(event, context):
    try:
        language = event['pathParameters']['language']
        response = update_vote_count(language)
        return response
    except ValueError as ve:
        return {'statusCode': 400, 'body': str(ve)}
    except Exception as e:
        return {'statusCode': 500, 'body': f'Error: {str(e)}'}
