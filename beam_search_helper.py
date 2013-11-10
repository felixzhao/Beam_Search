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

def find_cands(match_word_test, test_vectors, train_vecotrs):
    topnum = 50
    heap = []

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
        print >>sys.stderr, 'Generating match scores for: ', match_word_train, ' and ', match_word_t\
est
        match_score = calcMatchScore(match_word_test, match_word_train, knn, trainvectors, testvecto\
rs)
        heappush(heap, (match_score,match_word_train))

    return heap
