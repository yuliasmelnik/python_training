from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHalper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_contact_for_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form (self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("middlename", contact.middlename)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("nickname", contact.nickname)
        self.change_field_value_contact("title", contact.title)
        self.change_field_value_contact("company", contact.company)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("home", contact.homephone)
        self.change_field_value_contact("mobile", contact.mobilephone)
        self.change_field_value_contact("work", contact.workphone)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("email2", contact.email2)
        self.change_field_value_contact("email3", contact.email3)
        self.change_field_value_contact("homepage", contact.homepage)
        #self.change_field_value_contact_for_select("bday", contact.bday)
        #self.change_field_value_contact_for_select("bmonth", contact.bmonth)
        #self.change_field_value_contact("byear", contact.byear)
        #self.change_field_value_contact_for_select("aday", contact.aday)
        #self.change_field_value_contact_for_select("amonth", contact.amonth)
        #self.change_field_value_contact("ayear", contact.ayear)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector ("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_date):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # edit contact form
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr['str(index + 2)']/td[8]/a/img")[
            index].click()
        self.fill_contact_form(new_contact_date)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_date):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # edit contact form
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' %(id)).click()
        self.fill_contact_form(new_contact_date)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_date):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr['str(index + 2)']/td[8]/a/img")[
            index].click()
        # fill contact form
        self.fill_contact_form(new_contact_date)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_date):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # open modification form
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' %(id)).click()
        # fill contact form
        self.fill_contact_form(new_contact_date)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def return_to_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id = id, lastname = lastname, firstname = firstname, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        all_phones = re.search("\n{2}((.*\n){,4})\n{1}", text).group(1)
        return Contact(all_phones_from_view_page=all_phones.strip())
