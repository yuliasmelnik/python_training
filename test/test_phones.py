import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_phones_from_view_page == merge_phones_like_on_view_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_phones_like_on_view_page(contact):
    if contact.homephone == "":
        homephone_for_view_page = ""
    else:
        homephone_for_view_page = "%s%s" % ("H: ", contact.homephone)
    if contact.mobilephone == "":
        mobilephone_for_view_page = ""
    else:
        mobilephone_for_view_page = "%s%s" % ("M: ", contact.mobilephone)
    if contact.workphone == "":
        workphone_for_view_page = ""
    else:
        workphone_for_view_page = "%s%s" % ("W: ", contact.workphone)
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [homephone_for_view_page, mobilephone_for_view_page, workphone_for_view_page])))