#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import yaml
import os

import argparse
parser = argparse.ArgumentParser(
    description='''Generate a LCU command from a ARTEMIS3 YAML config file''')
parser.add_argument('configFile', help='YAML config file')
parser.add_argument('--templateDir', help='jinja2 template dir', default='../templates')
parser.add_argument('--template', help='jinja2 LCU beamctl template', default='beamctl.j2')
parser.add_argument('-o', '--output', help='Output script name, default: YAML config name with _LCU.sh')
parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
args = parser.parse_args()

configData = yaml.load(open(args.configFile))

# beamctl
beamctlConfig = configData['beamctl']
beamctlConfig['generator_script'] = os.path.basename(__file__)

#Load Jinja2 template
env = Environment(loader = FileSystemLoader(args.templateDir), trim_blocks=True, lstrip_blocks=True)
template = env.get_template(args.template)
renderText = template.render(beamctlConfig)

if args.verbose: print(renderText)

if args.output is None:
    outputFn = os.path.splitext(os.path.basename(args.configFile))[0]
else: outputFn = args.output
outputFn += '_LCU.sh'
print('Writing ' + outputFn)

fh = open(outputFn,'w')
fh.write(renderText)
fh.close()

