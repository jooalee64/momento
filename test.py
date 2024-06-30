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
    # message = event.get("message", "hello from lambda")
    # configure AWS s3 client
    s3_client = boto3.client('s3')

    # connect to azure blob storage using azure functions credential
    credential = DefaultAzureCredential()
    from azure.storage.blob import BlobServiceClient
    blob_service_client = BlobServiceClient()
    blob_service_client = BlobServiceClient(account_url="your-azure-storage-account-url", credential=credential)
    blob_client = blob_service_client.get_blob_client(container_name="my-azure-blob-container", blob_name="message.txt")

    # Upload the message to Azure Blob Storage (replace with your actual logic)
    blob_client.upload_blob(message)
    print(f"Uploaded message: '{message}' to Azure Blob Storage")

    return {
         'statusCode': 200,
         'body': message
     }


# Azure Function (triggered by HTTP request)
def main(req: Function):
    message = req.params.get('message')
    # simulate processing the message (replace with your actual logic)
    processed_message = f"Azure Function received: {message}"
    # trigger AWS lambda function (repalce with lambda function name)
    response = lambda_client.invoke(
        FunctionName = "my-lambda-function-name"
        payload = json.dumps({"message": processed_message})
    )


if __name__ == "__main__":
    main() 
