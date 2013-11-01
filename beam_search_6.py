from collections import deque

unks = deque() # queue, left in & right out
cands = []
docs = deque()
results = {} # dict key:unk , value:cands list

def add2result(unk, cands):
    result[unk] = cands

def generatedoc(cand):
  

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
      temp_cands_tuple = {} # generate tuple ( cand, doc number )
      while docs.empty() != True:
        temp_cands_tuple.append(find_cands(cur_unk, temp_docs.pop()))
      
      # generate res
      top_cands = get_top_cands(temp_cands_tuple)
      docs = deque(get_docs_from_top(top_cands)) # function return list
      cands = get_cands_from_top(top_cands) # function return list