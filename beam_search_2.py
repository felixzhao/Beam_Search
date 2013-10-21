
def find_match_candidates_list(w):
  return list

def find_comb_weight(w1, w2):
  return (w1 + w2) / 2

def replace_max_element(bucket, w, weight):
  return bucket

def find_best_beam_search( test_unk_word_list, find_match_candidates_list, beam_width):
  bucket = {} # init as a dict
  root = test_unk_word_list[0]
  cands = find_match_candidates_list(root)
  for cand in cands:
    # ? update matrix ?
    next_cands = find_match_candidates_list(cand)
    for next_cand in next_cands:
      curr_comb = find_comb_weight(cand, next_cand)
      if len(bucket) < beam_width:
        bucket[cand] = curr_comb # find cand, sotre the comb weight value.
      else:
        replace_max_element(bucket, cand, curr_comb)
  return bucket
  
def find_best(test_unk_word_list):
  beam_width = 20
  cand_dict = {}
  for i in xrange(len(test_unk_word_list)):
    curr_unk_list = test_unk_word_list[i:]
    cand_dict[test_unk_word_list[i]] = find_best_beam_search(test_unk_word_list[i], find_match_candidates_list, beam_width)
  return cand_dict