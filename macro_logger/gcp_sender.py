from google.cloud import storage

class GCPSender:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def send_to_gcp(self, local_file_path, gcp_file_path):
        storage_client = storage.Client()
        bucket = storage_client.bucket(self.bucket_name)
        blob = bucket.blob(gcp_file_path)
        blob.upload_from_filename(local_file_path)
