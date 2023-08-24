import logging
import traceback
from functools import wraps

from flask_sqlalchemy import SQLAlchemy

from boot_framework.Scanner.TargetBasic import BasicConfig


class SqlalchemyConfig(BasicConfig):
    db = None

    def init_app(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = '...'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.db = SQLAlchemy()
        self.db.init_app(app)
        app.db = self.db

    @staticmethod
    def transaction(func):
        @wraps
        def wrapper(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                SqlalchemyConfig.db.session.commit()
                return result
            except Exception:
                logging.error(traceback.format_exc())
                SqlalchemyConfig.db.session.rollback()
                return None

        return wrapper

