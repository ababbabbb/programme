import importlib
import inspect
from functools import partial

from find_func_decorator import MethodTestSide


module = importlib.machinery.SourceFileLoader(
                    'find_func_tested', '/home/bct/projects/programe/topics/backend/netapis/netapi_flask/flask_boot/test/find_func_tested.py'
                ).load_module()

# module.TargetCls()
# print(module.func_target)
instances = [
                    cls[1](*cls[1].test_args) for cls in inspect.getmembers(module) if inspect.isclass(cls[1]) and any(
                        value for value in cls[1].__dict__.values() if isinstance(value, MethodTestSide)
                    )
                ]

# methods = []
# for instance in instances:
#     methods += [getattr(instance, m) for m in dir(instance) if inspect.ismethod(getattr(instance, m))]

methods = [getattr(instance, m) for instance in instances for m in dir(instance) if isinstance(getattr(instance, m), partial)]
a = [func[1] for func in inspect.getmembers(module) if inspect.isfunction(func[1])]
for name, obj in getattr(module, 'globals')().items():
    print(name)

# [module.TargetCls.__dict__[attr_key] for attr_key in module.TargetCls.__dict__.keys() if isinstance(module.TargetCls.__dict__[attr_key], module.CustomDecorator)]
# [value for value in inspect.getmembers(module)[0][1].__dict__.values() if isinstance(value, module.TestSide)]
