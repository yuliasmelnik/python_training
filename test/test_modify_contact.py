# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                               company="test", title="test", address="test", home="test", mobile="test",
                               work="test", fax="test", email="test", email2="test", email3="test",
                               homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                               amonth="December", ayear="1900"))
    app.contact.modify_first_contact(Contact(firstname="New contact firstname"))

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                               company="test", title="test", address="test", home="test", mobile="test",
                               work="test", fax="test", email="test", email2="test", email3="test",
                               homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                               amonth="December", ayear="1900"))
    app.contact.modify_first_contact(Contact(middlename="New contact middlename"))
