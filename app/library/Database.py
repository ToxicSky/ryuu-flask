from flask_sqlalchemy import SQLAlchemy


class Database:
    db = None
    # uri = 'mysql://root:root@localhost/fallout'

    def connect(self, app):
        # app.config['SQLALCHEMY_DATABASE_URI'] = self.uri
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username
