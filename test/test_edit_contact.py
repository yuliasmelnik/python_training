# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="editf", middlename="editm", lastname="editl", nickname="editn",
                               company="editc", title="editt", address="edita", home="edith", mobile="editm",
                               work="editw", fax="editf", email="edite", email2="edite2", email3="edite3",
                               homepage="edith", bday="31", bmonth="December", byear="2000", aday="31",
                               amonth="December", ayear="2025"))
    app.session.logout()