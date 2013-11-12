import sys
import string, gzip
import time

from heapq import *
import beam_search_helper




def beam_search(match_word_test, test_vectors, train_vectors, beam_width):

    print >>sys.stderr, 'beam search started. at', time.strftime('%X')  

    #define
    unks = []
    docs = []
    cands = [] # dist, cand, #doc
    result = {} # unki : [ candj]

    # init
    topnum = 50
    unks = match_word_test
    docs.append(test_vectors)
    
    for u in unks:
        for d in xrange(len(docs)):
            cands = list( \
                merge( \
                   beam_search_helper.find_cands(u, docs[d], trainvectors, topnum, d) \
                        ,cands) \
                    )                    
        t_docs = []
        for item in nsmallest(beam_width, cands):

            #print len(item)
            #print item[-1]

            # unk, cand, doc
            t_docs.append( \
                beam_search_helper.update_docs( \
                        u, \
                        item[1], \
                        docs[ item[2] ],\
                        train_vectors \
                        ) \
                    )
            # add result
            if(u not in result):
                result[u] = []
            result[u].append(item[1])

        # perpare for next turn
        docs = t_docs
        cands = []
        print >>sys.stderr, 'unk: ', u, ' done. at time: ', time.strftime('%X')
    # end of beam search
    return result

if __name__ == '__main__':
    
    te_path = 'test.embed.txt.gz'
    tr_path = 'train.embed.txt.gz'
    
    trainfile = gzip.open(tr_path, "rb")
    testfile = gzip.open(te_path, "rb")
    
    #trainfile = gzip.open(sys.argv[1], "rb")
    #testfile = gzip.open(sys.argv[2], "rb")
    
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
        
    ## init data
    beam_width = 3
    ## get result
    actual =  beam_search(unk_list, testvectors, trainvectors, beam_width)
    ## pirnt out result
    for k in actual.keys():
        print ' ===== start of ' + k + ' ====== '
        print 'key: {0} ; value: {1};'.format(k, actual[k])
        print ' ===== end of ' + k + ' ====== '
        print ' '

 #   print(expected == actual[1][0])
#    print('best_match is the first word in list : ')
  #  print(actual[1])
   # print(' ; score : ' + str(actual[0]))
