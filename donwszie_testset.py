import sys
import gzip

sourcefile = gzip.open(sys.argv[1],'rb').readlines()
outfile_name = sys.argv[2]

fout = open(outfile_name,'w')

for i in xrange(len(sourcefile)):
    if i % 10 == 0:
        print i
        fout.write(sourcefile[i])

fout.close()

fout = open(outfile_name,'rb')

print len(fout.readlines())
