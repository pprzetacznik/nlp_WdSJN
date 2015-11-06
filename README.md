WdSJN
================

## Draw graphs

The lecture is a continuation of the lecture "Natural Language Processing." It is an introduction to the issues of describing semantics and shows the importance of the semantic motivation of natural language processing algorithms.

Run:
```Bash
$ git clone https://github.com/pprzetacznik/WdSJN.git
$ cd WdSJN
$ mkvirtualenv WdSJN
(WdSJN) $ pip install -r requirements.txt
(WdSJN) $ python draw_graph.py
```

## Create snippets

```Bash
(WdSJN) $ python parse_notes.py data/bialy.html False | uniq | head -n 100
```
