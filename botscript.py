import requests, json, re, discord, asyncio
from websocket import create_connection

api_url = 'https://discordapp.com/api'
client = discord.Client()

def name_is_formatted(name, pattern):
	print(name)
	if pattern.match(name):
		print(True)
		return(True)
	else:
		print(False)
		return(False)

def get_unformatted_users(name_pattern, guild_id, bot_token):
	#set request params
	url = api_url + '/guilds/' + guild_id + '/members'
	auth_string = 'Bot %s' % bot_token
	headers = {'Authorization' : auth_string}
	
	#make request to get list of all users
	r = requests.get(url, headers = headers)
	print(r.content)
	member_list = json.loads(r.content.decode('utf-8'))
	
	#add unformatted users to list
	unformatted_users = []
	for x in member_list:
		nickname = x['nick']
		if not name_is_formatted(nickname, name_pattern):
			unformatted_users.append(x)

	return(unformatted_users)

@client.event
async def on_ready():
	print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

def post_message_to_channel(message, channel_id, bot_token):
	client.send_message(channel_id, message)

def get_gateway():
	url = api_url + '/gateway'
	r = requests.get(url)
	gateway_url = json.loads(r.content.decode('utf-8'))['url']
	print(gateway_url)
	return(gateway_url)	

def connect_to_gateway(url):
	#websocket magic
	ws = create_connection(url)
	ws.send("Hello, World")
	res = ws.recv()
	print(res)
	ws.close()

	#create notification message
#	msg = ''
#	for x in users:
#		nickname = x['nick']
#		msg = msg + '<!@' + nickanem + '>' 
client_id = '306842719068749832'
client_secret = 'OKde2yforc75GEg0TOxvtnyMvNBKHqO4'

pattern		= re.compile("^.*\(.*\)$")
guild_id	= '260589757396942849'
channel_id	= '260589757396942849'
bot_token = 'MzA2ODQyNzE5MDY4NzQ5ODMy.C-Jwwg.gCOVKnFnOe9A85I2cUY9yPHOhDc'

users = get_unformatted_users(pattern, guild_id, bot_token)
#gateway_url = get_gateway()
#connect_to_gateway(gateway_url)
post_message_to_channel("testing", channel_id, bot_token)
