from . import db
import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    #                         no longer than 300 words (limitation), the unique keeps the data clean 
    complete = db.Column(db.Boolean, default = False)
    #These arre the columns.