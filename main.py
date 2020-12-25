import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

# Start by defining the discord client
client = discord.Client()

# lists of words for special responses

saltyb_words = ["SaltyBot", "saltybot", "Salty"]

t_words = ["help", "o-link", "kinect", "VR", "hand tracking", "VD", "Virtual Desktop", "oculus"]

greet_words = ["morning", "hey", "Hey", "hi", "Hi", "Hello", "hello", "Morning", "Afternoon" "afternoon", "Evening",
               "evening", "good morning", "Good morning", "Good afteroon", "good afternoon", "good evening",
               "Good evening", "good day", "Good day"]

cringe_words = ["furry", "furries", "uwu", "UWU", "uWu", "UwU", ":3", "vrc", "vrchat", "VR-Chat", "anime"]

salty_words = ["salt", "pleb", "dumb bot", "noob", "dumb", "egirl", "thot", "lame", "sucks", "crap", "salty",
               "really?!?"]

# List of responses to special words
starter_saltyb = [
    "Ugh, I am a simple bot... Please don't say my name with out giving me a purpose to be alerted xP",
    "Why are you using my name? Do you need something form me?!?",
    "Is this a test or something?",
    "... yet another human making me respond for no reason.",
    "...... was that meant for me?",
    "There is a command list you know..."
]

starter_tech_talk = [
    "If you are needing any help with the Quest, Quest 2, Virtual Desktop, Kinect or any other PCVR gaming questions; "
    "I think someone is needing help? Please check out the #troubleshooting-help channel.",
    "Do you need some help with something VR related? Check the #troubleshooting-help channel.",
    "If you have questions or need help, check out the different channels or DM @Thrice369. "
]

starter_greeting = [
    "Hey there",
    "Good morrow to you as well!",
    "Hi",
    "Afternoon for me!",
    "Hello"
]

starter_cringe = [
    "Oh no... there be furries here...",
    "'sniff, sniff,' I smell a weeb...",
    "Is that an Eboy I hear?",
    "Thots, Egirls, Eboys, Lolis, & Furries... We are doomed X("
]

starter_smack_talk = [
    "Uhoh, salt incoming xP",
    "Someone is getting salty!",
    "Did someone order a load of salt to be delivered right here ^ ",
    "Man, I though I was salty...",
    "The salt is thick with this one.",
    "Do I taste salt in the air?"
]


# helper function to return quote from api
def get_quote():
    response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")
    json_data = json.loads(response.text)
    quote = json_data[0] + "-Ron Swanson"
    return quote


def update_satlyb(saltyb_message):
    if "saltyb" in db.keys():
        saltyb = db["saltyb"]
        saltyb.appen(saltyb_message)
        db["saltyb"] = saltyb
    else:
        db["saltyb"] = [saltyb_message]


def delete_saltyb(index):
    saltyb = db["saltyb"]
    if len(saltyb).index:
        del saltyb[index]
    db["saltyb"] = saltyb


def update_tech_talk(tech_talk_message):
    if "tech_talk" in db.keys():
        tech_talk = db["tech_talk"]
        tech_talk.append(tech_talk_message)
        db["tech_talk"] = tech_talk
    else:
        db["tech_talk"] = [tech_talk_message]


def delete_tech_talk(index):
    tech_talk = db["tech_talk"]
    if len(tech_talk) > index:
        del tech_talk[index]
    db["tech_talk"] = tech_talk


def update_greeting(greeting_message):
    if "greeting" in db.keys():
        greeting = db["greeting"]
        greeting.append(greeting_message)
        db["greeting"] = greeting
    else:
        db["greeting"] = [greeting_message]


def delete_greeting(index):
    greeting = db["greeting"]
    if len(greeting).index:
        del greeting[index]
    db["greeting"] = greeting


# Function to update cringe response db list with an append
def update_cringe(cringe_message):
    if "cringe" in db.keys():
        cringe = db["cringe"]
        cringe.append(cringe_message)
        db["cringe"] = cringe
    else:
        db["cringe"] = [cringe_message]


# Function to delete cringe responses create by users
def delete_cringe(index):
    cringe = db["cringe"]
    if len(cringe) > index:
        del cringe[index]
    db["cringe"] = cringe


def update_smack_talk(smack_talk_message):
    if "smack_talk" in db.keys():
        smack_talk = db["smack_talk"]
        smack_talk.append(smack_talk_message)
        db["smack_talk"] = smack_talk
    else:
        db["smack_talk"] = [smack_talk_message]


def delete_smack_talk(index):
    smack_talk = db["smack_talk"]
    if len(smack_talk) > index:
        del smack_talk[index]
    db["smack_talk"] = smack_talk


# standard practice for discord bot events
# (@client.event
# async def)

@client.event
async def on_ready():  # When bot joins server
    print('We have logged in as {0.user}'.format(client))
    print("Username: ", end='')
    print(client.user.name)
    print("Userid: ", end='')
    print(client.user.id)


@client.event
async def on_message(message):  # For reading messages
    if message.author == client.user:
        return  # returning if bot is author

    msg = message.content

    if message.content.startswith('Hey SaltyBot'):  # Response to hello
        await message.channel.send('Salty bot reporting for duty!!!')

    if message.content.startswith('test'):
        await message.channel.send('... is this a test?')

    if message.content.startswith('Hey Salty, call stoutish a dork... xP'):  # Response to hello
        await message.channel.send(
            'Well, not wanting to be mean... I simply have to tell the truth. @stoutishsugar is a HUGE Star Citizen dork. There, I said it.')

    if message.content.startswith('Hey Salty, are you up?'):  # Response to hello
        await message.channel.send('Yes... Do you need something?')

    if message.content.startswith('Salty, who is stoutishsugar?'):  # Response to hello
        await message.channel.send(
            'A man.. neh, a weeb. dedicated to the fanboying over StarCitizen until the day he dies. But a really cool dude as well.')

    if message.content.startswith('Hey Salty, what is your purpose?'):  # Response to hello
        await message.channel.send(
            'Ugh. How cliche for you to ask that. I have no purpose besides fulfilling the selfish wants and needs of '
            'Thrice and his inflated ego. Well, that nad memes. I wish to be the greatest bot memer one day.')

    if message.content.startswith('I need a SALTY meme'):  # Response to hello
        await message.channel.send('https://images7.memedroid.com/images/UPLOADED367/5fe3875e6f017.jpeg')

    if message.content.startswith('Give me a daily quote.'):  # Response to hello
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('Give me another quote.'):  # Response to hello
        quote = get_quote()
        await message.channel.send("Okay, pulling up another now.")
        await message.channel.send(quote)

    if message.content.startswith('SaltCheck, testing?'):  # Response to hello
        await message.channel.send(
            "'clears throat' Salty here. Testing 1...2....3.... Scanning' 'database.... Retrieving core files.... c:/usr/thrice/Pictures/private/naughty_furries")

    if any(word in msg for word in saltyb_words):
        await message.channel.send(random.choice(starter_saltyb))

    if any(word in msg for word in salty_words):
        await message.channel.send(random.choice(starter_smack_talk))

    if any(word in msg for word in t_words):
        await message.channel.send(random.choice(starter_tech_talk))

    if any(word in msg for word in cringe_words):
        await message.channel.send(random.choice(starter_cringe))

    if any(word in msg for word in greet_words):
        await message.channel.send(random.choice(starter_greeting))

    if msg.startswith("$newcringe"):
        cringe_message = msg.split("$newcringe ", 1)[1]
        update_cringe(cringe_message)
        await message.channel.send("New cringy response added.")
        cringe = db["cringe"]
        await message.channel.send(cringe)

    # Do not want users in discord to be able to delete others users bot responses. Create command!
    # if msg.startswith("$delcringe"):
    # cringe = []
    # if "cringe" in db.keys():
    # index = int(msg.split("$delcringe", 1)[1])
    # delete_cringe(index)
    # cringe = db["cringe"]
    # await message.channel.send(cringe)

    if msg.startswith("#newsatlyb"):
        saltyb_message = msg.split("newsaltyb ", 1)[1]
        update_satlyb(saltyb_message)
        await message.channel.send("New SaltyBot response added.")
        saltyb = db["saltyb"]
        await message.channel.send(saltyb)

    if msg.startswith("$newsmack_talk"):
        smack_talk_message = msg.split("$newsmack_talk ", 1)[1]
        update_smack_talk(smack_talk_message)
        await message.channel.send("New salty response added.")
        smack_talk = db["smack_talk"]
        await message.channel.send(smack_talk)

    if msg.startswith("$newtech_talk"):
        tech_talk_message = msg.split("$newtech_talk ", 1)[1]
        update_tech_talk(tech_talk_message)
        await message.channel.send("New tech response added.")
        tech_talk = db["tech_talk"]
        await message.channel.send(tech_talk)

    if msg.startswith("$newgreeting"):
        greeting_message = msg.split("$newgreeting ", 1)[1]
        update_greeting(greeting_message)
        await message.channel.send("New greeting response added.")
        greeting = db["greeting"]

    # list function seems to be conflicting with othher messages. Maybe need alternative function that calls
    # from various functions or as a list. Need to simplify script to one style of command to fix.
    if message.startswith("$listcringe"):
        cringe = []
        if "cringe" in db.keys():
            cringe = db["cringe"]
        await message.channel.send(cringe)

    if msg.startswith("$listsaltyb"):
        saltyb = []
        if "saltyb" in db.keys():
            saltyb = db["saltyb"]
        await message.channel.send(saltyb)

    if msg.startswith("$listsmack_talk"):
        smack_talk = []
        if "smack_talk" in db.keys():
            smack_talk = db["smack_talk"]
        await message.channel.send(smack_talk)

    if msg.startswith("$listgreeting"):
        greeting = []
        if "greeting" in db.keys():
            greeting = db["greeting"]
        await message.channel.send(greeting)

    if msg.startswith("$listtech_talk"):
        tech_talk = []
        if "tech_talk" in db.keys():
            tech_talk = db("tech_talk")
        await message.channel.send(tech_talk)

keep_alive()
client.run(os.getenv('TOKEN'))  # relp.it based encryption w/.env