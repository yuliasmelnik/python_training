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
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contacts_in_groups = []
    for group in db.get_group_list():
        contacts_in_groups.extend(db.get_contacts_in_group(group))
    contact_list=db.get_contact_list()
    contacts = list(set(contact_list).difference(contacts_in_groups))
    if len(contacts) == 0:
        new_contact = (Contact(firstname="test_new", middlename="test_new", lastname="test_new", nickname="test_new",
                                   company="test_new", title="test_new", address="test_new", homephone="test_new", mobilephone="test_new",
                                   workphone="test_new", email="test_new", email2="test_new", email3="test_new",
                                   homepage="test_new", bday="1", bmonth="May", byear="1900", aday="31",
                                   amonth="December", ayear="1900"))
        app.contact.create(new_contact)
        contact_list_with_new_contact = db.get_contact_list()
        index = len(contact_list_with_new_contact)-1
        contact = contact_list_with_new_contact[index]
    else:
        contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    contact_in_some_group = app.contact.add_contact_in_some_group(contact_id=contact.id, group_id=group.id)
    contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    index = contacts_in_group.index(contact)
    contact_in_group = contacts_in_group[index]
    assert contact_in_some_group.id == contact_in_group.id