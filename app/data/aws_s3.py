import boto3
import logging
import pandas as pd
from configuration.config import Config
from io import StringIO

class AWSs3:
    def __init__(self) -> None:
        self.instantiate_s3()
    
    def instantiate_s3(self):
        try:
            self.resource = boto3.client('s3')
            self.bucket = Config.S3_BUCKET_NAME
        except Exception as ex:
            logging.error(str(ex))
    
    def get_last_object(self):
        try:
            response = self.resource.list_objects_v2(Bucket=self.bucket)
            all = response['Contents']        
            latest = max(all, key=lambda x: x['LastModified'])

            object_key = latest['Key']
            csv_obj = self.resource.get_object(Bucket=self.bucket, Key=object_key)
            body = csv_obj['Body']
            csv_string = body.read().decode('utf-8')

            data = pd.read_csv(StringIO(csv_string))
            df = pd.DataFrame(data)

            return df
        except Exception as ex:
            logging.error(str(ex))
    
