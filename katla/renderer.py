# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

from lxml import etree

from . import transforms
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


base_transforms = {'style': transforms.style,
                   'className' : transforms.className}


class BaseRenderer(object):

    def render(self, comp):
        tree = etree.Element('html')
        tree.append(comp.render(self))
        return RenderedTree(tree)


class HTMLRenderer(BaseRenderer):

    # From list @ https://developer.mozilla.org/fr/docs/Web/HTML/Element

    html = tag('html')

    # Meta
    base = tag('base', base_transforms)
    head = tag('head', base_transforms)
    link = tag('link', base_transforms)
    meta = tag('meta', base_transforms)
    style = tag('style', base_transforms)
    title = tag('title', base_transforms)

    # Content
    address = tag('address', base_transforms)
    article = tag('article', base_transforms)
    body = tag('body', base_transforms)
    footer = tag('footer', base_transforms)
    header = tag('header', base_transforms)
    h1 = tag('h1', base_transforms)
    h2 = tag('h2', base_transforms)
    h3 = tag('h3', base_transforms)
    h4 = tag('h4', base_transforms)
    h5 = tag('h5', base_transforms)
    h6 = tag('h6', base_transforms)
    hgroup = tag('hgroup', base_transforms)
    nav = tag('nav', base_transforms)
    section = tag('section', base_transforms)

    # Text content
    blockquote = tag('blockquote', base_transforms)
    dd = tag('dd', base_transforms)
    div = tag('div', base_transforms)
    dl = tag('dl', base_transforms)
    dt = tag('dt', base_transforms)
    figcaption = tag('figcaption', base_transforms)
    figure = tag('figure', base_transforms)
    hr = tag('hr', base_transforms)
    li = tag('li', base_transforms)
    main = tag('main', base_transforms)
    ol = tag('ol', base_transforms)
    p = tag('p', base_transforms)
    pre = tag('pre', base_transforms)
    ul = tag('ul', base_transforms)

    # Text semantics
    a = tag('a', base_transforms)
    abbr = tag('abbr', base_transforms)
    b = tag('b', base_transforms)
    bdi = tag('bdi', base_transforms)
    bdo = tag('bdo', base_transforms)
    br = tag('br', base_transforms)
    cite = tag('cite', base_transforms)
    code = tag('code', base_transforms)
    data = tag('data', base_transforms)
    dfn = tag('dfn', base_transforms)
    em = tag('em', base_transforms)
    i = tag('i', base_transforms)
    kbd = tag('kbd', base_transforms)
    mark = tag('mark', base_transforms)
    q = tag('q', base_transforms)
    rp = tag('rp', base_transforms)
    rt = tag('rt', base_transforms)
    ruby = tag('ruby', base_transforms)
    s = tag('s', base_transforms)
    samp = tag('samp', base_transforms)
    small = tag('small', base_transforms)
    span = tag('span', base_transforms)
    strong = tag('strong', base_transforms)
    sub = tag('sub', base_transforms)
    sup = tag('sup', base_transforms)
    time = tag('time', base_transforms)
    u = tag('u', base_transforms)
    var = tag('var', base_transforms)
    wbr = tag('wbr', base_transforms)

    # Image and multimedia
    area = tag('area', base_transforms)
    audio = tag('audio', base_transforms)
    img = tag('img', base_transforms)
    map_ = tag('map', base_transforms)
    track = tag('track', base_transforms)
    video = tag('video', base_transforms)

    # Embedded content
    embed = tag('embed', base_transforms)
    iframe = tag('iframe', base_transforms)
    object = tag('object', base_transforms)
    param = tag('param', base_transforms)
    source = tag('source', base_transforms)

    # Scripts
    canvas = tag('canvas', base_transforms)
    script = tag('script', base_transforms)
    noscript = tag('noscript', base_transforms)

    # Edition
    del_ = tag('del', base_transforms)
    ins = tag('ins', base_transforms)

    # Tables
    caption = tag('caption', base_transforms)
    col = tag('col', base_transforms)
    colgroup = tag('colgroup', base_transforms)
    table = tag('table', base_transforms)
    tbody = tag('tbody', base_transforms)
    td = tag('td', base_transforms)
    tfoot = tag('tfoot', base_transforms)
    th = tag('th', base_transforms)
    thead = tag('thead', base_transforms)
    tr = tag('tr', base_transforms)

    # Forms
    button = tag('button', base_transforms)
    datalist = tag('datalist', base_transforms)
    colgroup = tag('colgroup', base_transforms)
    fieldset = tag('fieldset', base_transforms)
    form = tag('form', base_transforms)
    input_ = tag('input', base_transforms)
    keygen = tag('keygen', base_transforms)
    label = tag('label', base_transforms)
    legend = tag('legend', base_transforms)
    meter = tag('meter', base_transforms)
    optgroup = tag('optgroup', base_transforms)
    option = tag('option', base_transforms)
    output = tag('output', base_transforms)
    progress = tag('progress', base_transforms)
    select = tag('select', base_transforms)
    textarea = tag('textarea', base_transforms)

    # Interactive
    details = tag('details', base_transforms)
    dialog = tag('dialog', base_transforms)
    menu = tag('menu', base_transforms)
    menuitem = tag('menuitem', base_transforms)
    summary = tag('summary', base_transforms)
