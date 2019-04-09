from behave import *
from Program import *

use_step_matcher("re")

result = ""
size = (0,0)

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


@step("I have saved image (?P<file_name>.+)")
def step_impl(context, file_name):
    """
    :type file_name: str
    :type context: behave.runner.Context
    """
    context.result = context.Converter.saveFile(file_name)
    return context.result


@step("I have resized image by W")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.size = context.Converter.resiseW ()
    return context.size


@then("The size should be (?P<size>.+)")
def step_impl(context, size):
    """
    :type size: str
    :type context: behave.runner.Context
    """
    assert context.size == size