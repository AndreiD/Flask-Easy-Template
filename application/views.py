import sendgrid
from flask import request, render_template, flash, current_app, jsonify
from application import app, logger, cache
from application.decorators import threaded_async
from application.models import *
from forms import *
from time import time


@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
    m_tasks = SampleTable()

    list_records = m_tasks.list_all(page, app.config['LISTINGS_PER_PAGE'])

    return render_template("index.html", list_records=list_records)


@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    form = Form_Record_Add(request.form)

    if request.method == 'POST':
        if form.validate():
            new_record = SampleTable()

            title = form.title.data
            description = form.description.data

            new_record.add_data(title, description)
            logger.info("Adding a new record.")
            flash("Record added successfully.", category="success")

    return render_template("add_record.html", form=form)


@threaded_async
def send_email(app, to, subject, body):
    with app.app_context():
        sg = sendgrid.SendGridClient("SG.pRFA8c9bRXXXXXXXXXXXXXXXXXXXXXXXXX")
        message = sendgrid.Mail()
        message.add_to(to)
        message.set_subject(subject)
        message.set_html(body)
        message.set_from('Template No-Reply <noreplay@flaskeasytemplate.com>')
        try:
            status, msg = sg.send(message)
            print("Status: " + str(status) + " Message: " + str(msg))
            if status == 200:
                return True
        except Exception, ex:
            print("------------ ERROR SENDING EMAIL ------------" + str(ex.message))
    return False


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    recaptcha = current_app.config['RECAPTCHA_SITE_KEY']
    email_sent = False

    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        message = request.form['message']
        recaptcha_response = request.form['g-recaptcha-response']

        send_email(app, to=current_app.config['ADMIN_EMAIL'], subject="Contact Form Flask Shop",
                   body=email + " " + name + " " + message)

        email_sent = True

    return render_template("contact.html", RECAPTCHA_SITE_KEY=recaptcha, email_sent=email_sent)


# ----- UTILS. Delete them if you don't plan to use them -----

@app.route('/cache_true')
@cache.cached(timeout=120)
def cached_examples():
    start = time()
    records = SampleTable().benchmark_searchspeed()
    return jsonify(data=records, cached_at=datetime.datetime.now(), done_in=time() - start)


@app.route('/cache_false')
def not_cached_examples():
    start = time()
    records = SampleTable().benchmark_searchspeed()
    return jsonify(result=records, cached_at=datetime.datetime.now(), done_in=time() - start)


@app.route('/fill_db')
def fill_db():
    # ---- it might take some time ----

    from random import choice
    from string import printable
    import humanize
    import os
    start = time()
    lis = list(printable)
    for i in range(0, 50000):
        title = ''.join(choice(lis) for _ in xrange(5))
        description = ''.join(choice(lis) for _ in xrange(200))
        SampleTable().add_data(title, description)

    return "done in %.3f  | database size: %s" % (time() - start, humanize.naturalsize(os.path.getsize("db.sqlite")))


@app.route('/get_user/<int:userId>')
def get_user(userId=0):
    result = SampleTable().get_id(userId)
    return jsonify(data=result)


@app.before_first_request
def before_first_request():
    logger.info("-------------------- initializing everything ---------------------")
    db.create_all()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
