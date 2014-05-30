# -*- coding: utf-8 -*-

def name():
	return "topog4qgis"

def description():
	return "Experimental topographic tools for qGis"

def version():
	return "0.00"

def icon():
    return 'Icons/topog4qgis.png'

def qgisMinimumVersion():
	return "2.0"

def authorName():
	return "giuliano curti"

def classFactory(iface):
	from topog4qgis import topog4qgis
	return topog4qgis(iface)
	