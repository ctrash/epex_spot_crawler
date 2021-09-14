#! /bin/bash    
# Pfade anpassen
# Ausführbar machen CHMOD +x
cd /Users/beda/Documents/GitHub/epex_spot_crawler/env
source bin/activate
cd /Users/beda/Documents/GitHub/epex_spot_crawler/tutorial
# virtualenv is now active, which means your PATH has been modified.
# Don't try to run python from /usr/bin/python, just run "python" and
# let the PATH figure out which version to run (based on what your
# virtualenv has configured).
# scrapy crawl scrape-table -o data.csv
scrapy crawl scrape-table -o data/$(date +'%Y-%m-%d').json