# -*- coding: utf-8 -*-
#!/usr/bin/env python

import csv
import sys

def parse_csv(csv_file):
  csv_reader = csv.reader(open(csv_file), dialect=csv.excel)
  return {unicode(key, 'utf-8'):value for [value, key] in csv_reader}

def main(snippets_filename):
  dataset = {
      u'biały' : parse_csv('data/bialy.csv'),
      u'godło' : parse_csv('data/godlo.csv'),
      u'orzeł' : parse_csv('data/orzel.csv'),
      u'ptak' : parse_csv('data/ptak.csv')
  }
  with open(snippets_filename, 'r') as f:
    for line in f:
      unicode_line = unicode(line, 'utf-8')
      print unicode_line.encode('utf-8').rstrip()
      word_list = unicode_line.split()
      for key in dataset.keys():
        if key in word_list:
          for key2 in dataset[key]:
            if key2 in word_list:
              print_line = key + "===[" + dataset[key][key2] + "]==>" + key2
              print print_line.encode('utf-8')

if __name__ == '__main__':
  if len(sys.argv) >= 2:
    snippets_filename = sys.argv[1]
    main(snippets_filename)
  else:
    print "Usage:"
    print "  python -m snippet_coupler [file_with_snippets]"
    print "  eg. python -m snippet_coupler bialy.snippets.txt"
