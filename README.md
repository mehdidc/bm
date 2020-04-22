# bm

Simple bookmark manager that uses SQLite to store the links.
It supports:

- searching for urls in the database based on keywords (bm ls --help and bm recommend --help 
for more details)
- tagging the urls (bm tag --help)
- opening the urls in the browser (bm ls --help|grep open-in-browser)
- caching the content of the urls in PDFs and opening the PDFs (bm ls --help|grep open-pdf)
- exporting the database to CSV and HTML

# Usage Examples

## Add link

```bash

bm a "https://www.sqlite.org/docs.html"

bm a "https://www.sqlite.org/docs.html" --desc='sqlite documentation' 

bm a "https://www.sqlite.org/docs.html" --tags='database documentation reference' # 3 tags, "database", "documentation", and "reference"
```

## List/Search for Links

```bash
bm ls # display all

bm ls 'health insurance' #look for "health" and "insurance" (both should be present) in urls, titles, tags and description.

bm ls 'health insurance' --query-mode=or # look for either "health" OR "insurance" (any should be present) in urls, titles, tags, and description)

bm ls 'health insurance' --nb=5 # show 5 first (sorted by time)

bm ls 'health insurance' --nb=10 --sort-by=views # show 10 first (sorted by views desc)

bm ls 'health insurance' --nb=10 --sort-by=views --order=asc #  show 10 first (sorted by views asc)

bm ls --random #show urls in random order

bm ls --random --nb=5 # show 5 randomly chosen urls

bm ls 'health insurance' --random --nb=5 # show 5 randomly chosen urls which contain they keywords "health" and "insurance"

bm ls --id=142 #look for a specfic url (each url has an id)

bm ls --tags='video' #look for all urls tagged as "video"

bm ls --trim=false  #do not trim the urls (trimming is used to constrain the urls to be in one line)

bm ls --id=142 --open-in-browser #open a specific url in the browser

bm ls 'machine learning' --open-in-browser --open-all # open all machine learning related urls in browser

bm ls 'machine learning' --open-pdf --open-all # open all machine learning  related urls in pdf (cached version)
```

## Remove link(s)

```bash
bm rm --id=143 #remove a specific url

bm rm 'health insurance' #remove all urls which match the keywords "health" and "insurance"
```
# Export to csv or HTML or Markdown

```bash
bm export-csv out.csv

bm export-html out.html

bm export-markdown out.md
```

# Export to pocket


```bash
bm export-pocket consumer_key access_token
```
