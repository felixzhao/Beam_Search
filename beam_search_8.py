from collections import deque

unks = deque() # queue, left in & right out
cands = []
docs = [] # list of doc. doc is a dictionary of word vector
results = {} # dict key:unk , value:cands list

trainvectors = {}
trainwords = set(trainvectors.keys())

def update_doc(doc, unk, cand):
  if cand == '':
    return doc
  updated_doc = doc.copy()
  updated_doc[cand] = trainvectors[cand]
  del updated_doc[unk]
  return updated_doc

def find_cands(match_word_test, testvectors, test_vector_number):
  matchs = []

  testwords = set(testvectors.keys())
  knownwords = trainwords & testwords
  matchwords_train = list(trainwords - knownwords)

# Get knn
# calculate clostest known_words in test_vectors which count is topnum
# The test_vectors could be change in bean search
  knn_size = 50
  heap = []
  knn = []
  for known_word in knownwords:
    dist = calcdist(testvectors[match_word_test],testvectors[known_word])
    heappush(heap, (dist,known_word))
  for item in nsmallest(knn_size, heap):
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
    heappush(heap, (match_score,match_word_train, test_vector_number))
#  for item in nsmallest(topnum, heap):
#    matchs.append(item)
# end for Get match words
  return heap

def beam_search(beam_width):
  while unks.empty() != True:
#    if len(cands) != 0:
      result(unks[-1], cands) # add2result(unks[-1],cands) # top unks, all cands
      cur_unk = unks.pop()
    
      # generate docs
      temp_docs = []
      for i in xrange(len(docs)):
        temp_docs.append(update_doc(docs[i], cur_unk, cand))
      
      # get cands
      temp_cands_tuple = [] # generate tuple ( score, cand, doc number )
      for i in xrange(len(temp_docs)):
        merge(temp_cands_tuple, find_cands(cur_unk, temp_docs[i], i))
      
      # generate res
      res_docs = set()
      cands = []
      for item in nsmallest(beam_width, temp_cands_tuple):
        res_docs.add(item[2])
        cands.append(item[1])
      docs = list(res_docs)
