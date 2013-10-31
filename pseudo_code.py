# input
unk_list = ['unk1','unk2',...]
test_vector_set = { 'word1':['a word embed vector for word1'], 'unk1':['a word embed vector for unk1'], ...} # word embed vector set of test set
training_vector_set = { 'word1':['a word embed vector for word1'], 'word2':['a word embed vector for word2'], ...} # word embed vector set of training set

# output
match_candidates_list = ['word6','word7',...]

# temp variable
level_candidates_set = [
    [('cand_word1',['word embed vector']),('cand_word2',['word embed vector']),...], # cands for level one (unk1)
    [('',[]),('',[]),...], # cands for level two (unk2)
    ...
] # a cands set for each unk
