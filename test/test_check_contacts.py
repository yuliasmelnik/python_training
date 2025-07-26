import re
from model.contact import Contact


def test_contact_info_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    for i, j in zip (sorted(contacts_from_home_page, key=Contact.id_or_max), sorted(db_contacts, key=Contact.id_or_max)):
        assert i.firstname == j.firstname
        assert i.lastname == j.lastname
        assert i.address == re.sub(r'\s+', ' ', j.address)
        assert i.all_phones_from_home_page == merge_phones_like_on_home_page(j)
        assert i.all_emails_from_home_page == merge_emails_like_on_home_page(j)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(db_contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [db_contacts.homephone, db_contacts.mobilephone, db_contacts.workphone]))))

def merge_emails_like_on_home_page(db_contacts):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                    [db_contacts.email, db_contacts.email2, db_contacts.email3])))