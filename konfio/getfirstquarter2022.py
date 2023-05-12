import firebase_admin
import pandas as pd
from firebase_admin import credentials
from firebase_admin import db
from firebase import firebase

firebase = firebase.FirebaseApplication("https://sikonfio-default-rtdb.firebaseio.com/",None)

# Initialize Firebase app
cred = credentials.Certificate("/Users/samantabhadra/sikonfio/Konfio/sikonfio.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sikonfio-default-rtdb.firebaseio.com/'
})

firstquarter = db.reference('firstquarter2022/-NVBSgYddYHhS_Q8QGVc')

# Retrieve the collection data
data = firstquarter.get()

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'],format='%d%b%Y')

# Set 'date' column as the index
df.set_index('date', inplace=True)


# # Group by date with the specified window size
grouped = df.groupby(pd.Grouper(freq='5D'))
# # Iterate over each group
cont=0
for group_name, group_data in grouped:
     cont += 1
     print(f"Group Name: Week {str(cont)} {group_name}")
     print(f"Group Data:\n{group_data}")
     print()
     # firebase.post('/firstquarter2022by5days', group_data.reset_index().to_dict('list'))