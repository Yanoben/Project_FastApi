import sqlalchemy
from .base import metadata

apples = sqlalchemy.Table(
    "apples",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      primary_key=True,
                      autoincrement=True,
                      unique=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'),
                      nullable=False),
    sqlalchemy.Column(
        "name", sqlalchemy.String),
    sqlalchemy.Column(
        "description", sqlalchemy.String)
)
