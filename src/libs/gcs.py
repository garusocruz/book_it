import json
import os
from google.cloud.storage import Client
from google.oauth2 import service_account
from google.cloud.storage import Client
from google.cloud.storage.bucket import Bucket
import base64
from decouple import config
GS_CREDENTIALS = base64.b64decode(config("GS_CREDENTIALS")).decode("utf-8")


class GCS(Client):
    def __init__(self, bucket_name: str):
        GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GS_CREDENTIALS
        GOOGLE_APPLICATION_CREDENTIALS = json.loads(GOOGLE_APPLICATION_CREDENTIALS)
        self.credentials = service_account.Credentials.from_service_account_info(GOOGLE_APPLICATION_CREDENTIALS)
        self.client = Client(credentials=self.credentials)


    def upload_blob(self, source_file_name:str):
        generation_match_precondition = 0
        blob = self.client.bucket("hawkers-storage").blob(source_file_name)
        blob.upload_from_filename("destination.png", if_generation_match=generation_match_precondition)

        return blob.public_url