import os
import csv
from config import db
from models import Product, Review


def fill_products(products_file):
    with open(products_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            p = Product(asin=row["Asin"], title=row["Title"])
            db.session.add(p)
        db.session.commit()


def fill_reviews(reviews_file):
    with open(reviews_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            r = Review(
                product_asin=row["Asin"],
                title=row["Title"],
                article=row["Review"]
            )
            db.session.add(r)
        db.session.commit()


def read_csv():
    # breakpoint()
    parent_dir = os.getcwd()
    csv_dir = os.path.join(parent_dir, 'csv')
    # os.listdir(csv_dir)
    # ['Reviews.csv', 'Products.csv']
    products_file = os.path.join(csv_dir, 'Products.csv')
    reviews_file = os.path.join(csv_dir, 'Reviews.csv')

    # fill tables with data
    fill_products(products_file)
    fill_reviews(reviews_file)

# deal with local SQLite
# if os.path.exists("marakas.db"):
#     os.remove("marakas.db")


db.session.query(Product).delete()
db.session.query(Review).delete()
db.session.commit()

# Create the database
db.create_all()

read_csv()

db.session.commit()
