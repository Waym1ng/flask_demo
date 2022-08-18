# -*- coding: utf-8 -*-
from flask import render_template
from hello.home import home_bp

@home_bp.route('/login', methods=['GET'])
def login_index():

    return render_template('login/index.html')