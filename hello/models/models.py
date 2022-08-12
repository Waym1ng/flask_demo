# -*- coding: utf-8 -*-
from datetime import datetime

from hello.utils.orm import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class ShowData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(128))
    name = db.Column(db.String(32))
    ssn = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    email = db.Column(db.String(32))
    job = db.Column(db.String(32))
    address = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
