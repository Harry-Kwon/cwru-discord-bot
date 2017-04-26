import requests, json

guild_id = "260589757396942849"
url = 'https://discordapp.com/api/guilds/' + guild_id + '/members'

bot_token = 'MzA2ODQyNzE5MDY4NzQ5ODMy.C-Jwwg.gCOVKnFnOe9A85I2cUY9yPHOhDc'
auth_string = 'Bot %s' % bot_token

print(auth_string)

headers = {'Authorization' : auth_string}

r = requests.get(url, headers = headers)
member_list = json.loads(r.content.decode('utf-8'))
print(member_list[0])
