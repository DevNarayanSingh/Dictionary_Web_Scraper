### Dictionary Web Scraper
Created with Python, saves a local file in JSON format.</b>

#### Contents:
[Data Saved](https://github.com/DevNarayanSingh/Dictionary_Web_Scraper/blob/main/README.md#data-saved-locally)<br>
[Process](https://github.com/DevNarayanSingh/Dictionary_Web_Scraper/blob/main/README.md#code-process)<br>


Two day project to learn more about scraping html website.<br>
Saves the meaning of the word searched.<br>
##### Data Saved (locally):
- [x] the meaning
- [x] 10 last searched history
- [x] times the word searched in total

##### Code Process:
```
search a word
checks the json file for previously stored meaning of the word, if found:
	displays the meaning directly
otherwise:
	fetches the dictionary.com for the word
	meaning of the word is displayed (if the relevant page is found),
	which is also stored in a json file
```
