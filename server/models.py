from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"  

    # Define columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    magnitude = db.Column(db.Float, nullable=False)  # Magnitude column
    location = db.Column(db.String(100), nullable=False)  # Location column
    year = db.Column(db.Integer, nullable=False)  # Year column

    def __repr__(self):
        # Format attributes for better debugging and representation
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"