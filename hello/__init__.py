# -*- coding: utf-8 -*-
from flask import Flask

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
    from hello.user import user_bp
    app.register_blueprint(user_bp)
    from hello.home import home_bp
    app.register_blueprint(home_bp)
    # 可选参数
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    bootstrap = Bootstrap(app)
    moment = Moment(app)

    return app