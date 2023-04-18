from scratchclient import ScratchSession
import requests
import json

user = OS.getenv("USER")
password = OS.getenv("PASSWORD")
session = ScratchSession(user, password)
connection = session.create_cloud_connection(837287681)

@connection.on("set")
def on_set(variable):
  parsed = "minecraft"
  request = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&exintro&titles=" + parsed + "&redirects=").json()
  
