# -*- coding: utf-8 -*-
from flask import render_template
from hello.utils.orm import db
from hello.models.models import ShowData
from hello.show import show_bp


@show_bp.route('/', methods=['GET'])
def index():
    data = ShowData.query.order_by(ShowData.id.desc()).all()
    return render_template('show/index.html', data=data)
