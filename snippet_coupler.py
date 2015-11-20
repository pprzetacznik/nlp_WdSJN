# -*- coding: utf-8 -*-
#!/usr/bin/env python

import csv

def parse_csv(csv_file):
  csv_reader = csv.reader(open(csv_file), dialect=csv.excel)
  return {unicode(key, 'utf-8'):value for [value, key] in csv_reader}

def main(snippets_filename, primary_word):
  dataset = {
      u'biały' : parse_csv('data/bialy.csv'),
      u'godło' : parse_csv('data/godlo.csv'),
      u'orzeł' : parse_csv('data/orzel.csv'),
      u'ptak' : parse_csv('data/ptak.csv')
  }
  with open(snippets_filename, 'r') as f:
    print f.readline()


if __name__ == '__main__':
    main()
  if len(sys.argv) == 3:
    snippets_filename = sys.argv[1]
    primary_word = unicode(sys.argv[2], 'utf-8')
    main(snippets_filename, primary_word)
  else:
    print "Usage:"
    print "  python -m snippet_coupler [file_with_snippets] [primary_word]"
    print "  eg. python -m snippet_coupler bialy.snippets.txt bialy"
