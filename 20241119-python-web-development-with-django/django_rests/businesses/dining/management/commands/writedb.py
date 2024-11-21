from django.core.management import BaseCommand, CommandError
from dining.models import Restaurant
import os
import requests

# django command can do anything
# does not has to be database
# e.g. at day end, store stock data

API_KEY = "XvjYqbn8DC8HN_eYPfE_w9vI-YBeuYN80lDtUtM1pFWrD4Ty3tG4mAodP_qOB3Noc4heAO4t-QAD8tb6y8IPctgTV8C1QJuvn_QathZzFcsLDz2jB6Q7YGCtNxI1Z3Yx"
url = "https://api.yelp.com/v3/businesses/search"
headers = {"Authorization": f"Bearer {API_KEY}"}
params = {"term": "restaurants", "location": "California", "limit": 50}
path = "/Users/n/Desktop/Oscar/noble-table/20241119-python-web-development-with-django/django_rests/businesses/uploads"

# New York City
# Chicago
# California

def fetch_img(url, title, folder_name):
    _, extension = os.path.splitext(url)
    file_name = f"{title}{extension}"
    file_path = os.path.join(folder_name, file_name)
    response = requests.get(url)

    with open(file_path, "wb") as image_file:
        image_file.write(response.content)

    return image_file, file_name

class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        for res in data["businesses"]:
            try:
                cuisine = res.get("categories")[0].get("title", "")
            except:
                cuisine = ""

            name = res.get('name', '')
            location = res.get("location", {})
            img = fetch_img(res.get("image_url"), name.replace(" ","-"), path)[1]

            res_detail, created = Restaurant.objects.get_or_create(
                name = name,
                rating = res.get("rating", 0),
                review_count = res.get("review_count", 0),
                price = len(res.get("price", "")),
                cuisine = cuisine,
                image = img,
                address = location.get("address1", ""),
                city = location.get("city", ""),
                zip_code = location.get("zip_code", ""),
                state = location.get("state", ""),
                phone = res.get("display_phone", ""),
            )

            print(res_detail, created)


