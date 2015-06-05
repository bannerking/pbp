from flask_restful import reqparse
from service_resource import ARGS_LOG_SIZE
from service_list_resource import GET_ARGS_NUMBER, GET_ARGS_OFFSET, POST_ARGS_NAME, POST_ARGS_LOG_SIZE, POST_ARGS_OWNER_ID, DEFAULT_OWNER_ID

class ServiceParser():
    @staticmethod
    def parsePutParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_LOG_SIZE, type=int, required=True)
        args = parser.parse_args()
        return args

class ServiceListParser():
    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(GET_ARGS_NUMBER, type=int, default=None)
        parser.add_argument(GET_ARGS_OFFSET, type=int, default=None)
        args = parser.parse_args()
        return args

    @staticmethod
    def parsePostParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(POST_ARGS_NAME, type=str, required=True)
        parser.add_argument(POST_ARGS_LOG_SIZE, type=int, default=1048576)
        parser.add_argument(POST_ARGS_OWNER_ID, type=str, default=DEFAULT_OWNER_ID)
        args = parser.parse_args()
        return args