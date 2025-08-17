# -*- coding: utf-8 -*-
import allure

from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                   company="test", title="test", address="test", homephone="test", mobilephone="test",
                                   workphone="test", email="test", email2="test", email3="test",
                                   homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                                   amonth="December", ayear="1900"))
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact_mode = random.choice(old_contacts)
    with allure.step('Given a modify contact with new <firstname>, <lastname>'):
        contact = Contact(firstname="New contact firstname",lastname="New contact lastname")
        contact.id = contact_mode.id
    with allure.step('When I modify the contact from the list'):
        app.contact.modify_contact_by_id(contact.id, contact)
    with allure.step('Then the new contact list is equal to the old list with modified contact'):
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        index = old_contacts.index(contact_mode)
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_modify_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
#                               company="test", title="test", address="test", home="test", mobile="test",
#                               work="test", email="test", email2="test", email3="test",
#                               homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
#                               amonth="December", ayear="1900"))
#    app.contact.modify_first_contact(Contact(middlename="New contact middlename"))
