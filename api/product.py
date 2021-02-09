"""
This is the product module and supports some the REST actions
"""

from flask import abort
from models import Product, ProductSchema, Review, ReviewSchema


def read_all():
    """
    This function responds to a request for /api/product
    with the complete lists of product
    :return:        json string of list of products
    """

    people = Product.query.order_by(Product.asin).all()

    # Serialize the data for the response
    product_schema = ProductSchema(many=True)
    data = product_schema.dump(people)
    return data


def read_one(asin):
    """
    This function responds to a request for /api/product/{product_asin}
    with one matching product from products
    :param asin:   Asin of product to find
    :return:            product matching id
    """
    product = Product.query.filter(Product.asin == asin).one_or_none()

    if product is not None:

        # Serialize the data for the response
        product_schema = ProductSchema()
        product_data = product_schema.dump(product)

        reviews = Review.query.filter(Review.product_asin == asin).all()
        review_schema = ReviewSchema()

        # combine product description and reviews
        data = {
            'product': product_data,
            'reviews': [review_schema.dump(r) for r in reviews],
        }

        return data
    else:
        abort(
            404,
            "Product not found for Id: {asin}".format(asin=asin),
        )
