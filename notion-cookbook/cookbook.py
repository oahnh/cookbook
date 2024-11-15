import requests

from recipe_scrapers import scrape_html

url1 = "https://www.allrecipes.com/recipe/23431/to-die-for-fettuccine-alfredo/"
url2 = "https://www.maangchi.com/recipe/oi-bokkeum"

html = requests.get(
    "https://www.maangchi.com/recipe/maeuntang",
    headers={"User-Agent": "Burger Seeker Noah"},
).text
scraper = scrape_html(html, org_url="https://www.maangchi.com/recipe/maeuntang")

print(scraper.ingredients())


# links that don't properly get scraped for ingredients:
