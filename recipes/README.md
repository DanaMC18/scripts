# NYT Recipe Scraper
Built using python 3 and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

**Install dependencies:** `pip install -r requirements.txt`


## RecipeScraper
Class that expects a NYT recipe URL. It parses the page source of the URL and returns a formatted recipe.
It can also be run in this [repl.it](https://repl.it/@DanaMC18/nyt-recipes#main.py).


### Usage
```python
recipe_scraper = RecipeScraper('https://cooking.nytimes.com/recipes/some-recipe')
recipe_scraper.scrape()
```

```bash
>>>

'NAME OF RECIPE'
 '# servings, # minutes or hours'

 'INGREDIENTS'
 ' quantity  ingredient'

 'PREPERATION'
 ' Cook the food.'
```


## CLI
The scraper can be run directly in the command-line by providing a valid url.

```bash
$ python run_parser.py https://cooking.nytimes.com/recipes/some-recipe
```
