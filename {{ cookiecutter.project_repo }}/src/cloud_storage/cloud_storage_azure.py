import logging
import os
from azure.storage.blob import BlobServiceClient


def write_file_to_azure_blob_storage(local_file_path):
    """
        Upload file to Azure Blob Storage. Use .env file to get access information.

        Args:
            - local_file_path to upload

        Returns:
            True or False depending on the success of the upload
    """
    # Blob storage access information
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    blob_container_name = os.getenv('AZURE_BLOB_CONTAINER_NAME')
    sas_credential = os.getenv('AZURE_SAS_CREDENTIAL')

    if account_name is not None and blob_container_name is not None and sas_credential is not None and account_name != "" and blob_container_name != "" and sas_credential != "":

        try:
            blob_name = os.path.basename(local_file_path)
            account_url = f"https://{account_name}.blob.core.windows.net"

            # Upload file
            blob_service_client = BlobServiceClient(account_url=account_url, credential=sas_credential)
            blob_client = blob_service_client.get_blob_client(blob_container_name, blob_name)
            with open(local_file_path, "rb") as local_file:
                blob_client.upload_blob(local_file)

            return True

        except Exception as exc:
            logging.error(f"Error while uploading file to Azure: {str(exc)}")
            return False

    else:
        logging.error("Please enter valid access information to Azure blob storage in .env file")
        return False
