from flask import Blueprint,render_template,request,flash
from flask_login import login_user,login_required,logout_user,current_user
from .models import Note
from . import db
from datetime import datetime


views = Blueprint('views',__name__)


@views.route('/')
def app():
    return render_template("base.html",user=current_user)

@views.route('/home',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) <= 1:
            flash("Note is too short!",category='error')
        else:
            new_note = Note(data=note,user_id=current_user.id,date=datetime.utcnow())
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!',category='sucess')
    return render_template("home.html",user=current_user)