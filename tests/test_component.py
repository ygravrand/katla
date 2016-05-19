# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

import unittest

from katla import transforms
from katla.component import Component
from katla.renderer import BaseRenderer, base_transforms
from katla.tag import tag

from .utils import render_tag


class A(Component):

    def render(self, r):
        return r.div('Hello', ' ', 'World ', className='greetings')


class B(Component):

    def render(self, r):
        return r.div('Wrapped: ', A(), A(), className='wrapper')


class Renderer(BaseRenderer):

    div = tag('div', base_transforms)


class TestComponent(unittest.TestCase):

    def test_simple(self):
        a = A()
        r = Renderer()
        self.assertEquals(render_tag(a.render(r)),
                          '<div class="greetings">Hello World </div>',
                          'Simple component rendering')

    def test_composition(self):
        b = B()
        r = Renderer()
        self.assertEquals(render_tag(b.render(r)),
                          '<div class="wrapper">Wrapped: <div class="greetings">Hello World </div><div class="greetings">Hello World </div></div>',
                          'Simple component rendering')
