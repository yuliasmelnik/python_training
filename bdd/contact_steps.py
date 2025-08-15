from pytest_bdd import given, when, then, parsers
from model.contact import Contact
import random

@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given(parsers.parse('a contact with {firstname}, {middlename}, {lastname}, {nickname}, {company}, {title}, '
                     '{address}, {homephone}, {mobilephone}, {workphone}, {email}, {email2}, {email3}, {homepage}'), target_fixture='new_contact')
def new_contact(firstname, middlename, lastname, nickname, company, title, address, homephone, mobilephone, workphone,
              email, email2, email3, homepage):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, company=company,
                   title=title, address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                   email=email, email2=email2, email3=email3, homepage=homepage)
@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, new_contact, contact_list):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    return db.get_contact_list()

@given('a random contact from the list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(app, random_contact, non_empty_contact_list, db, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

@given(parsers.parse('a modify contact with new {firstname}, {middlename}, {lastname}, {nickname}, {company}, '
                     '{title}, {address}, {homephone}, {mobilephone}, {workphone}, {email}, {email2}, {email3}, '
                     '{homepage}'), target_fixture='new_contact_date')
def new_contact_date(firstname, middlename, lastname, nickname, company, title, address, homephone, mobilephone, workphone,
              email, email2, email3, homepage):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, company=company,
                   title=title, address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                   email=email, email2=email2, email3=email3, homepage=homepage)

@when('I modify the contact from the list')
def modify_contact(app, random_contact, new_contact_date):
    new_contact_date.id = random_contact.id
    app.contact.modify_contact_by_id(random_contact.id, new_contact_date)

@then('the new contact list is equal to the old list with modified contact')
def verify_contact_modified(app, random_contact, new_contact_date, non_empty_contact_list, db, check_ui):
    old_contacts = non_empty_contact_list
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    index = old_contacts.index(random_contact)
    old_contacts[index] = new_contact_date
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)