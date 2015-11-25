#!/bin/bash

python -m parse_notes data/orzel.html | sort | uniq | sort -R | head -n 100 > data/orzel.snippets.txt
python -m parse_notes data/ptak.html | sort | uniq | sort -R | head -n 100 > data/ptak.snippets.txt
python -m parse_notes data/godlo.html | sort | uniq | sort -R | head -n 100 > data/godlo.snippets.txt
python -m parse_notes data/bialy.html | sort | uniq | sort -R | head -n 100 > data/bialy.snippets.txt
