# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

from lxml import etree

from .component import Component


class Tag(object):
    """Tag is the base class to render HTML tags"""

    def __init__(self, name, attrs_transforms):
        """Init a tag.
           :param name: Name of the tag to use in output
           :param attrs_transforms: either:
           - a dictionary of {``attribute_name``:``attribute_transform``},
             each ``attribute_transform`` being a function:
               :param name: Original attribute name
               :param value: Original attribute value
               :return: A (``name``, ``value``) tuple with the new attribute name and value
           - a list of allowed attribute names
           - None to apply no transform and disable restriction on attribute names
        """
        self._name = name
        self._attrs_transforms = None
        if attrs_transforms is None:
            self._allowed_attrs = None
        elif isinstance(attrs_transforms, dict):
            self._allowed_attrs = self._attrs_transforms = attrs_transforms
        else:
            self._allowed_attrs = attrs_transforms

    def __call__(self, *children, **attrs):
        attrs = self._handle_attrs(attrs)
        res = etree.Element(self._name, **attrs)
        self._extend(res, children)
        return res

    def __get__(self, renderer, *args, **kw):
        self._renderer = renderer
        return self

    def _set_text(self, tree, text):
        if len(tree) != 0:
            tree[-1].tail = (tree[-1].tail or '') + text
        else:
            tree.text = (tree.text or '') + text

    def _extend(self, tree, children):
        for child in children:
            if isinstance(child, basestring):
                self._set_text(tree, child)
            # TODO comment case
            elif isinstance(child, Component):
                res = child.render(self._renderer)
                if res is not None:
                    tree.append(res)
            else:
                tree.append(child)

    def _handle_attrs(self, attrs):
        res = {}
        for name, value in attrs.items():
            if self._allowed_attrs is None:
                res[name] = value
            elif name in self._allowed_attrs:
                if self._attrs_transforms is not None:
                    new_name, new_value = self._attrs_transforms[name](name, value)
                    res[new_name] = new_value
                else:
                    res[name] = value
        return res


def tag(name, attrs_transforms=None):
    """Creates a ``Tag``, see ``Tag:__init__`` for documentation"""
    return Tag(name, attrs_transforms)
