import boto3
import json
from decimal import Decimal

print('Loading function')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def get_all_votes():
    dynamo_table_name = 'VotingTable'
    dynamo = boto3.resource('dynamodb').Table(dynamo_table_name)

    response = dynamo.scan()
    all_votes = response.get('Items', [])

    return all_votes

def lambda_handler(event, context):
    try:
        all_votes = get_all_votes()

        return {
            'statusCode': 200,
            'body': json.dumps(all_votes, cls=DecimalEncoder)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
