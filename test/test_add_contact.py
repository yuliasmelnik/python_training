# -*- coding: utf-8 -*-
import random
import string
import pytest
from model.contact import Contact

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_without_space(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                      company="", title="", address="", homephone="", mobilephone="",
                      workphone="", email="", email2="", email3="",
                      homepage="", bday="", bmonth="", byear="", aday="",
                      amonth="", ayear="")] + [
    Contact(firstname=random_string_without_space("firstname", 10), middlename=random_string_without_space("middlename", 10),
            lastname=random_string_without_space("lastname", 10), nickname=random_string("nickname", 10),
            company=random_string("company", 10), title=random_string("title", 10),
            address=random_string("address", 20), homephone=random_string_without_space("homephone", 5),
            mobilephone=random_string_without_space("mobilephone", 5), workphone=random_string_without_space("workphone", 5),
            email=random_string_without_space("email", 10), email2=random_string_without_space("email2", 10),
            email3=random_string_without_space("email3", 10), homepage=random_string_without_space("homepage", 10))
    for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


