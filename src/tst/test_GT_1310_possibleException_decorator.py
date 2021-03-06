from unittest import TestCase
from service_not_exist_exception import ServiceNotExistException
from possible_exception import possibleException
TEST_VALID_EXCEPTION = ServiceNotExistException
TEST_NOT_VALID_EXCEPTION = ArithmeticError
TEST_VALID_TUPLE = ('Service not found', 404)
TEST_NOT_VALID_EXCEPTION_STRING = 'This is not valid exception'


@possibleException
def funcForTesting(Exc):
    raise Exc(TEST_NOT_VALID_EXCEPTION_STRING)


class TestPossibleExceptionDecorator(TestCase):

    def testPossibleExceptionDecorator(self):
        self.assertEqual(
            funcForTesting(TEST_VALID_EXCEPTION),
            TEST_VALID_TUPLE)
        with self.assertRaises(TEST_NOT_VALID_EXCEPTION) as context:
            funcForTesting(TEST_NOT_VALID_EXCEPTION)
        self.assertTrue(TEST_NOT_VALID_EXCEPTION_STRING in context.exception)
