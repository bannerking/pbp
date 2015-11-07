from flask_restful import Resource
from flask import render_template
from flask import make_response
from config_reader import getInstancePrefix


class MacrosTestsResource(Resource):

    def get(self):
        return make_response(
            render_template(
                'macros_test.html',
                instancePrefix=getInstancePrefix()))
