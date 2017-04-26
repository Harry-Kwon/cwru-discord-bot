import requests, json, re

def name_is_formatted(name, pattern):
	print(name)
	if pattern.match(name):
		print(True)
		return(True)
	else:
		print(False)
		return(False)

def get_unformatted_users(guild_id, bot_token, name_pattern):
	#set request params
	url = 'https://discordapp.com/api/guilds/' + guild_id + '/members'
	auth_string = 'Bot %s' % bot_token
	headers = {'Authorization' : auth_string}
	#make request to get list of all users
	r = requests.get(url, headers = headers)
	member_list = json.loads(r.content.decode('utf-8'))
	#add unformatted users to list
	unformatted_users = []
	for x in member_list:
		nickname = x['nick']
		if not name_is_formatted(nickname, name_pattern):
			unformatted_users.append(x)

	return(unformatted_users)

pattern = re.compile("^.*\(.*\)$")
guild_id = "260589757396942849"
bot_token = 'MzA2ODQyNzE5MDY4NzQ5ODMy.C-Jwwg.gCOVKnFnOe9A85I2cUY9yPHOhDc'

print( get_unformatted_users(guild_id, bot_token, pattern))
