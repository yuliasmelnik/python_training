# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                   company="test", title="test", address="test", homephone="test", mobilephone="test",
                                   workphone="test", email="test", email2="test", email3="test",
                                   homepage="test", bday="1", bmonth="May", byear="1900", aday="31",
                                   amonth="December", ayear="1900"))
    elif len(db.get_group_list()) == 0:
            app.group.create(Group(name="test", header="test", footer="test"))
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    try:
        contacts_in_all_groups = db.get_contacts_in_all_groups()
    finally:
        if len(db.get_contacts_in_all_groups()) == 0:
            contacts = db.get_contact_list()
            groups = db.get_group_list()
            contact = random.choice(contacts)
            group = random.choice(groups)
            app.contact.add_contact_in_some_group(contact_id=contact.id, group_id=group.id)
        from_delete_group = random.choice(contacts_in_all_groups)
        try:
            contacts_in_group = db.get_contacts_in_group(Group(id=from_delete_group.id))
        finally:
            contact_delete = random.choice(contacts_in_group)
            app.contact.delete_contact_from_group(contact_id=contact_delete.id, group_id=from_delete_group.id)
            new_contacts_in_group = db.get_contacts_in_group(Group(id=from_delete_group.id))
            contacts_in_group.remove(contact_delete)
            assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
