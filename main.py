import sendtext
from random import shuffle

#user details for automatically logging into meteor webtext
username=""
password=""
yournumber=""
recipientsnumber="" #don't actually need this one for now

#the list of people taking part in the secret santa,
#their numbers, and who they get as their secret santa (leave recipient blank)
people = [
            {
            "name":"jesus",
            "phone": "12345678",
            "reciever":""
            },
            {
            "name":"mary",
            "phone": "12345678",
            "reciever":""
            },
            {
            "name":"joseph",
            "phone": "12345678",
            "reciever":""
            }
            #add more people if needed
        ]

#build the list of recipients from the orginal list of names
recipientlist=[]
for i in xrange(len(people)):
    recipientlist.append(people[i]["name"])

#randomize the list
shuffle(recipientlist)

#check that people don't recieve themselves as their secret santa
keepgoing=True
while keepgoing==True:
    for i in xrange(len(people)):
        if people[i]["name"] == recipientlist[i]:
            print("...Someone matched with themselves, reshuffling...")
            keepgoing=True
            shuffle(recipientlist)
            break
        else:
            keepgoing=False

# updating people list with matched recipients
for i in xrange(len(people)):
    people[i]["reciever"] = recipientlist[i]

#loop through people and send the actual text
for peeps in people:
    #print the messages:
    #message="(automated text..) Hi " + peeps["name"] + " you're secret santa is " + peeps["reciever"]
    print(message)
    sendtext.meteor(username, password,yournumber, peeps["phone"], message)
