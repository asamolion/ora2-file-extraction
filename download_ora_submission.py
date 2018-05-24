import boto3


BUCKET_NAME = "<INSERT BUCKET NAME>"

AWS_ACCESS_KEY_ID = "<INSERT ACCESS KEY ID>"

AWS_ACCESS_SECRET_KEY = "<INSERT SECRET ACCESS KEY>"

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET_NAME)

file_name = '<INSERT FILE NAME>'
file_key =  '<INSERT FILE KEY>'


def download_ora_submission(file_key, file_name):
    """
    Function to download file given by file key

    arguments:
    file_key (string): string representation of file path in AWS S3 bucket
    file_name (string): downloaded file will be saved with this name
    """
    file_path = 'submissions_attachments/{}'.format(file_key)
    return bucket.download_file(file_path, file_name)

download_ora_submission(file_key, file_name)

