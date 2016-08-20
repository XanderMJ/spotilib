# spotilib.py
I'm working on a python library to access metadata from Spotify on windows, keep in mind this is still work in progress. I wanted to make this libraby so i could ignore speciffic songs on Spotify and prevent them from playing on my PC. At this moment I completed a python script which runs in the background and allows blocking songs from playing (with the use of hotkeys). If people are intrested I will upload the script as well.

###What does it offer?
This library gives you easy acces to the current playing song in Spotify. It returns the song title and artist name within a single line of code. At this moment the artist information is limited to one artist name, this is due to the way Spotify represents the song information in the windowtitle (and ofcourse the lack of a Spotify API for windows). However, I'm already working on a little workaround for this problem!

###How does it work?
*spotilib.getwindow(Title="SpotifyMainWindow")* returns the id from the Spotify window

*spotilib.song_info()* returns the windowtitle of the Spotify window as: Artist - SongTitle

*spotilib.artist()* returns the Artist name

*spotilib.song()* retuns the SongTitle


######I added media hotkeys for the ease of use and to make it a bit more complete. However, these can be achieved without the use of spotilib library.


*spotilib.next()* skips to the next song

*spotilib.previous()* returns to the beginning of the song, or skips to previous song (depending on how long the song is playing)

*spotilib.pauze()* pauzes the playing media, if the media is already pauzed it wil resume playing

*spotilib.mute()* mutes the audio (from all media, not only Spotify)


######The library contains some options to create folders en .txt files. I have used those to store the information from songs I dont want to get played by Spotify.

