from typing import Dict, List, Optional

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(
    cred,
    {
        "projectId": "bodybuilding-notification-app",
    },
)

db = firestore.client()


def does_resource_exist(collection: str, resource_id: str):
    doc = db.collection(collection).document(resource_id).get()
    return doc.exists


def get_all(collection: str) -> List:
    docs = db.collection(collection).list_documents()
    return list(docs)


def get(collection: str, resource_id: str) -> Optional[Dict]:
    try:
        doc = db.collection(collection).document(resource_id).get()
        if doc.exists:
            return doc.to_dict()
        return None
    except Exception as e:
        return None


def add(collection: str, resource: Dict) -> bool:
    try:
        db.collection(collection).document(resource["id"]).set(resource)
        return True
    except Exception as e:
        return False


def delete(collection: str, resource_id: str) -> None:
    db.collection(collection).document(resource_id).delete()
