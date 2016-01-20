# -*- coding: utf-8 -*-
"""
    Viewed Tests
    ~~~~~~~~~~~~

    Tests the Viewed application.

    :copyright: (c) 2016 by Dan Nascimbeni.
"""

import pytest

import os
import viewed
import tempfile


@pytest.fixture
def client(request):
    db_fd, viewed.app.config['DATABASE'] = tempfile.mkstemp()
    viewed.app.config['TESTING'] = True
    client = viewed.app.test_client()
    with viewed.app.app_context():
        viewed.init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(viewed.app.config['DATABASE'])
    request.addfinalizer(teardown)

    return client


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)

def new_user_request(client):
    return client.get('/new_user_request', follow_redirects=True)
	
def view_user_request(client):
    return client.get('/view_user_request', follow_redirects=True)

