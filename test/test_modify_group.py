# -*- coding: utf-8 -*-
import allure
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group_mode = random.choice(old_groups)
    with allure.step('Given a modify group with new <name>, <header> and <footer>'):
        group = Group(name="New group")
        group.id = group_mode.id
    with allure.step('When I modify the group from the list'):
        app.group.modify_group_by_id(group.id,group)
    with allure.step('Then the new group list is equal to the old list with modified group'):
        assert len(old_groups)  == app.group.count()
        new_groups = db.get_group_list()
        index = old_groups.index(group_mode)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", header ="test", footer ="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
