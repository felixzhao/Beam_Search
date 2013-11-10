from heapq import *
import beam_search_helper




def beam_search(match_word_test, test_vectors, train_vectors, beam_width):
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
            # add result
            if(u not in result):
                result[u] = []
            result[u].append(item[1])

        # perpare for next turn
        docs = t_docs
        cands = []
    # end of beam search
    return result

if __name__ == '__main__':
    ## init data
    trainvectors = {'a':[5,5], 'b':[2,2], 'c':[3,3], 'k':[1,1]}
    testvectors = {'<unk>1':[9,9], '<unk>2':[8,8], '<unk>3':[7,7], 'k':[1,1]}
    word_list = ['<unk>1', '<unk>2', '<unk>3']
    beam_width = 2
  ## expected 
    expected = 'a'
  ## get result
    actual =  beam_search(word_list, testvectors, trainvectors, beam_width)
  ## pirnt out result
    for k in actual.keys():
        print 'key: {0} ; value: {1};'.format(k, actual[k])

 #   print(expected == actual[1][0])
#    print('best_match is the first word in list : ')
  #  print(actual[1])
   # print(' ; score : ' + str(actual[0]))
