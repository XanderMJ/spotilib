######Hello there! Just a quick headsup, I'm pretty new to python and my code may not be the best. So feel free to give some suggestions or tips!

# spotilib.py
I'm working on a python library to access metadata from Spotify on windows, keep in mind this is still work in progress. I wanted to make this libraby so i could ignore speciffic songs on Spotify and prevent them from playing on my PC. At this moment I completed a python script which runs in the background and allows blocking songs from playing (with the use of hotkeys). If people are intrested I will upload the script as well.

###What does it offer?
This library gives you easy acces to the current playing song in Spotify. It returns the song title and artist name within a single line of code. At this moment the artist information is limited to one artist name, this is due to the way Spotify represents the song information in the windowtitle (and ofcourse the lack of a Spotify API for windows). However, I'm already working on a little workaround for this problem! *(see: spotimeta.py)*

###How does it work?
*spotilib.getwindow(Title="SpotifyMainWindow")* returns the id from the Spotify window

*spotilib.song_info()* returns the windowtitle of the Spotify window as: Artist - SongTitle

*spotilib.artist()* returns the Artist name

*spotilib.song()* retuns the SongTitle


######I added media hotkeys for the ease of use and to make it a bit more complete. However, these can be achieved without the use of spotilib library.


*spotilib.next()* skips to the next song

*spotilib.previous()* returns to the beginning of the song, or skips to previous song (depending on how long the song is playing)

*spotilib.pauze()* pauzes the playing media, if the media is already paused it wil resume playing

*spotilib.mute()* mutes the audio (from all media, not only Spotify)


######The library contains some options to create folders en .txt files. I have used those to store the information from songs I dont want to get played by Spotify.





#spotimeta.py

Spotimeta is a library that allows you to acces more of the metadata from the currently playing song. This library uses the *spotipy* library to search for missing data. At this moment the library is still very limmited.

###What does it offer?
The *spotilib* library can only give you the name of one artist, even if the song is a collaboration between mulitple artists. The *spotimeta* library tries to find the missing artists. As this is very early stage,it does not always succed in finding the wright information, in that case it returns an error and falls back to the *spotilib* results.

At this moment it is capable of returning the song info as text or as 'uri'. The 'uri' can be usefull if you are using *spotipy*.
###How does it work?
*spotimeta.artists(Type)* this returns a list op all the collaborating artist. *Type='name'* returns the name(s) of the artist(s). *Type='uri'* returns the spotify URI link(s).

*spotimeta.track(Type)* this returns the current playing track. *Type='name'* returns the name of the track. *Type='uri'* returns the spotify URI link.


##Known Issues:
*spotimeta.artists(Type)* won't succes in returning a value if an artist name (or a part of it) also occurs in the track title. In this case it returns the value "None". 
