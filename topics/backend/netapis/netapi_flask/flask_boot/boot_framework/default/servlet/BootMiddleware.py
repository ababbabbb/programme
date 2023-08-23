from boot_framework.ConfigContainer import servlets_before, servlets_back


class BootMiddleware:

    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        # 请求前拦截器
        for servlet_bf in servlets_before:
            servlet_bf(environ, start_response)

        response = self.old_wsgi_app(environ, start_response)

        # 请求后拦截器
        for servlet_bk in servlets_back:
            response = servlet_bk(response)

        return response
