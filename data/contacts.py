# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string


constant = [Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                    company="company1", title="title1", address="address1", homephone="homephone1",
                    mobilephone="mobilephone1", workphone="workphone1", email="email1", email2="email21",
                    email3="email31", homepage="homepage1"),
            Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
                    company="company2", title="title2", address="address2", homephone="homephone2",
                    mobilephone="mobilephone2", workphone="workphone2", email="email2", email2="email22",
                    email3="email32", homepage="homepage2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_without_space(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                      company="", title="", address="", homephone="", mobilephone="",
                      workphone="", email="", email2="", email3="",
                      homepage="")] + [
    Contact(firstname=random_string_without_space("firstname", 10), middlename=random_string_without_space("middlename", 10),
            lastname=random_string_without_space("lastname", 10), nickname=random_string("nickname", 10),
            company=random_string("company", 10), title=random_string("title", 10),
            address=random_string("address", 20), homephone=random_string_without_space("homephone", 5),
            mobilephone=random_string_without_space("mobilephone", 5), workphone=random_string_without_space("workphone", 5),
            email=random_string_without_space("email", 10), email2=random_string_without_space("email2", 10),
            email3=random_string_without_space("email3", 10), homepage=random_string_without_space("homepage", 10))
    for i in range(5)
    ]

