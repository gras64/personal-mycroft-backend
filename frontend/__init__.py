from flask import Flask, redirect, url_for, render_template, request, \
    session, make_response, flash
from flask_mail import Mail, Message
from flask_sslify import SSLify

from settings import *
from database.users import db_connect

__author__ = "JarbasAI"

engine = db_connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT
app.config["MAIL_SERVER"] = MAIL_SERVER
app.config["MAIL_PORT"] = MAIL_PORT
app.config["MAIL_USE_TLS"] = MAIL_USE_TLS
app.config["MAIL_USE_SSL"] = MAIL_USE_SSL
app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
app.config["MAIL_DEFAULT_SENDER"] = MAIL_DEFAULT_SENDER

sslify = SSLify(app)
mail = Mail(app)

from frontend.main import login, logout, signup, confirm, unconfirmed, \
    resend, settings, pair


def start_frontend(port=WEBSITE_PORT):
    if SSL:
        import ssl
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(SSL_CERT, SSL_KEY)
        app.run(debug=DEBUG, port=port, ssl_context=context,
                use_reloader=True)
    else:
        app.run(debug=DEBUG, port=port, use_reloader=True)

if __name__ == "__main__":
    start_frontend()