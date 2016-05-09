# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

def className(name, val):
    return 'class', val


def style(name, val):
    if isinstance(val, dict):
        return (name, '; '.join(['%s: %s' %
                                (attr_name, attr_value) for \
                                attr_name, attr_value in val.items()]))
    return name, val
