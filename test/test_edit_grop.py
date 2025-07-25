# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = db.get_group_list()
    group_edit = random.choice(old_groups)
    group = Group(name ="editn", header ="edith", footer ="editf")
    group.id = group_edit.id
    app.group.edit_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    index = old_groups.index(group_edit)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)