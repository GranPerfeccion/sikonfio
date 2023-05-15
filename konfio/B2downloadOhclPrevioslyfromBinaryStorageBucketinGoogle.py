import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase
cred = credentials.Certificate("/Users/samantabhadra/sikonfio/Konfio/sikonfio.json")
default_app = firebase_admin.initialize_app(cred, {'storageBucket': "sikonfio.appspot.com"})

# Download the file from the Firebase Storage bucket
bucket = storage.bucket()
blob = bucket.blob("ohlc_data.xlsx")
local_path = "/Users/samantabhadra/sikonfio/Konfio/ohlc_data.xlsx"
blob.download_to_filename(local_path)