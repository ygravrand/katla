# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""


def from_string(s):
    """Returns a dictionary of styles from a styles string
       :param s: Input string, eg. "display:none; text-align: right"
       :return: A dictionary of styles {declaration: value}
    """
    declarations = [decl.strip().split(':') for decl in s.split(';')]
    return {name.strip(): value.strip() for (name, value) in declarations}


def to_string(d):
    """Returns a string from a dictionary of styles
       :param s: Styles dictionary, eg. {"display": "none", "text-align": "right"}
       :return: A styles string
    """
    return '; '.join(['%s: %s' %
                      (name, value) for name, value in d.items()])
