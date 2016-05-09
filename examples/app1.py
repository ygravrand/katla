# -*- coding: utf-8 -*-
"""
    katla
    :copyright: (c) 2016 by Yann Gravrand.
    :license: BSD, see LICENSE for more details.
"""

from werkzeug.wrappers import Request, Response

from katla.renderer import HTML5Renderer

from app1_root import Root


class App(object):

    def __init__(self):
        self.root = Root()

    def dispatch_request(self, request):
        res = HTML5Renderer().render(self.root)
        return Response(res.to_html_string(), mimetype='text/html')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app():
    return App()


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
