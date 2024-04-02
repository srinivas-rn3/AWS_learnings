import json
import boto3
import pymysql

# Configuration
S3_BUCKET_NAME = 'your-s3-bucket-name'
RDS_HOST = 'your-rds-host'
RDS_USER = 'your-rds-username'
RDS_PASSWORD = 'your-rds-password'
RDS_DB_NAME = 'your-rds-db-name'

s3 = boto3.client('s3')
rds = pymysql.connect(host=RDS_HOST, user=RDS_USER, password=RDS_PASSWORD, database=RDS_DB_NAME)

def lambda_handler(event, context):
    # Extract data from S3
    s3_object_key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=S3_BUCKET_NAME, Key=s3_object_key)
    data = response['Body'].read().decode('utf-8')
    
    # Transform data (For demonstration, let's assume we just uppercase it)
    transformed_data = data.upper()
    
    # Load data into RDS
    cursor = rds.cursor()
    try:
        cursor.execute("INSERT INTO your_table (your_column) VALUES (%s)", (transformed_data,))
        rds.commit()
    except Exception as e:
        print(f"Error inserting data into RDS: {e}")
        rds.rollback()
    finally:
        cursor.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('ETL process completed successfully')
    }
