import sys
import string, gzip
import time

from heapq import *
import beam_search_helper
import helper

def beam_search(match_word_test, test_vectors, train_vectors, beam_width):

    print >>sys.stderr, 'beam search started. at', time.strftime('%X')  

    #define
    unks = []
    docs = []
    cands = [] # dist, cand, #doc
    result = {} # unki : [ candj]
    
    nsmallest = []

    # init
    topnum = 50
    unks = match_word_test
    docs.append(test_vectors)
    
    for u in unks:

# log
        print u
# end log

        for d in xrange(len(docs)):
            cands = list( \
                merge( \
                   beam_search_helper.find_cands(u, docs[d], trainvectors, topnum, d) \
                        ,cands) \
                    )                    
            # debug
            print cands[0][0]
            print cands[0][1]
            print cands[0][2]
            # end debug
        t_docs = []
        for item in helper.nsmallestcandidates(beam_width, cands):
            print len(item)
            print item[-1]

            # unk, cand, doc
            t_docs.append( \
                beam_search_helper.update_docs( \
                        u, \
                        item[1], \
                        docs[ item[2] ],\
                        train_vectors \
                        ) \
                    )

# log
            print ' => ' + item[1] + ' : ' + str(item[0])
# end log
            # add result
            if(u not in result):
                result[u] = []
            result[u].append(item[1])

        # perpare for next turn
        docs = t_docs
        cands = []
        print >>sys.stderr, 'unk: ', u, ' done. at time: ', time.strftime('%X')
# debug
        print ' ++++++ result ++++++ '
        print u
        print result[u]
        print result[u][0]
        print result[u][1]
        print result[u][2]
        print '{0}:{1}|{2}|{3}'.format(u,result[u][0],result[u][1],result[u][2])
        out_str = '{0}:'.format(u)
        for item in result[u]:
            out_str += '{0}|'.format(item)
        print out_str
        print ' ++++++ end of result ++++++ '
# end bebug
    # end of beam search
    return result

if __name__ == '__main__':
    
    ## init data
    beam_width_str = sys.argv[1]
    print 'beam width:' + beam_width_str
    beam_width = int(beam_width_str)
    
    te_path = 'test.embed.txt.gz'
    tr_path = 'train.embed.txt.gz'
    out_path = 'out.' + str(beam_width_str) + '.txt'
    
    trainfile = gzip.open(tr_path, "rb")
    testfile = gzip.open(te_path, "rb")
    
    outfile = open(out_path,'w')
    
    trainwords = set()
    testwords = set()
    knownwords = set()
    matchwords_train = []
    unk_list = []
    trainvectors = {}
    testvectors = {}
    
    #Read files
    for l in trainfile:
        toks = string.split(l)
        if toks[0] == '*UNKNOWN*':
            continue
        trainwords.add(toks[0])
        trainvectors[toks[0]] = [float(f) for f in toks[1:]]
    for l in testfile:
        toks = string.split(l)
        if toks[0] == '*UNKNOWN*':
            continue
        testwords.add(toks[0])
        testvectors[toks[0]] = [float(f) for f in toks[1:]]
    
    knownwords = trainwords & testwords
    matchwords_train = list(trainwords - knownwords)
    #Deal with the OOV words in test corpus
    for w in testwords:
        if w.startswith('<unk>'):
            unk_list.append(w)
        
    print len(unk_list)
    ## get result
    actual =  beam_search(unk_list, testvectors, trainvectors, beam_width)
    ## pirnt out result
    for k in actual.keys():
        print >> outfile, ' ===== start of ' + k + ' ====== '

        out_str = '{0}:'.format(k)
        for item in actual[k]:
            out_str += '{0}|'.format(item)
        print out_str

        print >> outfile, match_list

        print >> outfile, ' ===== end of ' + k + ' ====== '
        print >> outfile, ' '
