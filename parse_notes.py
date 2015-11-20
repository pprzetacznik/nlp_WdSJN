# -*- coding: utf-8 -*-
#!/usr/bin/env python

import re
import sys
from lib.clp import CLP

clp = CLP()

def parse_side(side_tuple):
  left_data = re.findall(ur"([^\s]+?) \[.*?\]", side_tuple, re.DOTALL)
  return [key for key in left_data if clp.rec(key) and clp.label(clp.rec(key)[0])[0] != 'G']

def is_boundary_word(word):
  id = clp.rec(word)[0]
  if clp.label(id)[0] != 'C':
    return False
  if clp.bform(id) == u'być':
    return False
  if clp.vec(id, word)[0] in [1, 13, 14, 45, 46, 47]:
    return False
  return True

def bform(word_list):
  return [clp.bform(clp.rec(key)[0]) for key in word_list] if word_list else word_list

def filter_left(side_list):
  new_side_list = None
  for i in xrange(len(side_list)-1, 0, -1):
    if is_boundary_word(side_list[i]):
      new_side_list = side_list[i:]
      break
  return new_side_list

def filter_right(side_list):
  new_side_list = None
  for i in xrange(len(side_list)):
    if is_boundary_word(side_list[i]):
      new_side_list = side_list[:i+1]
      break
  return new_side_list

def parse_note_to_snippet_list(note_tuple):
  left = bform(filter_left(parse_side(note_tuple[0])))
  right = bform(filter_right(parse_side(note_tuple[3])))
  return [left, [note_tuple[1]], right] if (left and right) else None

def parse_note(filename):
  with open(filename, 'r') as f:
    data = unicode(f.read(), "utf-8")
  data = re.findall(ur"<tr><td[^>]*?>\s?(.*?)</td><td[^>]*?><strong>\s?(.*?)</strong>\s?\[(.*?)\]</td><td[^>]*?>\s?(.*?)</td></tr>", data, re.DOTALL)
  snippet_list = map(parse_note_to_snippet_list, data)
  snippet_list = [x for x in snippet_list if x is not None]
  return snippet_list

def print_snippet_list(snippet_list):
  for snippet in snippet_list:
    whole_set = [i for side in snippet for i in side]
    print u' '.join(whole_set).encode('utf-8')

def main(filename):
  print_snippet_list(parse_note(filename))

if __name__ == '__main__':
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    main(filename)
  else:
    print "Usage:"
    print "  python -m parse_notes [filename.html]"
    print "  eg. python -m parse_notes data/orzel.html"
