#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import yaml
import os

import argparse
parser = argparse.ArgumentParser(
    description='''Generate a LuMP recorder command from a ARTEMIS3 YAML config file''')
parser.add_argument('configFile', help='YAML config file')
parser.add_argument('--templateDir', help='jinja2 template dir', default='../templates')
parser.add_argument('-t', '--template', help='jinja2 template', default='LuMP_recorder.j2')
parser.add_argument('-o', '--output', help='Output script name, default: YAML config name with _laneX.sh')
parser.add_argument('-s', '--start_date', help='Override the config file start date, format: YYYY-MM-DDThh:mm:ssZ or none')
parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
args = parser.parse_args()

configData = yaml.load(open(args.configFile))

# check for start_date
if 'start_date' in configData:
    configData['opt_arg'] = '--start_date=%s'%configData['start_date']

# override start_date
if not(args.start_date is None):
    if args.start_date.startswith('none'): configData['opt_arg'] = ''
    else: configData['opt_arg'] = '--start_date=%s'%args.start_date

# build a config dict for each lane
configBase = configData.copy()
configBase.pop('lane', None)

for lane in configData['lane']:
    configLane = {**configBase, **lane}

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader(args.templateDir), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(args.template)
    renderText = template.render(configLane)
    
    if args.verbose: print(renderText)

    if args.output is None:
        outputFn = os.path.splitext(os.path.basename(args.configFile))[0]
    else: outputFn = args.output
    outputFn += '_lane%i.sh'%lane['id']
    print('Writing ' + outputFn)
    
    fh = open(outputFn,'w')
    fh.write(renderText)
    fh.close()

