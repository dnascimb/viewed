# -*- coding: utf-8 -*-
"""
    Viewed
    ~~~~~~

    Application using Flask.

    :copyright: (c) 2016 by Dan Nascimbeni.

"""

from flask import Flask
from viewed.database import db_session

# create the application
app = Flask(__name__)
app.secret_key = 'sipPinOnGinAndJuiceLaidBack'

import viewed.views


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


