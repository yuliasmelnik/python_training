*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixture
Suite Teardown  Destroy Fixture

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  middlename1  lastname1  nickname1  company1  title1  address1  homephone1  mobilephone1  workphone1  email1  email21  email31  homepage1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${contact_data}=  Modify Data Contact  firstnamenew  middlenamenew  lastnamenew  nicknamenew  companynew  titlenew  addressnew  homephonenew  mobilephonenew  workphonenew  emailnew  email2new  email3new  homepagenew
    Modify Contact  ${contact}  ${contact_data}
    ${new_list}=  Get Contact List
    Set List Value   ${old_list}  ${index}  ${contact_data}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}