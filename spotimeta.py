import spotipy
import pprint
import spotilib

sp = spotipy.Spotify()

def find_data():
	results = sp.search(q=spotilib.song(), limit=50)
	for i, t in enumerate(results['tracks']['items']):
		temp_artist = str(t['artists'])
		temp_track =(t['name']).encode('utf-8')
		if spotilib.artist() in temp_artist and temp_track == spotilib.song():
			data = temp_artist
			return data
			
def count(item='name' ):
	stng = find_data()
	temp = stng.split(',')
	length = len(temp)
	count = 0 
	for i in range(length):
		if item in temp[i]:
			count += 1
	return count, temp
	
def mulitple():
	n = count()[0]
	temp = count()[1]
	meta_data = []
	artists = []
	number_of_items = 6
	index_count = 0 
	for i in range(n*number_of_items):
		meta_data.append(temp[i])
		for j in range(n):
			if index_count == j*number_of_items:
				artists.append(meta_data[i][13:-1])
		index_count += 1
	return artists	
	
def artists():
	if find_data() is None:
		print "spotimeta wasn\'t able to get all metadata of current song"
		return spotilib.artist()
	else:
		return mulitple()