from recipe_scrapers import scrape_me



link = "https://www.hellofresh.fr/recipes/rigatoni-aux-epinards-miso-and-champignons-65e1db39174d24a92992304c"
scraper = scrape_me(link, wild_mode=True)
scraper.host()
scraper.title()
scraper.total_time()
scraper.image()
scraper.ingredients()
scraper.ingredient_groups()
scraper.instructions()
scraper.instructions_list()
scraper.yields()
scraper.to_json()
scraper.links()


print(scraper.ingredients())
# scraper.nutrients()  # not always available
# scraper.canonical_url()  # not always available
# scraper.equipment()  # not always available
