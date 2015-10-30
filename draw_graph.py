# -*- coding: utf-8 -*-
#!/usr/bin/env python

from graphviz import Digraph
import csv

def parse_csv(csv_file):
  csv_reader = csv.reader(open(csv_file), dialect=csv.excel)
  return {unicode(key, 'utf-8') for [_, key] in csv_reader}

def draw_graph(centroid, graph):
  g = Digraph('G', filename=centroid + '.pdf')
  g.edge('Hello', 'World')
  g.view()

def main():
  dataset = {
      'bialy' : parse_csv('data/bialy.csv'),
      'godlo' : parse_csv('data/godlo.csv'),
      'orzel' : parse_csv('data/orzel.csv'),
      'ptak' : parse_csv('data/ptak.csv')
  }
  for key in dataset:
    draw_graph(key, dataset)
  print dataset


if __name__ == '__main__':
    main()
