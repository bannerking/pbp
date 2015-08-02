#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath
PLUGINS_DIR_NAME = 'plugins'
sys.path.append(PLUGINS_DIR_NAME)

import imp
from url_routines import getPluginUrl

GET_PLUGIN_RESOURCES = 'getPluginResources'
EXCEPT_ERROR_TEXT = 'Error occurred while loading the plugin '

def getPluginList():
    pluginsDirList = os.listdir(PLUGINS_DIR_NAME)
    pluginsList = []
    for i in pluginsDirList:
        if os.path.isdir(joinpath(PLUGINS_DIR_NAME,i)):
            pluginsList.append(i)
    return pluginsList

def enablePlugin(api, pluginName):
    loadMain = 'plugins.' + pluginName + '.main'
    loadModule = __import__ (loadMain, globals(), locals(), [GET_PLUGIN_RESOURCES], -1)
    try:
        pluginResourcesDict = loadModule.getPluginResources()
        for pluginResource in pluginResourcesDict:
            print getPluginUrl(pluginResource, pluginName)
            api.add_resource(pluginResourcesDict[pluginResource], getPluginUrl(pluginResource, pluginName))
    except Exception as e:
        print EXCEPT_ERROR_TEXT + pluginName
        print e

def getPluginState(pluginName):
    return True

def isPluginEnabled(pluginName, api):
    return True