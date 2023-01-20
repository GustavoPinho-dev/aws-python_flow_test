import os

class Config:
    
    S3_BUCKET_NAME = os.getenv(
        'S3_BUCKET_NAME', 'programminglanguagesfiles'
    )

    DYNAMODB_TABLE_NAME = os.getenv(
        'DYNAMODB_TABLE_NAME', 'user_data_test'
    )