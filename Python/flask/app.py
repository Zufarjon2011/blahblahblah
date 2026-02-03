from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123aAtrue@127.0.0.1/news'
db = SQLAlchemy(app)

# Models
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    posts = db.relationship('Post', back_populates='category')

    def __repr__(self):
        return f'<Category {self.title}>'

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='posts')

    def __repr__(self):
        return f'<Post {self.title}>'

# Route
@app.route("/")
def index():
    categories = Category.query.all()
    posts = Post.query.all()
    return render_template("news/index.html", categories=categories, title='Главная', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
