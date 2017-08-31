import discord
import asyncio
import re
import random

client = discord.Client()
accepted_messages = ["Welcome {}, giveme a second to flip some bits and you should be able to use our channels.")]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def get_member_role(serv):
    member_role = discord.utils.get(serv.roles, name="cwru")
    return(member_role)

@client.event
async def on_message(message):
    if message.author.name.endswith("bot"):
        return None
    elif message.channel.name == "introductions":
        if get_member_role(message.server) in message.author.roles:
            return None
        elif name_formatted(message.author.nick):
            await client.send_message(message.channel, get_accepted_message.format(message.author.name))
            role = await get_member_role(message.server)
            await client.add_roles(message.author, role)
        else:
            await client.send_message(message.channel, "Hi {}, please edit your nickname to our server's standard [real name]([in-game name]) and post your introduction again.".format(message.author.name))
    elif message.channel.name == "exec":
        if message.content.startswith("!text"):
            await client.send_message(message.channel, "test echo")
        elif message.content.startswith("!list_welcome"):
            await client.send_message(message.channel, "here are my current welcome messages:")
            for x in accepted_messages:
                await client.send_message(message.channel, x)
        elif message.content.startswith("!add_welcome"):
            if "{}" in message.content:
                add_accepted_message(message.content[len("!add_welcome"):])
            elif:
                await client.send_message(message.channel, "welcome messages must have \"{}\" in place for the user's name")

def get_accepted_message():
    return(random.choice(accepted_messages))

def add_accepted_message(msg):
    accepted_messages.append(msg)

def name_formatted(name):
    print(name)
    if name == None:
        return

    pattern = re.compile("^.*\(.*\)$")
    if pattern.match(name):
        return(True)
    else:
        return(False)
    
#@client.event
#async def on_message(message):
#    print(new_member_role)
#    if message.content.startswith('!text'):
#        counter=0
#        tmp = await client.send_message(message.channel, 'Calculating messages...')
#        async for log in client.logs_from(message.channel, limit=100):
#            if log.author == message.author:
#                counter += 1
#        
#        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#    elif message.content.startswith('!sleep'):
#        await asyncio.sleep(5)
#        await client.send_message(message.channel, 'Done sleeping')

client.run("MzA2ODQyNzE5MDY4NzQ5ODMy.DEshiw.3lSwGvLYT4ucggcm72twWnIlVbI")
