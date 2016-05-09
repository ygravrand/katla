# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

from lxml import etree

from . import attributes
from .tag import tag


class RenderedTree(object):

    def __init__(self, tree):
        self.tree = tree

    def to_html_string(self):
        return etree.tostring(self.tree,
                              encoding='utf-8',
                              method='html',
                              pretty_print=True,
                              xml_declaration=False,
                              doctype=None)


base_attributes = {'style': attributes.style,
                   'className' : attributes.className}


class BaseRenderer(object):

    def render(self, comp):
        tree = etree.Element('html')
        tree.append(comp.render(self))
        return RenderedTree(tree)


class HTML5Renderer(BaseRenderer):

    # div = partial(etree.Element, 'div')
    span = tag('span', base_attributes)
    div = tag('div', base_attributes)
