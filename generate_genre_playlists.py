import sys
import getpass
from gmusicapi import Mobileclient


email = raw_input("User (gmail): ")
pswd = getpass.getpass('Password:')
api = Mobileclient()
logged_in = api.login(email, pswd, Mobileclient.FROM_MAC_ADDRESS)

if not logged_in:
	print "Authentification error"
	sys.exit()

songs = api.get_all_songs()

for song in songs:
	song['genre'] = song['genre'].replace(" ", "").lower()
	if ';' in song['genre']:
		song['genre'] = song['genre'].split(';')
	elif ',' in song['genre']:
		song['genre'] = song['genre'].split(',')
	elif '/' in song['genre']:
		song['genre'] = song['genre'].split('/')
	else:
		song['genre'] = [song['genre']]

genres_map = {}
for s in songs:
	for g in s['genre']:
		genres_map.setdefault(g, [])
		genres_map[g].append(s['id'])

good_genres = []
print "Available genres:"
for g in genres_map.keys():
	if len(g) == 0: 
		continue # empty genre tag

	if len(genres_map[g]) >= 20:
		print g + '\t' + str(len(genres_map[g])) + ' tracks --> generating playlist'
		good_genres.append(g)

	else:
		print g + '\t' + str(len(genres_map[g])) + ' tracks --> too few tracks'

print

# remove all existing auto-playlists first
playlists = api.get_all_playlists()
for p in playlists:
	if p['name'].startswith("genre auto-playlist"):
		print "Removing playlist " + p['name']
		api.delete_playlist(p['id'])

for genre in good_genres:
	playlist = genres_map[genre]
	playlist_name = "genre auto-playlist - " + genre
	print "Creating playlist " + playlist_name

	pid = api.create_playlist(playlist_name, description="Test " + genre + " playlist created automatically with a script", public=False)
	api.add_songs_to_playlist(pid, playlist)
