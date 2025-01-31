# delete-crap-scrobbles
Small Python utility to filter and delete scrobbles from Last.fm

Requires premium account to fetch all scrobbles list. If you want it free, you can remake fetching with scrapping.

Put your token and username in the corresponding fields in `delete_crap_scrobbles.py`

Last FM does not provide API endpoint to delete scrobbles, therefore it is done by sending same form as webside sends when you press 'Delete scrobble' button. For this to work you might need to change `CSRFTOKEN` and `SESSIONID` which you can find in `Network` tab in Chrome developer tools. Idk about other browsers.

Also you might need to change `CSRFMIDDLEWARE` which you can find in `Elements` tab in Chrome developer tools if you inspect `Delete scrobble` button and look over the html form it belongs to.

Any Python version will work hopefully because there's no any additional libraries. I personally used 3.10.6
By default it deletes scrobbles which artist you have listened only once.
If you want another behaviour edit this function to your needs
```python
	def filter_shitty_scrobbles(scrobbles, artist_counts)
```
It asks for confirmation before deleting as well, and saves all the information in json format in the script directory such as *how it was before*, *what it is going to delete*, *what it have deleted*, *what it failed to delete*.

Run with
```sh
	python delete_crap_scrobbles.py 
```

Default timeout before request is set to 0.25f. You can try to set it lower but don't forget to respect the API or it won't respect you!