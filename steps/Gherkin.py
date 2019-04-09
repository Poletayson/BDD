from behave import *
from Program import *

use_step_matcher("re")

result = ""

@given("I have my Image converter (?P<file_name>.+)")
def step_impl(context, file_name):
    """
    :type file_name: str
    :type context: behave.runner.Context
    """
    context.Converter = Example(file_name)
    pass



@when("I have opened image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = context.Converter.openFile()
    return context.result
    #raise NotImplementedError(u'STEP: When I have opened image')


@then("The result should be (?P<file_type>.+)")
def step_impl(context, file_type):
    """
    :type file_type: str
    :type context: behave.runner.Context
    """
    assert context.result == file_type
