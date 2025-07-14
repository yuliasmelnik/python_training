# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                   company="test", title="test", address="test", homephone="test", mobilephone="test",
                                   workphone="test", email="test", email2="test", email3="test",
                                   homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                                   amonth="December", ayear="1900"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New contact firstname",lastname="New contact lastname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
#                               company="test", title="test", address="test", home="test", mobile="test",
#                               work="test", email="test", email2="test", email3="test",
#                               homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
#                               amonth="December", ayear="1900"))
#    app.contact.modify_first_contact(Contact(middlename="New contact middlename"))
