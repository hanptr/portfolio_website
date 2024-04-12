from flask_babel import Babel
from flask import Flask, g, request


class BabelFlask(Babel):
    '''    babel = None

    def __init__(self, app: Flask):
        self.babel = Babel(app)'''

    @staticmethod
    def get_locale():
        user = getattr(g, "user", None)
        if user is not None:
            return user.locale
        return request.accept_languages.best_match(["de", "en", "hun"])
