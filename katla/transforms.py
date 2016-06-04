# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.

    The ``transforms`` module defines usual transforms on attributes,
    e.g. "className" --> "class"
"""

from . import styles

def className(name, val):
    return 'class', val


def style(name, val):
    if isinstance(val, dict):
        return name, styles.to_string(val)
    return name, val
