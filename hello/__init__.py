# -*- coding: utf-8 -*-
from flask import Flask, render_template

from flask_wtf.csrf import CSRFError
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from hello.utils.orm import db


def create_app(config_name="setting.dev"):
    """
    创建app
    """
    # 实例化
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config_name)
    # 加载数据库
    db.init_app(app)
    # 注册蓝图
    register_blueprints(app)
    # 异常处理
    register_error_handlers(app)
    # 可选参数
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    bootstrap = Bootstrap(app)
    moment = Moment(app)

    return app

def register_blueprints(app):
    """
    注册蓝图
    """
    from hello.msg import msg_bp
    app.register_blueprint(msg_bp)
    from hello.home import home_bp
    app.register_blueprint(home_bp)
    from hello.show import show_bp
    app.register_blueprint(show_bp)

def register_error_handlers(app):
    """
    注册异常处理
    """
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=e.description), 500