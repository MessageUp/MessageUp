from service import app, db

from service.forms import StoreForm, ReadForm
from flask import render_template, flash
@app.route('/')
def home():
    return render_template('index.html', page='home')


@app.route('/read', methods=['GET', 'POST'])
def read():
    form = ReadForm()
    error = None
    message = None
    if form.validate_on_submit():
        try:
            message = db.get(form.key.data, int(form.mid.data))
        except ValueError as e:
            error = str(e)
    if form.errors:
        error = 'Error submitting from. Please check your input. %s' % str(form.errors)

    return render_template('read.html', form=form, page='read', error=error, message=message)


@app.route('/store', methods=['GET','POST'])
def store():
    form = StoreForm()
    error = None
    if form.validate_on_submit():
        try:
            rowid = db.store(form.key.data, form.message.data)
            flash('Message saved! Message ID: %s' % rowid)
        except ValueError as e:
            error = "Error: %s" % str(e)
    if form.errors:
        error = 'Error submitting from. Please check your input. %s' % str(form.errors)

    return render_template('store.html', form=form, page='store', error=error)
