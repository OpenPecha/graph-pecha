from terminusdb_client import WOQLClient

team = "openpecha"
db = "Texts_as_chunks"

client = WOQLClient("https://cloud.terminusdb.com/openpecha/")
client.connect(db=db, team=team, use_token=True)

print(client)
