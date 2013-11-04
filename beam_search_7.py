from collections import deque

unks = deque() # queue, left in & right out
cands = []
docs = deque()
results = {} # dict key:unk , value:cands list

def update_doc(doc, cand):
  return updated_doc

def find_cands(cur_unk, doc):
  return cands_tuple
  
trainvectors = {}
trainwords = set(trainvectors.keys())

def getmatchswithscore(match_word_test, testvectors):
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
    heappush(heap, (match_score,match_word_train))
#  for item in nsmallest(topnum, heap):
#    matchs.append(item)
# end for Get match words
  return heap

def beam_search():
  while unks.empty() != True:
    if len(cands) != 0:
      result(unks[-1], cands) # add2result(unks[-1],cands) # top unks, all cands
      cur_unk = unks.pop()
    
      # generate docs
      temp_docs = deque()
      while docs.empty() != True:
        for cand in cands:
          temp_docs.appendleft(update_doc(doc, cand))
      
      # get cands
      temp_cands_tuple = [] # generate tuple ( cand, doc number )
      while docs.empty() != True:
        temp_cands_tuple.append(find_cands(cur_unk, temp_docs.pop()))
      
      # generate res
      top_cands = get_top_cands(temp_cands_tuple)
      docs = deque(get_docs_from_top(top_cands)) # function return list
      cands = get_cands_from_top(top_cands) # function return list
