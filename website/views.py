from flask import Flask, Blueprint, redirect, render_template, url_for, request
from .models import Todo
from . import db
import colorama 
from colorama import Fore, Style, Back

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    print(todo_list)
    message = request.args.get("message", None)
    return render_template("index.html", todo_list=todo_list, message=message)

@my_view.route("/add", methods=["POST"])
def add():
    try:
        task = request.form.get("task")
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
    # Changes have to be saved.
        return redirect(url_for("my_view.home"))
    # redirects us back to home.
    except:
        message= "There was an error adding your task"
        # Leth themknow there was an error
        return redirect(url_for("my_view.home", message=message))
        # takes them back to homepage to try again

@my_view.route("/update/<todo_id>", methods=["POST"])
#            Path ID hands it to out function
def update(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete or todo.complete
        db.session.commit()
        return redirect(url_for("my_view.home"))
    except:
        message = "Edit not saved"
        return redirect(url_for("my_view.home", message=message))


@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    task = request.form.get("task1")
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    message = "Task deleted"
    return redirect(url_for("my_view.home"))
    




