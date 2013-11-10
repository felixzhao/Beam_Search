from heapq import *
import beam_search_helper




def beam_search(match_word_test, test_vectors, train_vectors, beam_width):
    #define
    unks = []
    docs = []
    cands = [] # dist, unk, cand, #doc
    result = {} # unki : [ candj]

    # init
    topnum = 50
    unks = match_word_test
    docs.append(test_vectors)
        
    for u in unks:
        for d in docs:
            cands = list( \
                merge( \
                    beam_search_helper.find_cands(u, d, trainvectors) \
                        ,cands) \
                    )                    
        t_docs = []
        for item in nsmallest(beam_width, cands):
            # unk, cand, doc
            t_docs.append( \
                beam_search_helper.update_docs( \
                        item[1], \
                        item[2],\
                        docs[ item[3] ],\
                        train_vectors \
                        ) \
                    )
            result[item[1]].append(item[2])

        # perpare for next turn
        docs = t_docs
        cands = []
    # end of beam search
    return result
