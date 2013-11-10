
from heapq import *

unks = []
docs = []
cands = [] # dist, unk, cand, #doc
result = {} # unki : [ candj]


def beam_search(match_word_test, test_vectors, train_vectors, beam_width):
    # init
    unks = match_word_test
    docs.append(test_vectors)
        
    for u in unks:
        for d in docs:
            cands = list(merge(find_cands(u, d, trainvectors),cands))
        t_docs = []
        for item in nsmallest(beam_width, cands):
            # unk, cand, doc
            t_docs.append( update_docs( item[1], item[2], docs[item[3]], train_vectors ) )
            result[item[1]].append(item[2])

        # perpare for next turn
        docs = t_docs
        cands = []

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
        print >>sys.stderr, 'Generating match scores for: ', match_word_train, ' and ', match_word_test
        match_score = calcMatchScore(match_word_test, match_word_train, knn, trainvectors, testvectors)
        heappush(heap, (match_score,match_word_train))

    return heap


    


