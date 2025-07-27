# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

def test_add_contact_in_some_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                   company="test", title="test", address="test", homephone="test", mobilephone="test",
                                   workphone="test", email="test", email2="test", email3="test",
                                   homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                                   amonth="December", ayear="1900"))
    if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test", header="test", footer="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    contact_in_some_group = app.contact.add_contact_in_some_group(contact_id=contact.id, group_id=group.id)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    try:
        contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    finally:
        index = contacts_in_group.index(contact)
        contact_in_group = contacts_in_group[index]
        assert contact_in_some_group.id == contact_in_group.id