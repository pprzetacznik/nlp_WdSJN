# -*- coding: utf-8 -*-
#!/usr/bin/env python

import re
import sys

allowed_set = {
  u'fin',
  # u'bedzie',
  # u'aglt',
  u'praet',
  u'impt',
  # u'imps',
  # u'inf',
  # u'pcon',
  # u'pant',
  u'ger',
  # u'pact',
  # u'ppas'
}

filter_set = {
  u'.',
  u',',
  u':',
  u';',
  u'!',
  u'-',
  u'–',
  u'?',
  u')',
  u'(',
  u'\"',
  u'„',
  u'”',
  u'“',
  u'[',
  u']',
  u'…',
  u'&',
}

def parse_side(side_tuple):
  left_data = re.findall(ur"([^\s]+?) \[(.*?)\]", side_tuple, re.DOTALL)
  left_data = [(key, value.split(':')) for (key, value) in left_data]
  return left_data

def filter_special_characters(filter_side_fun):
  def helper(snippet_list):
    new_snippet_list = filter_side_fun(snippet_list)
    new_snippet_list = [item for item in new_snippet_list if not any(x in item[0] for x in filter_set)] if new_snippet_list is not None else None
    return new_snippet_list
  return helper

@filter_special_characters
def filter_left(side_list):
  new_side_list = None
  for i in xrange(len(side_list)-1, 0, -1):
    classes = side_list[i][1]
    if bool(allowed_set & set(classes)):
      new_side_list = side_list[i:]
      break
  return new_side_list

@filter_special_characters
def filter_right(side_list):
  new_side_list = None
  for i in xrange(len(side_list)):
    classes = side_list[i][1]
    if bool(allowed_set & set(classes)):
      new_side_list = side_list[:i+1]
      break
  return new_side_list

def parse_note_to_snippet_list(note_tuple):
  left = filter_left(parse_side(note_tuple[0]))
  right = filter_right(parse_side(note_tuple[3]))
  return [left, [(note_tuple[1], note_tuple[2].split(':'))], right] if (left and right) else None

def parse_note(filename):
  with open(filename, 'r') as f:
    data = unicode(f.read(), "utf-8")
  data = re.findall(ur"<tr><td[^>]*?>\s?(.*?)</td><td[^>]*?><strong>\s?(.*?)</strong>\s?\[(.*?)\]</td><td[^>]*?>\s?(.*?)</td></tr>", data, re.DOTALL)
  snippet_list = map(parse_note_to_snippet_list, data)
  snippet_list = [x for x in snippet_list if x is not None]
  return snippet_list

def print_snippet_list(snippet_list, seek_function = lambda x:x[0]):
  for snippet in snippet_list:
    whole_set = [seek_function(i) for side in snippet for i in side]
    print u' '.join(whole_set).encode('utf-8')

def main(filename):
  print_snippet_list(parse_note(filename))
  # print_snippet_list(parse_note(filename), seek_function = lambda x: x[1][0])
  # print_snippet_list(parse_note(filename), seek_function = lambda x: x[0] + ":" + x[1][1] if len(x[1]) >= 2 else x[0])

if __name__ == '__main__':
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    main(filename)
  else:
    print "Usage:"
    print "  python -m parse_notes [filename.html]"
    print "  eg. python -m parse_notes data/orzel.html"
