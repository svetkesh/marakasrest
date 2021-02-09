"""
This is the review module
"""

from flask import abort
from config import db
from models import Review, ReviewSchema, Product


def read_all():
    """
    This function responds to a request for /api/review
    with the complete lists of reviews
    :return:        json string of list of reviews
    """
    # Create the list of reviews
    review = Review.query.order_by(Review.review_id).all()

    # Serialize the data for the response
    review_schema = ReviewSchema(many=True)
    data = review_schema.dump(review)
    return data


def read_one(review_id):
    """
    This function responds to a request for /api/review/{review_id}
    with one matching review from reviews
    :param review_id:   Id of review to find
    :return:            review matching id
    """
    # Get the review requested
    review = Review.query.filter(Review.review_id == review_id).one_or_none()

    if review is not None:
        # Serialize the data for the response
        review_schema = ReviewSchema()
        data = review_schema.dump(review)
        return data

    # Didn't find that review
    else:
        abort(
            404,
            "Review not found for Id: {review_id}".format(review_id=review_id),
        )


def create(review):
    """
    This function creates a new review
    for product with given productc Asin
    :param review:  review to create
    :return:        201 on success, 406 on product_asin not exists
    """

    # get the parent product
    product_asin = review.get("product_asin")
    product = Product.query.filter(Product.asin == product_asin).one_or_none()

    if product is None:
        abort(404, f"Product not found for Asin: {product_asin}")

    schema = ReviewSchema()
    new_review = schema.load(review, session=db.session)
    db.session.add(new_review)
    db.session.commit()

    data = schema.dump(new_review)

    return data, 201


