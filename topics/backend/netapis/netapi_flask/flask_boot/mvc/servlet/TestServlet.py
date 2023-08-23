from boot_framework.Scanner.TargetBasic import BeforeServlet


class TestServlet(BeforeServlet):

    def __call__(self, environ, start_response):
        print('拦截器执行了，意味着配置、拦截器成功装载到框架中，且拦截器中间件生效了')
