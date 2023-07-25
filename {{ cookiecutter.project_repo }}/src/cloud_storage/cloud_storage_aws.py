import logging
import os
import boto3


def write_file_to_aws_s3(local_file_path):
    """
        Upload file to AWS S3 Bucket. Use .env file to get access information.

        Args:
            - local_file_path to upload

        Returns:
            True or False depending on the success of the upload
    """
    # AWS s3 access information
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    bucket_name = os.getenv('AWS_BUCKET_NAME')

    if access_key is not None and secret_key is not None and bucket_name is not None and access_key != "" and secret_key != "" and bucket_name != "":

        try:
            file_name = os.path.basename(local_file_path)

            # Declare s3 resource and upload file
            s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
            s3.Object(bucket_name, file_name).delete()
            s3.Object(bucket_name, file_name).upload_file(local_file_path)

            return True

        except Exception as exc:
            logging.error(f"Error while uploading file to AWS S3: {str(exc)}")
            return False

    else:
        logging.error("Please enter valid access information to AWS S3 in .env file")
        return False
