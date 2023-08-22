from boot_framework.default.config.ServletConfig import ServletConfig

configs = [
    ServletConfig
]

servlets_before = []
servlets_back = []

# TODO：后续可尝试通过自定义容器(可能是扩展list)的方式实现上述容器，使其更加定制化


__all__ = [
    'configs',
    'servlets_before',
    'servlets_back'
]
