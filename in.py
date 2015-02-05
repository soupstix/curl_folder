import argparse
import sys
import subprocess
parser=argparse.ArgumentParser()
parser.add_argument("-O", "--overridden_facts", dest="overridden_facts", default=False, help="any overridden facts")
args = parser.parse_args()
def msg(string):
    print string
    return 'returned string'
#sys.stdout=open('ofile','w')
print 'hello' 
print msg('hellooo')
if args.overridden_facts :
    for ufkv in  args.overridden_facts.split(' '):
        key,value = ufkv.split('=')
        print 'arg[' + key + '] '+value
user_facts={}
#for user_input_fact in args.overridden_facts.split(' '):
 #   key,value=user_input_fact.split('=')
  #  user_facts[key]=value


