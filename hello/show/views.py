# -*- coding: utf-8 -*-
from flask import render_template
from hello.show import show_bp

@show_bp.route('/', methods=['GET'])
def show():

    return render_template('show.html')