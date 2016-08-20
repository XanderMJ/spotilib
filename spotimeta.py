import spotipy
import pprint
import spotilib

sp = spotipy.Spotify()

def find_metadata():
	results = sp.search(q=spotilib.song(), limit=50)
	for i, t in enumerate(results['tracks']['items']):
		artist_meta = str(t['artists'])
		temp_artist_meta = artist_meta.split(',')
		track = (t['name']).encode('utf-8')	
		track_uri = (t['uri']).encode('utf-8')
		
		artist, artist_uri = get_artist_uri(n=len(temp_artist_meta), dataset=temp_artist_meta)
		
		if spotilib.artist() in artist and track == spotilib.song():
			return track, track_uri, artist, artist_uri
			

def get_artist_uri(n, dataset):
	meta_data, artists, artist_uri = [],[],[]
	name_index = 6
	index_count = 0 
	
	for i in range(n):
		meta_data.append(dataset[i])
		for j in range(n):
			if index_count == j*name_index:
				artists.append(meta_data[i][13:-1])
			elif index_count == (j)*name_index+2:
				artist_uri.append(meta_data[i][11:-1])
		index_count += 1
	return artists, artist_uri
		
	
def artists(Type):
	if find_metadata() is None:
		print "spotimeta wasn\'t able to get all metadata of current song"
		return spotilib.artist()
	elif Type == 'name':
		return find_metadata()[2]
	elif Type == "uri":
		return find_metadata()[3]
	else:
		print "Error: Invalid Type"
		
def track(Type):
	if find_metadata() is None:
		print "spotimeta wasn\'t able to get all metadata of current song"
		return spotilib.song()
	elif Type == 'name':
		return find_metadata()[0]
	elif Type == "uri":
		return find_metadata()[1]
	else:
		print "Error: Invalid Type"
