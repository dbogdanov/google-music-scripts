# google-music-scripts
Scripts for playlist generation using [unofficial Google Music API](https://unofficial-google-music-api.readthedocs.org).

Google Music allows browsing your music collection by genre, but it does not support multi-genre annotations in track metadata that can be typically found after using tagger tools like MusicBrainz Picard.

This script parses multi-genre annotations (separated by ';', ',' or '/' in genre tag field) 
for each track of your Google Music library and generates a playlist for each genre found.


