import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-O", "--overridden_facts", dest="overridden_facts", default=False, help="any overridden facts")
args = parser.parse_args()
print 'hello' 
for ufkv in  args.overridden_facts.split(' '):
    key,value = ufkv.split('=')
    print 'arg[' + key + '] '+value
user_facts={}
#for user_input_fact in args.overridden_facts.split(' '):
 #   key,value=user_input_fact.split('=')
  #  user_facts[key]=value


