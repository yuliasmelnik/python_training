# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                               company="test", title="test", address="test", home="test", mobile="test",
                               work="test", fax="test", email="test", email2="test", email3="test",
                               homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                               amonth="December", ayear="1900"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                               company="test", title="test", address="test", home="test", mobile="test",
                               work="test", fax="test", email="test", email2="test", email3="test",
                               homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                               amonth="December", ayear="1900")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)