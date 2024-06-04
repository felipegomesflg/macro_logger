import os
from datetime import datetime
from google.cloud import storage

def upload_to_gcp_bucket(logs, bucket=None):
    if bucket is None:
        bucket = os.getenv('GCP_BUCKET')

    if not bucket:
        raise ValueError("Variável de ambiente GCP_BUCKET não está definida.")

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(f'logs_{datetime.now().strftime("%Y%m%d%H%M%S")}.json')

    # Write logs to blob
    blob.upload_from_string(''.join(logs), content_type='application/json')

    print(f'Logs enviados para o bucket da GCP: {blob.public_url}')
