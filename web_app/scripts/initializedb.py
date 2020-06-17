import os, sys

sys.path.append(os.getcwd() + '/web_app')

from app import create_app
from models import Role, User, db, Page, Menu

app = create_app()

with app.app_context():
    admin_role = Role()
    admin_role.name = 'admin'
    db.session.add(admin_role)
    db.session.commit()

    root = User()
    root.email = 'azizsaefulhidayat@gmail.com'
    root.password = '1234567a'
    root.active = True
    root.roles.append(admin_role)
    db.session.add(root)

    page = Page()
    page.title = 'Homepage'
    page.is_homepage = True
    page.contents = '<h1>Selamat Datang di Homepage</h1>'
    page.url = 'home'
    page.id = 1

    db.session.add(page)
    db.session.commit()

    menu = Menu()
    menu.title = 'Home'
    menu.page_id = 1
    menu.order = 1

    db.session.add(menu)
    db.session.commit()