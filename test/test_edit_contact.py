# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                               company="test", title="test", address="test", home="test", mobile="test",
                               work="test", fax="test", email="test", email2="test", email3="test",
                               homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                               amonth="December", ayear="1900"))
    app.contact.edit_first_contact(Contact(firstname="editf", middlename="editm", lastname="editl", nickname="editn",
                               company="editc", title="editt", address="edita", home="edith", mobile="editm",
                               work="editw", fax="editf", email="edite", email2="edite2", email3="edite3",
                               homepage="edith", bday="31", bmonth="December", byear="2000", aday="31",
                               amonth="December", ayear="2025"))