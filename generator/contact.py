# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__,indent=2))