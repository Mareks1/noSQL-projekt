#!/usr/bin/python

import codecs
with codecs.open('National_Statistics_Postcode_Lookup_Latest_Centroids.csv','r',encoding='windows-1250') as f:
    text = f.read()
with codecs.open('map.csv','w',encoding='windows-1250') as f:
	f.write(text[3:])