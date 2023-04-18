from scratchclient import ScratchSession
import requests

user = OS.getenv("USER")
password = OS.getenv("PASSWORD")
session = ScratchSession(user, password)
connection = session.create_cloud_connection(837287681)
cipher = "❓ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]\{}|;':\",./<>`~? "

def decode(encoded):
  result = ""
  for part in [line[i:i+2] for i in range(0, len(line), 2)]:
    result += cipher[int(part)]
  return result

def encode(text):
  result = ""
  for letter in text:
    encoded = cipher.find(letter)
    if encoded < 0:
      encoded = "00"
    elif encoded < 10:
      encoded = "0" + str(encoded)
    else:
      encoded = str(encoded)
    result += encoded
  return result

@connection.on("set")
def on_set(variable):
  request = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&exintro&titles=" + decode(str(variable.value)) + "&redirects=").json()
  page = list(request["pages"])[0]
  title = page["title"]
  text = page["extract"]
