import json
import boto3
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.storage.blob import BlobServiceClient
"""
    implementing a service migration that connects AWS lambda functions to Azure services and vice versa
    including setting up the required permissions, configuring the services, and writing the integration code.

    1. AWS and Azure accounts with appropriate permissions
    2. AWS CLI and Azure CLI installed and configured on your local machine 

"""

# lambda function code to interact with azure services 
def lambda_handler(event, context):
    # Initialize the Azure credential
    credential = DefaultAzureCredential()

    # Replace with your Azure subscription ID
    subscription_id = 'YOUR_AZURE_SUBSCRIPTION_ID'

    # Initialize the Resource Management client
    resource_client = ResourceManagementClient(credential, subscription_id)

    # Replace with your Azure storage account name and container name
    storage_account_name = 'YOUR_STORAGE_ACCOUNT_NAME'
    container_name = 'YOUR_CONTAINER_NAME'

    # Construct the Blob service client URL
    blob_service_client_url = f"https://{storage_account_name}.blob.core.windows.net"

    # Initialize the Blob Service client
    blob_service_client = BlobServiceClient(account_url=blob_service_client_url, credential=credential)

    # List blobs in the container
    container_client = blob_service_client.get_container_client(container_name)
    blob_list = container_client.list_blobs()

    # Print the blob names
    for blob in blob_list:
        print(f"Blob name: {blob.name}")

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully accessed Azure Blob Storage from AWS Lambda')
    }


def main():
    # Initialize AWS client
    session = boto3.Session(
        aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',
        aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
        region_name='YOUR_AWS_REGION'
    )
    s3_client = session.client('s3')

    # Replace with your S3 bucket name
    bucket_name = 'YOUR_S3_BUCKET_NAME'

    # List objects in the S3 bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    # Print the object keys
    for obj in response.get('Contents', []):
        print(f"Object key: {obj['Key']}")

    return function.HttpResponse(
        json.dumps('Successfully accessed AWS S3 from Azure Function'),
        mimetype="application/json"
    )


if __name__ == "__main__":
    main()

