# Phantomas Metrics Collector

Collects frontend performance metrics for a list of configured sites and writes them to a list of json files.

In order to use it, 

1. Install [phantomas](https://github.com/macbre/phantomas)
 
   ```bash
   npm install --global phantomas
   ```
   
2. Copy config.json.example to config.json and adapt the example:
   
   ```json
   {
       "output-base-dir": "/Users/mloetzsch/web-performance-stats/",
       "phantomas-binary": "/opt/local/bin/phantomas",
       "sites": {
           "zalando.de": {
               "start page": "https://www.zalando.de",
               "catalog page": "https://www.zalando.de/damenbekleidung/",
               "product detail page": "https://www.zalando.de/adidas-originals-sneaker-core-black-ad115b023-q11.html"
           },
           "aboutyou.de": {
               "start page": "http://www.aboutyou.de/",
               "catalog page": "http://www.aboutyou.de/frauen/bekleidung",
               "product detail page": "http://www.aboutyou.de/p/marc-opolo/ledersandale-1861142"
           }
       }
   }
   ```
   
   
3. Run main.py frequently (e.g. every hour)

   ```
   ➜ phantomas-metrics-collector git:(master) python main.py                                        
   fetching zalando.de start page (https://www.zalando.de)
   fetching zalando.de catalog page (https://www.zalando.de/damenbekleidung/)
   fetching zalando.de product detail page (https://www.zalando.de/adidas-originals-sneaker-core-black-ad115b023-q11.html)
   fetching aboutyou.de start page (http://www.aboutyou.de/)
   fetching aboutyou.de catalog page (http://www.aboutyou.de/frauen/bekleidung)
   fetching aboutyou.de product detail page (http://www.aboutyou.de/p/marc-opolo/ledersandale-1861142)
   ```


4. Find the results under the configured output directory, with sub folders for year/ month/ day/ /hour-minute

   ```
   ➜  ~  find web-performance-stats 
   web-performance-stats
   web-performance-stats/2015
   web-performance-stats/2015/02
   web-performance-stats/2015/02/18
   web-performance-stats/2015/02/18/phantomas-metrics
   web-performance-stats/2015/02/18/phantomas-metrics/10-45
   web-performance-stats/2015/02/18/phantomas-metrics/10-45/aboutyou.de-catalog page.json
   web-performance-stats/2015/02/18/phantomas-metrics/10-45/aboutyou.de-product detail page.json
   web-performance-stats/2015/02/18/phantomas-metrics/10-45/aboutyou.de-start page.json
   web-performance-stats/2015/02/18/phantomas-metrics/10-45/zalando.de-catalog page.json
   web-performance-stats/2015/02/18/phantomas-metrics/10-45/zalando.de-product detail page.json
   web-performance-stats/2015/02/18/phantomas-metrics/10-45/zalando.de-start page.json
   ```
   
   `phantomas-metrics/10-45/zalando.de-start page.json`:
   
   ```json
   {
       "url": "https://www.zalando.de", 
       "timestamp": "2015-02-18T10:45:00.626740", 
       "metrics": {
           "requests": 119, 
           "gzipRequests": 41, 
           "postRequests": 0, 
           "httpsRequests": 119, 
           "notFound": 0, 
           "bodySize": 1498948, 
           "contentLength": 1562108, 

           ...

           "slowestResponse": 2131, 
           "smallestLatency": 6, 
           "biggestLatency": 2130, 
           "medianResponse": 445, 
           "medianLatency": 453
       }, 
       "site": "zalando.de", 
       "page": "start page"
   }
   ```
   

By [Martin Loetzsch](http://martin-loetzsch.de)