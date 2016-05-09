# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

from katla.component import Component


class Root(Component):

    def render(self, r):
        my_div = r.div('Hello', className='super', style={'display':'block'})
        return r.div(my_div,
                     r.span('World', style={'display':'inline'}),
                     style='color:red')
