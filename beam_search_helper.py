import sys
import math
from heapq import *

def calcdist(x, y):
    res = 0.0
    for i in range(len(x)):
        res += (x[i]-y[i]) ** 2
    return math.sqrt(res)

def calcMatchScore(w1, w2, knn, trainvectors, testvectors):
    res = 0.0
    i = 0
    for w in knn:
        d1 = calcdist(trainvectors[w2],trainvectors[w])
        d2 = calcdist(testvectors[w1],testvectors[w])
        i+=1
        res += (d1-d2)**2 / i
    return res

def update_docs(unk, cand, doc, train_vecotrs):
    updated_vectors = doc.copy()
    updated_vectors[cand] = train_vecotrs[cand]
    del updated_vectors[unk]
    return updated_vectors

def find_cands(match_word_test, testvectors, trainvectors, topnum, doc_num):

    trainwords = set(trainvectors.keys())
    testwords = set(testvectors.keys())
    knownwords = trainwords & testwords
    matchwords_train = list(trainwords - knownwords)

# Get knn
# calculate clostest known_words in test_vectors which count is topnum
# The test_vectors could be change in bean search

    heap = []
    knn = []
    for known_word in knownwords:
        dist = calcdist(testvectors[match_word_test],testvectors[known_word])
        heappush(heap, (dist,known_word))
    for item in nsmallest(topnum, heap):
        knn.append(item[1])

# End of Get knn

# Get match words
# get match word & match_score in train_words to test_word
# which size based on topnum
# "knn", "test_vectors" could be change in bean_search

    heap = []
    for match_word_train in matchwords_train:
        print >>sys.stderr, 'Generating match scores for: ', match_word_train, ' and ', match_word_test
        match_score = calcMatchScore(match_word_test, match_word_train, knn, trainvectors, testvectors)
        heappush(heap, (match_score,match_word_train,doc_num))

    return heap

if __name__ == '__main__':
    print '====== unit test for update doc ======'
    print '--- case 1 ---'
    unk = 'u'
    cand = 'c'
    doc = {'u':1,'b':2}
    trv = {'b':3,'c':4}
    expected = {'b':2,'c':4}
    actual = update_docs(unk, cand, doc, trv)
    if( len(actual) != len(expected)):
        print 'test for update doc, case 1 failed'
    else:
        for k in expected.keys():
            if ( expected[k] != actual[k]):
                print 'test for update doc, case 1 failed'
        print 'case 1 passed.'
    print '--- case 1 end ---'
    print '--- case 2 ---'
    cand = 'b'
    expected = {'b':3}
    actual = update_docs(unk, cand, doc, trv)
    if( len(actual) != len(expected)):
        print 'test for update doc, case 2 failed'
    else:
        for k in expected.keys():
            if ( expected[k] != actual[k]):
                print 'test for update doc, case 2 failed'
        print 'case 2 passed.'
    print '--- case 2 end ---'
    print '====== end of unit test for update doc ======'
    print ' '

    print '====== unit test for find cands ======'

    print '--- case 1 ---'
    topnum = 2
    doc_num = 9
    mwt = 'u'
    tev = {'u':[1,1], 'b':[0,0]}
    trv = {'b':[0,0], 'a':[0.5,0.25], 'c':[0.5,0.5], 'd':[3,1]}
    expected = set(['a','c','d'])
    actual = find_cands(mwt, tev, trv, topnum, doc_num)

    for item in actual:
#        print 'score: ', item[0], '; cand: ', item[1] '; doc_num: ',item[2]
        print 'score: {0} ; cand: {1} ; doc_num: {2} ;'.format(item[0], item[1], item[2])

    if( len(actual) != len(expected)):
        print 'test for find cands, case 1 failed. len diff.'
    else:
        if(set([x[1] for x in actual]) != expected):

#        for k in xrange(len(expected)):
 #           if ( expected[k] != actual[k][1] or doc_num != actual[k][2]):
                print 'test for find cands, case 1 failed'
        print 'case 1 passed.'
    print '--- case 1 end ---'
    print '====== end of unit test for update doc ======'
    print ' '
    

    print '====== end of unit test for find cands ======'
