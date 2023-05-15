import firebase_admin
from firebase_admin import credentials, storage
import pandas as pd
import io

cred = credentials.Certificate("/Users/samantabhadra/sikonfio/Konfio/sikonfio.json")
default_app = firebase_admin.initialize_app(cred, {'storageBucket': "sikonfio.appspot.com"})

bucket = storage.bucket()
blob = bucket.blob("ohlc2.xlsx")
df = pd.DataFrame(data={'date': [1, 2], 'price': [3, 4]})

output = io.BytesIO()
writer = pd.ExcelWriter(output, engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1')

workbook = writer.book  # Get the workbook object
workbook.save("ohlc2.xlsx")  # Save the workbook
writer.close()

xlsx_data = output.getvalue()
blob.upload_from_string(xlsx_data)