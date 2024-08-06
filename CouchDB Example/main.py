import config
import requests
import json
from time import time

class Sofa:
    def __init__(self):
        # Config Based Params
        self.username: str = config.username
        self.password: str = config.password
        self.url: str = config.url
        self.url = self.url.replace("[username]", f"{self.username}")
        self.url = self.url.replace("[password]", f"{self.password}")
        # Empty Params
        self.q_url: str = "None"
        self.db_name: str = "None"
        
    def is_up(self):
        # Assign Variables
        self.q_url = f"{self.url}/_up"
        # Query
        with requests.get(self.q_url) as resp:
            self.status = resp.status_code
        # Finalization
        if self.status == 200:
            return 1
        else:
            return 0


    # Database Funcs
    def create_db(self, db_name: str):
        # Assign Variables
        self.db_name = db_name
        self.q_url = f"{self.url}/{self.db_name}"
        # Query
        with requests.put(self.q_url) as resp:
            self.status = resp.status_code
        # Finalization
        if self.status == 201:
            return 1
        else:
            return 0

    def delete_db(self, db_name: str):
        # Assign Variables
        self.db_name = db_name
        self.q_url = f"{self.url}/{self.db_name}"
        # Query
        with requests.delete(self.q_url) as resp:
            self.status = resp.status_code
        # Finalization
        if self.status == 200:
            return 1
        else:
            return 0

    # Document Funcs
    def get_all_docs(self, db_name: str):
        # Assign Variables
        self.db_name = db_name
        self.q_url = f"{self.url}/{self.db_name}/_all_docs"
        # Query
        with requests.get(self.q_url) as resp:
            self.data = resp.json()
        # Finalization
        return self.data

    def insert_doc(self, db_name: str, doc_data: dict):
        # Assign Variables
        self.db_name = db_name
        self.doc_id = str(int(time()))
        self.doc_data = json.dumps(doc_data) # Convert to JSON
        self.q_url = f"{self.url}/{self.db_name}/{self.doc_id}"
        # Query
        with requests.put(self.q_url, data=self.doc_data) as resp:
            self.status = resp.status_code
        # Finalization
        if self.status == 201 or self.status == 202:
            return 1
        else:
            return 0

    def read_doc(self, db_name: str, doc_id: str):
        # Assign Variables
        self.db_name = db_name
        self.doc_id = doc_id
        self.q_url = f"{self.url}/{self.db_name}/{self.doc_id}"
        # Query
        with requests.get(self.q_url) as resp:
            self.status = resp.status_code
            self.data = resp.json()
        # Finalization
        if self.status == 200:
            return 1, self.data
        else:
            return 0, {}

    def truncate_db(self):
        pass


# Testing Script
if __name__ == "__main__":
    # Create Object
    sofa = Sofa()
    # Test Connectivity
    status = sofa.is_up()
    # Test Query All Docs
    if status == True:
        print("Server Online")
        q_status, q_data = sofa.read_doc("pidata", "1722907282")
        if q_status == True:
            print("Query Success")
            print(q_data)
        else:
            print("Query Failed")
    else:
        print("Server Offline")
