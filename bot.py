import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(member):
    new_member_role = await get_new_member_role(member.server)
    print(new_member_role)
    client.add_roles(member, [new_member_role]); 
    print('joined')

@client.event
async def get_new_member_role(serv):
    roles = list(serv.roles)
    new_member_role = [x for x in roles if x.name == "new member"][0]
    return(new_member_role)

@client.event
async def on_message(message):
    print(new_member_role)
    if message.content.startswith('!text'):
        counter=0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run("MzA2ODQyNzE5MDY4NzQ5ODMy.DEshiw.3lSwGvLYT4ucggcm72twWnIlVbI")
