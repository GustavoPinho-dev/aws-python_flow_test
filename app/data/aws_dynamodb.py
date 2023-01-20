import boto3
import logging
import pandas as pd
from configuration.config import Config

class AWSdynamodb:
    def __init__(self) -> None:
        self.instantiate_dynamo()
    
    def instantiate_dynamo(self):
        try:
            self.resource = boto3.resource('dynamodb')
            self.table = self.resource.Table(Config.DYNAMODB_TABLE_NAME)
        except Exception as ex:
            logging.error(str(ex))

    def put_item_in_database(self, item):
        try:
            #API expect data in dictionary format
            self.table.put_item(Item = item)
        except Exception as ex:
            logging.error(str(ex))