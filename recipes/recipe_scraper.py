"""NYT Recipe scraper class."""

from bs4 import BeautifulSoup
from collections import namedtuple
from urllib import request


ELEMENT_CLASSES_DICT = {
    'INGREDIENTS': 'recipe-ingredients',
    'PREPERATION': 'recipe-steps',
    'TIME_YIELD': 'recipe-yield-value',
    'TITLE': 'recipe-title'
}

ELEMENT_TUPLE = namedtuple('elements', ELEMENT_CLASSES_DICT.keys())
ELEMENT_CLASSES = ELEMENT_TUPLE(**ELEMENT_CLASSES_DICT)

LINE_BREAK = '\n'


class RecipeScraper():
    """NYT recipe scraper class."""

    is_valid = True
    page_source = None

    def __init__(self, url: str):
        """Init recipe scraper."""
        base_url = url.split('?')[0]
        self.page_source = self._get_page_source(base_url)
        self.is_valid = self._validate()

    def scrape(self):
        """Build recipe."""
        if not self.is_valid:
            return

        ingredients = self._ingredients()
        prep = self._preperation()
        time_servings = self._time_yield()
        title = self._title()

        recipe = [LINE_BREAK, title, time_servings, ingredients, prep, LINE_BREAK]
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
        ingredients_ul = self.page_source.find(class_=ELEMENT_CLASSES.INGREDIENTS)
        items = ingredients_ul.find_all('span')
        ingredients = str()

        for ingredient in items:
            index = items.index(ingredient)
            text = ingredient.get_text().strip()
            line = f' {text}'

            if index == 0 or index % 2 == 0:
                line = f'{LINE_BREAK} {text}'

            ingredients += line

        return f'{LINE_BREAK} INGREDIENTS {LINE_BREAK} {ingredients.strip()}'

    def _preperation(self):
        """Find, parse, and format recipe preperation from source."""
        steps_ol = self.page_source.find(class_=ELEMENT_CLASSES.PREPERATION)
        return f'{LINE_BREAK} PREPERATION {LINE_BREAK} {steps_ol.get_text().strip()}'

    def _time_yield(self):
        """Find serving size and recipe time from source."""
        spans = self.page_source.find_all(class_=ELEMENT_CLASSES.TIME_YIELD)
        values = [span.get_text().strip() for span in spans]
        return ', '.join(values)

    def _title(self):
        """Find recipe title from source."""
        title = self.page_source.find(class_=ELEMENT_CLASSES.TITLE)
        return title.get_text().strip().upper()

    def _validate(self):
        """Validate page_source has valid class elements."""
        for klass in ELEMENT_CLASSES:
            if not self.page_source.find(class_=klass):
                print(f'INVALID SOURCE: {klass} NOT FOUND')
                return False
        return True
