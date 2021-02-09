from config import db, ma


class Product(db.Model):
    __tablename__ = "product"
    asin = db.Column(db.String(32), primary_key=True)
    title = db.Column(db.String(200))
    reviews = db.relationship(
        "Review",
        backref="product",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )


class Review(db.Model):
    __tablename__ = "review"
    review_id = db.Column(db.Integer, primary_key=True)
    product_asin = db.Column(db.String(32), db.ForeignKey('product.asin'))
    title = db.Column(db.String(200))
    article = db.Column(db.String(200))
    parent = db.relationship("Product", back_populates="reviews")


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True
