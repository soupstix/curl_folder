

fd=open('ofile','r')
s = fd.read()
fd.close()
print s
s=s.replace("hello","edited!!")
print s
fd=open('ofile','w')
fd.write(s);
fd.close()

