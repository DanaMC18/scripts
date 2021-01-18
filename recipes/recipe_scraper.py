"""NYT Recipe scraper class."""

from bs4 import BeautifulSoup
from collections import namedtuple
from urllib import request


def enum(name, **elements):
    """Create a new enumerable."""
    meta = namedtuple(name, elements.keys())
    return meta(**elements)


ELEMENT_CLASSES = enum(
    'elements',
    INGREDIENTS='recipe-ingredients',
    PREPERATION='recipe-steps',
    TIME_YIELD='recipe-yield-value',
    TITLE='recipe-title'
)

LINE_BREAK = '\n'


class RecipeScraper():
    """NYT recipe scraper class."""

    page_source = None

    def __init__(self, url: str):
        """Init recipe scraper."""
        self.page_source = self._get_page_source(url)

    def scrape(self):
        """Build recipe."""
        ingredients = self._ingredients()
        prep = self._preperation()
        time_servings = self._time_yield()
        title = self._title()

        recipe = [title, time_servings, ingredients, prep]
        for r in recipe:
            print(r)
        return recipe

    def _get_page_source(self, url: str):
        """Get page source html from specified url."""
        res = request.urlopen(url)
        raw_page_source = res.read().decode('utf-8')
        return BeautifulSoup(raw_page_source, 'html.parser')

    def _ingredients(self):
        """Find, parse, and format ingredients from source."""
        ingredients_ul = self.page_source.find('ul', class_=ELEMENT_CLASSES.INGREDIENTS)
        raw_ingredients = ingredients_ul.get_text().strip().split(LINE_BREAK)
        clean_ingredients = [ri.strip() for ri in raw_ingredients if ri]

        ingredients = f'INGREDIENTS {LINE_BREAK}'

        for ingredient in clean_ingredients:
            line = f' {ingredient}'

            if ingredient.isdigit():
                line = f'{LINE_BREAK} {ingredient}'

            ingredients += line

        return ingredients.strip()

    def _preperation(self):
        """Find, parse, and format recipe preperation from source."""
        steps_ol = self.page_source.find('ol', class_=ELEMENT_CLASSES.PREPERATION)
        return f'PREPERATION {LINE_BREAK} {steps_ol.get_text().strip()}'

    def _time_yield(self):
        """Find serving size and recipe time from source."""
        spans = self.page_source.find_all('span', class_=ELEMENT_CLASSES.TIME_YIELD)
        values = [span.get_text() for span in spans]
        return ', '.join(values)

    def _title(self):
        """Find recipe title from source."""
        title = self.page_source.find('h1', class_=ELEMENT_CLASSES.TITLE)
        return title.get_text().strip().upper()
