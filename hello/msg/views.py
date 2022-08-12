# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template
from hello.forms import HelloForm
from hello.utils.orm import db
from hello.models.models import Message
from hello.msg import msg_bp

@msg_bp.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('msg.index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)