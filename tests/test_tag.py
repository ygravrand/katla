# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

import unittest

from katla import attributes
from katla.tag import tag

from .utils import render_tag


class TestTag(unittest.TestCase):

    div = tag('div')
    span = tag('span', ('alt',))
    a = tag('a', {'className': attributes.className,
                  'style': attributes.style})

    def test_tags_and_text(self):
        d = self.div()
        self.assertEquals(render_tag(d), '<div></div>',
                          'Empty tag')

        d = self.div('Hello')
        self.assertEquals(render_tag(d), '<div>Hello</div>',
                          'Text only tag')

        d = self.div('Hello', ' ', 'World')
        self.assertEquals(render_tag(d), '<div>Hello World</div>',
                          'Tag with multiple concatenated texts')

        d = self.div('Hello', self.div('World'))
        self.assertEquals(render_tag(d), '<div>Hello<div>World</div></div>',
                          'Child tag')

        d = self.div('Hello', self.span(' World'), ' ')
        self.assertEquals(render_tag(d), '<div>Hello<span> World</span> </div>',
                          'Child tag and texts')

    def test_tag_attributes(self):
        d = self.div('Hello', ' ', 'World', title='Hello', alt='Hello')
        self.assertEquals(render_tag(d),
                          '<div alt="Hello" title="Hello">Hello World</div>',
                          'Multiple attributes')

        d = self.div('Hello', self.span('World', alt='World'), ' ', title="Hello")
        self.assertEquals(render_tag(d),
                          '<div title="Hello">Hello<span alt="World">World</span> </div>',
                          'Child with attributes')

        d = self.span('Hi', alt='World', title='World')
        self.assertEquals(render_tag(d), '<span alt="World">Hi</span>',
                          'Forbidden attributes are cleared')

        d = self.a('Link', className='link')
        self.assertEquals(render_tag(d),
                          '<a class="link">Link</a>',
                          'Attribute transform: className example')

        d = self.a('Link', style={'display': 'none',
                                  'text-decoration': 'underline'})
        self.assertEquals(render_tag(d),
                          '<a style="display: none; text-decoration: underline">Link</a>',
                          'Attribute transform: style example')


if __name__ == '__main__':
    unittest.main()
