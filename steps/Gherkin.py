from behave import *

use_step_matcher("re")

result = ""

@given("I have my Image converter (?P<file_name>.+)")
def step_impl(context, file_name):
    """
    :type file_name: str
    :type context: behave.runner.Context
    """
    context.Converter = Example(file_name)
    raise NotImplementedError(u'STEP: Given I have my Image converter whith file \'1.jpg\'')


@when("I have opened image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.Converter.openFile()
    #raise NotImplementedError(u'STEP: When I have opened image')


@then("The result should be (?P<file_type>.+)")
def step_impl(context, file_type):
    """
    :type file_type: str
    :type context: behave.runner.Context
    """
    assert result == file_type
    raise NotImplementedError(u'STEP: Then The result should be jpg')