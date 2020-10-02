from itertools import islice
from fbchat import Client
from fbchat.models import *
import os
import time
import sys

email = os.environ["email"]
fbpass = os.environ["fbpassord"]


client = Client(email, fbpass)

print("Own id: {}", format(client.uid))

threads = client.fetchThreadList()
try:

    navn = input("Velg facebookvenn: ")
    user = client.searchForUsers(navn)[0]

    print("user ID: {}".format(user.uid))
    print("user's name: {}".format(user.name))
    print("Is user client's friend: {}".format(user.is_friend))
    print(type(user.is_friend))

    fil = "ballefrans.txt"

    with open(fil, "r") as file:
        tekst = file.read()
        newfile = tekst.split("\n")

    moviescript = []

    for i in range(len(newfile)):
        if newfile[i] == " " or newfile[i] == "":
            continue
        else:
            moviescript.append(newfile[i])

    for i in range(25):
        client.send(
            Message(text=moviescript[i]), thread_id=user.uid, thread_type=ThreadType.USER)
        print("Message sent: ", moviescript[i])
        time.sleep(3)
    
    print("Thank you for using ShrekBot")
    time.sleep(10)
    client.logout()
    sys.exit()

except:
    sys.exit()
