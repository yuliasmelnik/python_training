# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="arty", middlename="rtyu", lastname="otyu", nickname="tyui",
                               company="sdfg", title="asdf", address="dfgh", home="dfgh", mobile="ghjk",
                               work="hjkl", fax="kl;h", email="zxcv", email2="vbnm", email3="vbnm",
                               homepage="fghj", bday="20", bmonth="December", byear="1986", aday="10",
                               amonth="May", ayear="2002"))
    app.session.logout()


