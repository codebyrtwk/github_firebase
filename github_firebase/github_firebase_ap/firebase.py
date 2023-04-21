import firebase_admin
from firebase_admin import credentials, firestore
import os


cred = credentials.Certificate('github_firebase_ap\githubfirebase-44f2c-firebase-adminsdk-ixhhe-63b826d461.json')
print(cred)
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db)