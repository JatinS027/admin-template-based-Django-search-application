import pandas as pd
from search_app.models import Restaurant
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_search.settings')
django.setup()

csv_url = "https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv"
df = pd.read_csv(csv_url)

Restaurant.objects.all().delete()  # Optional: Clear existing data

for index, row in df.iterrows():
    Restaurant.objects.create(
        name=row['name'],
        dish=row['dish'],
        rating=row['rating']
    )
