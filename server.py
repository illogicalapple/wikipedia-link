from scratchclient import ScratchSession
import requests

user = OS.getenv("USER")
password = OS.getenv("PASSWORD")
session = ScratchSession(user, password)
connection = session.create_cloud_connection(837287681)

@connection.on("set")
def on_set(variable):
  print(variable.name, variable.value, "aaaaaa")
