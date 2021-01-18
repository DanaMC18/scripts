# NYT Recipe Scraper
Built using python 3 and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

**Install dependencies:** `pip install -r requirements.txt`

## RecipeScraper
Class that expects a NYT recipe url and parses the page source, and returns a recipe.

### Usage
```python
recipe_scraper = RecipeScraper('https://cooking.nytimes.com/recipes/some-recipe')
recipe_scraper.scrape()
```

```bash
>>>
'Name of Recipe'
 '# servings, # minutes or hours'
 'INGREDIENTS'
 ' quantity  ingredient'
 'PREPERATION'
 ' Cook the food.'
```


## CLI
The scraper can be run directly in the command-line be providing a valid url.

```bash
$ python recipe_scraper.py https://cooking.nytimes.com/recipes/some-recipe
```
