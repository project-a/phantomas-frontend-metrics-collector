import json
import os.path
import inspect
import sys
import subprocess
import datetime
from collections import OrderedDict

# most reliable way to find out the path of this script
def dummy_function():
    pass

# read config
config_path = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy_function))) + '/config.json'

if not os.path.isfile(config_path):
    print >> sys.stderr, 'please copy config.json.example to config.json and adapt it'
    sys.exit(1)

config = json.load(open(config_path), object_pairs_hook=OrderedDict)

# check output dir
output_base_dir = config['output-base-dir']

if not os.path.isdir(output_base_dir) or not os.access(output_base_dir, os.W_OK):
    print >> sys.stderr, 'directory "' + output_base_dir + '" does not exist or is not writable'
    sys.exit(1)

# create output dir by day, e.g. {base-path}/2015/02/10/phantomas-metrics/%H-%M/"
output_dir = output_base_dir + datetime.datetime.now().strftime("/%Y/%m/%d/phantomas-metrics/%H-%M/")
os.system('mkdir -p -m 755 ' + output_dir)

now = datetime.datetime.now()

# crawl pages and write results
for site, pages in config['sites'].items():
    for page, url in pages.items():
        print 'fetching ' + site + ' ' + page + ' (' + url + ')'

        process = subprocess.Popen(config['phantomas-binary'] + ' --reporter=json ' + url,
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # output hopefully is one line of json
        output = process.stdout.readline()

        if (process.wait() not in [0, 252]):  # 252 is timeout
            for line in process.stderr.readlines():
                print >> sys.stderr, line
            exit(1)

        phantomas_result = json.loads(output, object_pairs_hook=OrderedDict)
        data = {'site': site, 'page': page, 'url': url, 'timestamp': now.isoformat(),
                'metrics': phantomas_result['metrics']}

        json.dump(data, open(output_dir + site + '-' + page + '.json', 'w'), indent=4)


