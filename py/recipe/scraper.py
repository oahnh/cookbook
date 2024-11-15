from recipe_scrapers import scraper_exists_for, scrape_html, WebsiteNotImplementedError
from config.config import EXTRACTED_FIELDS
import requests


def get_scraper(url):
    if not scraper_exists_for(url):
        raise WebsiteNotImplementedError(domain=url)
    try:
        res = requests.get(url, headers={"User-Agent": "Noah's Recipe Scraper"})
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"An error occurred: {err}")
        return None, str(err)
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return None, str(err)

    html = res.content
    scraper = scrape_html(html, org_url=url)

    # manually set the scraper data to contain the url
    # scraping library only contains host name
    return scraper, None


def get_recipe_data(scraper):

    if not scraper:
        return None, "invalid scraper object"

    scraper_json = scraper.to_json()

    recipe_data = {field: scraper_json.get(field, None) for field in EXTRACTED_FIELDS}

    return recipe_data, None
