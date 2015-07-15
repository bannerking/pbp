from tests_resource import TestsResource
from point_resource import PointResource
from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from service_list_resource import ServiceListResource
from status_resource import StatusResource
from config_reader import getInstancePrefix
from log_resource import LogResource
from debug_info_resource import DebugInfoResource
from flask import make_response
from bson import json_util
from channels_list_resource import ChannelsListResource
from channel_resource import ChannelResource
from point_list_resource import PointListResource
from os import urandom
from logout_resource import LogoutResource
from login_resource import LoginResource
from debug_login_resource import DebugLoginResource

def output_json(obj, code, headers=None):
    if isinstance(obj, str) == True:
        return make_response(obj, code)
    return make_response(json_util.dumps(obj), code)

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
app = Flask(__name__)
app.secret_key = urandom(32)
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS

def getPathWithPrefix(str):
    path = '/'+getInstancePrefix()+str
    return path

api.add_resource(ServiceResource, getPathWithPrefix('/service/<string:serviceName>'))
api.add_resource(StatusResource, getPathWithPrefix('/status'))
api.add_resource(ServiceListResource, getPathWithPrefix('/service'))
api.add_resource(DebugInfoResource, getPathWithPrefix('/debug_info'))
api.add_resource(LogResource, getPathWithPrefix('/service/<string:serviceName>/log'),
                              getPathWithPrefix('/log'))
api.add_resource(ChannelsListResource, getPathWithPrefix('/service/<string:serviceName>/channel'))
api.add_resource(ChannelResource, getPathWithPrefix('/service/<string:serviceName>/channel/<string:channelId>'))

api.add_resource(PointResource, getPathWithPrefix('/service/<string:serviceName>/point/<string:pointId>'))
api.add_resource(PointListResource, getPathWithPrefix('/service/<string:serviceName>/point'))

api.add_resource(LogoutResource, getPathWithPrefix('/logout'))
api.add_resource(LoginResource, getPathWithPrefix('/login'))
api.add_resource(DebugLoginResource, getPathWithPrefix('/debug_login'))

api.add_resource(TestsResource, getPathWithPrefix('/tests'))
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
