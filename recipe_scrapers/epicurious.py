from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string

class Epicurious(AbstractScraper):

    @classmethod
    def host(self):
        return 'epicurious.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return 	self.soup.find('dd', {'class': 'total-time'}).get_text()

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        things =  self.soup.find('div', {'itemprop': 'recipeInstructions'}).findAll(attrs={'class': "preparation-step"})

        results = []
        for x in things:
            results.append(x.get_text().strip())
        
        return results

    def image(self):
        image_html = self.soup.find('meta', {'itemprop': 'image'})['content']
        return image_html