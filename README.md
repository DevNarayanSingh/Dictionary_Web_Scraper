### Dictionary Web Scraper
Created with Python and JSON</b>

Content:
[Data Saved](/#saves)
[Process](/#saves)


Two day project to learn more about scraping html website.<br>
Saves the meaning of the word searched.<br>
##### Data Saved (locally):
- [x] the meaning
- [x] 10 last searched history
- [x] times the word searched in total

##### Code Process:
```
-> search a word<br>
-> checks the json file for previously stored meaning of the word, if found:<br>
	-> displays the meaning directly<br>
-> otherwise:<br>
	-> fetches the dictionary.com for the word<br>
	-> meaning of the word is displayed (if the relevant page is found),
	   which is also stored in a json file<br><br>
```
