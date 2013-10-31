unks = [] # queue
cands = []
docs = []
results = {} # dict key:unk , value:cands list

def add2result(unk, cands):
    result[unk] = cands

def generatedoc(cand):
  

def beam_search():
  if len(cands) != 0:
    add2result(unks.top,cands) # top unks, all cands
    unks.remove(top)
    docs.clean()
    for cand in cands:
      docs.add(generatedoc(cand))
    cands.clean()
    if len(unks) == 0:
      return
    else
      unk = unks.top
      tempcands = [(,)] # tuple list. first:cand , second:doc number
      for doc in docs:
        tempcands.append((findcands(unk, doc),doc)) # generate tuple (cand,doc)
      tempcands = tempcands.sort().top(n)
      docs = tempcands[doc] # just keep the doc which find cands
      cands = tempcands[cand] # put cands info to cands Queue without doc info
      