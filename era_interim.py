#!/usr/bin/env python
import json
from pprint import pprint
from ecmwfapi import ECMWFDataServer


with open('properties.json') as json_data:
		config = json.load(json_data)
		print(config)

name = config["datasets"][0]["name"]


if name  == "ECMWF":
	ecmwf = config["datasets"][0]
	print(name)
	server = ECMWFDataServer()
	server.retrieve({
		'stream'    : "oper",
		'levtype'   : ecmwf["levtype"],
	    'param'     : "165.128/166.128/167.128",
	    'dataset'   : ecmwf["dataset"],
	    'step'      : ecmwf["step"],
	    'grid'      : ecmwf["grid"],
	    'time'      : ecmwf["time"],
	    'date'      : ecmwf["date"],
	    'type'      : ecmwf["type"],
	    'class'     : ecmwf["class"],
	    'target'    : ecmwf["target"]
	})
