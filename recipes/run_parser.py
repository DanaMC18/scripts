"""Recipe scraper CLI."""

import argparse
import sys

from recipe_scraper import RecipeScraper


URL_PREFIX = 'https://cooking.nytimes.com/recipes/'

parser = argparse.ArgumentParser(
    description='Print a NYT recipe from a given URL.'
)

parser.add_argument(
    'Url',
    metavar='url',
    type=str,
    help=f'NYT recipe url; should start with {URL_PREFIX}'
)

args = parser.parse_args()

recipe_url = args.Url

if URL_PREFIX not in recipe_url:
    print('The specified url is invalid')
    sys.exit()

RecipeScraper(recipe_url).scrape()
