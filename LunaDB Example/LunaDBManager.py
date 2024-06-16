from LunaDB import LunaDB

db = LunaDB('db.json')
collection = db.table("Blockchain", id_field="id")

collection.insert({"id": 1,"city": "Semarang"})
collection.insert({"id": 2,"city": "Jakarta"})

print(db)
