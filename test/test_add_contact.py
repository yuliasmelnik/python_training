# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="arty", middlename="rtyu", lastname="otyu", nickname="tyui",
                      company="sdfg", title="asdf", address="dfgh", homephone="homedfgh", mobilephone="mobileghjk",
                      workphone="workphjkl", email="zxcv", email2="vbnm", email3="vbnm",
                      homepage="fghj", bday="20", bmonth="December", byear="1986", aday="10",
                      amonth="May", ayear="2002")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


