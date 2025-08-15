Feature: Contact tests
  Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <company>, <title>, <address>, <homephone>, <mobilephone>, <workphone>, <email>, <email2>, <email3>, <homepage>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname | middlename | lastname | nickname | company | title | address | homephone | mobilephone | workphone | email | email2 | email3 | homepage |
    | firstname1 | middlename1 | lastname1 | nickname1 | company1 | title1 | address1 | homephone1 | mobilephone1 | workphone1 | email1 | email21 | email31 | homepage1 |
    | firstname2 | middlename2 | lastname2 | nickname2 | company2 | title2 | address2 | homephone2 | mobilephone2 | workphone2 | email2 | email22 | email32 | homepage2 |

  Scenario Outline: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the deleted contact

  Scenario Outline: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a modify contact with new <firstname>, <middlename>, <lastname>, <nickname>, <company>, <title>, <address>, <homephone>, <mobilephone>, <workphone>, <email>, <email2>, <email3>, <homepage>
    When I modify the contact from the list
    Then the new contact list is equal to the old list with modified contact

     Examples:
    | firstname | middlename | lastname | nickname | company | title | address | homephone | mobilephone | workphone | email | email2 | email3 | homepage |
    | test | test | test | test | test | test | test | test | test | test | test | test | test | test |