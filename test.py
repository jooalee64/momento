import boto3 # AWS lambda dependencies 
import sys 
import os 
import config

from azure.functions import Function 
from azure.identity import DefaultAzureCredential 

# def start_migration(source, destination):
#     s3 = boto3.resource('s3')
    
    
#     # Get the source and destination bucket objects
#     source = s3.Bucket(source)
#     print(source)
#     pass 
def lambda_handler(event, context):
    
def main():
    start_migration()

if __name__ == "__main__":
    main() 
