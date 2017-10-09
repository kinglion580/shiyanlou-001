from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datatime import datatime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLALchemy(app)

class File(db.Model):
    __tablename__='files'

    id=Column(db.Integer,primary_key=True)
    title=Column(db.String(80))
    created_time=(db.Datetime)
    category_id=(db.Integer,db.ForeignKey('categories.id'))
    content=(db.Text)
    category=relationship('Category')


class Category(db.Model):
    __tablename__='categories'

    id=Column(db.Integer,primary_key=True)
    name=Column(db.String(80))
    file=relationship('File')

