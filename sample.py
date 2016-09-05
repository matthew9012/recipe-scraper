#!/usr/bin/python3

from recipe_scrapers import scrap_me

s = scrap_me("http://allrecipes.com/recipe/221093/good-frickin-paprika-chicken/")

try:
    print("~~~~~~~~~~~TITLE~~~~~~~~~~~~~")
    print(s.title())
except Exception:
    print("no title")
try:
    print("~~~~~~~~~~~TIME~~~~~~~~~~~~~")
    print(s.total_time())
except Exception:
    print("no time")
try:
    print("~~~~~~~~~~~INGREDIENTS~~~~~~~~~~~~~")
    print(s.ingredients())
except Exception:
    print("no ingredients")
try:
    print("~~~~~~~~~~~INSTRUCTIONS~~~~~~~~~~~~~")
    print(s.instructions())
except Exception:
    print("no instructions")
try:
    print("~~~~~~~~~~~IMAGE~~~~~~~~~~~~~")
    print(s.image())
except Exception:
    print("no image")
