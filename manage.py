# -*- coding: utf-8 -*-
import click

from flask_script  import Manager
from hello import create_app, db
from hello.models.models import Message, ShowData

app = create_app("setting.dev")
manager = Manager(app)

'''
自定义命令方法: 1. manager.add_command('func', Func()) 2. @manager.command 3. @manager.option('-n', '--name', help='Your name')
使用: python manage.py initDB
'''
@manager.command
def initDB():
    """
    初始化数据库
    """
    db.create_all()
    click.echo('Initialized database.')

@manager.command
def dropDB():
    """
    清空数据库
    """
    click.confirm('This operation will delete the database, do you want to continue?', abort=True)
    db.drop_all()
    click.echo('Drop tables.')

@manager.option('-c', '--count', help='Quantity of data')
def makeMessage(count):
    """
    生成message数据
    """
    from faker import Faker

    fake = Faker(locale='zh_CN')
    click.echo('Working...')

    for i in range(int(count)):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('Created {} fake data.'.format(count))

@manager.option('-c', '--count', help='Quantity of data')
def makeShowData(count):
    """
    生成show data数据
    """
    if not count:
        count = 20
    from faker import Faker

    fake = Faker(locale='zh_CN')
    click.echo('Working...')

    for i in range(int(count)):
        show_data = ShowData(
            uuid = fake.uuid4(),
            name = fake.name(),
            ssn = fake.ssn(),
            phone = fake.phone_number(),
            email = fake.free_email(),
            job = fake.job(),
            address = fake.address(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(show_data)
    db.session.commit()
    click.echo('Created {} fake data.'.format(count))

if __name__ == '__main__':
    """python manage.py runserver -h 127.0.0.1 -p 5000"""
    manager.run()