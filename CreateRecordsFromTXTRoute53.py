#!/usr/bin/env python

import boto.route53
import time
from sys import argv

script, dominio, destino, tipo, fname = argv

conn = boto.connect_route53()
zone = conn.get_zone(dominio)

for line in open(fname):
    registro = line.rstrip('\n')
    #print registro
    route53 = zone.find_records(registro, tipo, desired=9, all=False, identifier=None)
    print route53
    if route53 == None:
    	if tipo != "NS":
			print '%s (%s) %s -> %s' % ('Creando registro', tipo, registro, dominio)
			result = zone.add_record(tipo, registro, destino)
	print '====='
			#print result
			#break
