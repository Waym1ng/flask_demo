# -*- coding: utf-8 -*-
from flask import render_template
from hello.home import home_bp

@home_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')