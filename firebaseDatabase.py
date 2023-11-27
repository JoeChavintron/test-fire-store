import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('testfirebase-7f38d-98dc71469ecf.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection("test01")
docs = doc_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})