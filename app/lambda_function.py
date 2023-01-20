import json
import logging
from data.aws_s3 import AWSs3
from data.aws_dynamodb import AWSdynamodb

def lambda_handler(event, context):
    try:
        aws_s3 = AWSs3()
        aws_dynamo = AWSdynamodb()

        df = aws_s3.get_last_object()

        jsonData = df.to_json(orient='records')

        usersData = json.loads(jsonData)

        for current_data in usersData:
            aws_dynamo.put_item_in_database(current_data)
    
    except Exception as ex:
        logging.error(str(ex))

if __name__ == "__main__":
    event = ''
    context = None
    
    lambda_handler(event, context)


