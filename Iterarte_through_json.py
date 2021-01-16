def return_listings(response):

    results = response['results']

    listings = []
    for item in results:
        listing = {}
        listing['url'] = item['url']
        listing['title'] = item['title']
        listings.append(listing)

    return {'listings': listings}