from flask import Flask


def createa_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HomeGrid' # this is going to kind of encrypt or secure the cookies and session data related to our website.

    from.views import views
    from.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app # So we have now created a flask pplication. We've initialized its secret key, and then we've returned it from this function. 