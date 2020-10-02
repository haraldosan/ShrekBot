from itertools import islice
from fbchat import Client
from fbchat.models import *
import os
import time

email = os.environ["email"]
fbpass = os.environ["fbpassord"]


client = Client(email, fbpass)

print("Own id: {}", format(client.uid))

threads = client.fetchThreadList()


navn = input("Velg facebookvenn: ")
user = client.searchForUsers(navn)[0]

print("user ID: {}".format(user.uid))
print("user's name: {}".format(user.name))
print("user's photo: {}".format(user.photo))
print("Is user client's friend: {}".format(user.is_friend))


fil = "ballefrans.txt"


with open(fil, "r") as file:
    tekst = file.read()
    newfile = tekst.split("\n")

for i in range(10):
    client.send(
        Message(text=str(newfile[i])), thread_id=user.uid, thread_type=ThreadType.USER)
    time.sleep(3)


client.logout()
