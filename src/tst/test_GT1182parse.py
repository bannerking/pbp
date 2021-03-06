#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from flask import Flask
import json
from log_parsers import LogParser
from date_utils import dateDeserialiser


NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
DATE_FROM = 'date_from'
DATE_FROM_VALUE = '1970-06-15T18:00:00.000000'
DATE_TO = 'date_to'
DATE_TO_VALUE = '2015-06-15T17:00:00.000000'


CORRECT_ARGS = NUMBER + '=' + unicode(NUMBER_VALUE) + \
    '&' + OFFSET + '=' + unicode(OFFSET_VALUE) + \
    '&' + DATE_FROM + '=' + unicode(DATE_FROM_VALUE) + \
    '&' + DATE_TO + '=' + unicode(DATE_TO_VALUE)
INCORRECT_ARGS = 'incorect='
app = Flask(__name__)


class TestParserLogResource(TestCase):

    def testGetParser(self):
        with app.test_request_context('/?' + CORRECT_ARGS):
            args = LogParser.parseGetParameters()
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)
            loadedDatetime_from = json.loads(
                args[DATE_FROM], object_hook=dateDeserialiser(
                    args, DATE_FROM))
            self.assertEquals(loadedDatetime_from, DATE_FROM_VALUE)
            loadedDatetime_to = json.loads(
                args[DATE_TO], object_hook=dateDeserialiser(
                    args, DATE_TO))
            self.assertEquals(loadedDatetime_to, DATE_TO_VALUE)

        with app.test_request_context('/?' + INCORRECT_ARGS):
            args = LogParser.parseGetParameters()
            self.assertIsNone(args.get(OFFSET))
            self.assertIsNone(args.get(NUMBER))
            self.assertIsNone(args.get(loadedDatetime_from))
            self.assertIsNone(args.get(loadedDatetime_to))
