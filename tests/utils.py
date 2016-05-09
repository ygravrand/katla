# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

from lxml import etree


def render_tag(tag):
    res = etree.tostring(tag,
                         encoding='utf-8',
                         method='html',
                         pretty_print=False,
                         xml_declaration=False,
                         doctype=None)
    print res
    return res
