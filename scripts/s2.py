#!/usr/bin/python

import codecs
with codecs.open('NHS_Postcode_Directory_Latest_Centroids.csv','r',encoding='windows-1250') as f:
    text = f.read()
with codecs.open('map.csv','w',encoding='windows-1250') as f:
	f.write(text[290:])