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
    elif len(db.get_group_list()) == 0:
            app.group.create(Group(name="test", header="test", footer="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_in_some_group(id=contact.id, group_id=group.id, group_name=group.name)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    try:
        contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    finally:
        pass
    return contacts_in_group
    assert app.contact.add_contact_in_some_group(contact.id) == contacts_in_group
