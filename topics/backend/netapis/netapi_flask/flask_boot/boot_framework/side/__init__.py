"""
该模块其实主要意味着手脚架侧面结合的实现，主要通过aop的方式实现，
由于aop接管了约定的方法，导致侧面可以由原先横向管理某一个方法或函数直接变为了影响整个系统的纵向侧面
同样也意味着，倘若不指定侧面，将导致侧面的配置在该处不生效
"""
from boot_framework.side.PluginSide import PluginSide
