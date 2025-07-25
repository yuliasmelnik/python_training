# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                   company="test", title="test", address="test", homephone="test", mobilephone="test",
                                   workphone="test", email="test", email2="test", email3="test",
                                   homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                                   amonth="December", ayear="1900"))
    old_contacts = db.get_contact_list()
    contact_mode = random.choice(old_contacts)
    contact = Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                      company="test", title="test", address="test", homephone="test", mobilephone="test",
                      workphone="test", email="test", email2="test", email3="test",
                      homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                      amonth="December", ayear="1900")
    contact.id = contact_mode.id
    app.contact.edit_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    index = old_contacts.index(contact_mode)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)