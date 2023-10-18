from find_func_decorator import MethodTestSide, FunctionTestSide


@FunctionTestSide
def func_target():

    return '10010'


class TargetCls:
    test_args = ()

    @MethodTestSide
    def func(self):

        return '10086'

# print(__file__)
