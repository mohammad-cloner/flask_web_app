from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/task', methods=['GET', 'POST'])
@login_required

def task():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("Task.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/', methods=['GET', 'POST'])
@login_required

def home():

    return render_template("home2.html", user=current_user)

@views.route('/telegram')
@login_required

def telegram():
    return render_template("telegram.html", user=current_user)

@views.route('/dashboard')
@login_required

def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/setting')
@login_required

def setting():
    return render_template("change_password.html", user=current_user)