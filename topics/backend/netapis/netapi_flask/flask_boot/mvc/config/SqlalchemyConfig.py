from flask_sqlalchemy import SQLAlchemy

from boot_framework.conventions import BasicConfig


class SqlalchemyConfig(BasicConfig):
    db = None

    def init_app(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = '...'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.db = SQLAlchemy()
        self.db.init_app(app)
        app.db = self.db

        ...

