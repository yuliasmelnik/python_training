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
    if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test", header="test", footer="test"))
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contacts_in_all_groups=[]
    for group in db.get_group_list():
        contacts_in_all_groups.extend(db.get_contacts_in_group(group))
        contacts_in_all_groups_without_dublicates = list(set(contacts_in_all_groups))
    if len(contacts_in_all_groups_without_dublicates) == 0:
        contacts = db.get_contact_list()
        groups = db.get_group_list()
        contact = random.choice(contacts)
        group = random.choice(groups)
        app.contact.add_contact_in_some_group(contact_id=contact.id, group_id=group.id)
    contacts_in_all_groups = []
    for group in db.get_group_list():
        contacts_in_all_groups.extend(db.get_contacts_in_group(group))
    contacts_in_all_groups_without_dublicates = list(set(contacts_in_all_groups))
    contact_delete = random.choice(contacts_in_all_groups_without_dublicates)
    groups_contact_delete = db.get_group_for_contact(Contact(id=contact_delete.id))
    group_contact_delete = random.choice(groups_contact_delete)
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group_contact_delete.id))
    app.contact.delete_contact_from_group(contact_id=contact_delete.id, group_id=group_contact_delete.id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group_contact_delete.id))
    old_contacts_in_group.remove(contact_delete)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)