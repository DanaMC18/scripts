"""Recipe scraper CLI."""

from recipe_scraper import RecipeScraper


print('ENTER URL HERE:')

recipe_url = input()

URL_PREFIX = 'https://cooking.nytimes.com/recipes/'

if URL_PREFIX not in recipe_url:
    print('The specified url is invalid')

RecipeScraper(recipe_url).scrape()
