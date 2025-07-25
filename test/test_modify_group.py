# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = db.get_group_list()
    group_mode = random.choice(old_groups)
    group = Group(name="New group")
    group.id = group_mode.id
    app.group.modify_group_by_id(group.id,group)
    assert len(old_groups)  == app.group.count()
    new_groups = db.get_group_list()
    index = old_groups.index(group_mode)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", header ="test", footer ="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
