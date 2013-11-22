
# candi_tuple_list : tuple ( dist, cand, #doc )
# cands sorted by average dist for each cand
# #doc get smallest score for this cand
# return tuple list : tuple( dist, cand, #doc )
def nsmallestcandidates(width, candi_tuple_list):
  result = [] # dist, cand, #doc
  cands = dict() # cand, #doc
  
  doc_dic = dict() # cand, #doc
  score_dic = dict() # cand, score
  
  avg_list = dict()
  count_list = dict()
  
  # get cands sorted list by avg score for this cand
  for tuple in candi_tuple_list:
    if tuple[1] in avg_list:
      avg_list[tuple[1]] += tuple[0]
    else:
      avg_list[tuple[1]] = tuple[0]
    if tuple[1] in count_list:
      count_list[tuple[1]] += 1
    else:
      count_list[tuple[1]] = 1
    cands_sortby_avg_score = list(set([(x[1]/y[1], x[0]) for x in avg_list.items() for y in count_list.items()]))[:width] # avg_score, cand
   
  # debug 
  print 'avg list:'
  print avg_list
  print
  print 'count_list:'
  print count_list
  print
  print 'avg cands:'
  print cands_sortby_avg_score
  print
  # end debug
   
  # get smallest score for cand's #doc
  for sorted_cand in cands_sortby_avg_score: # avg_score, cand
    for source_item in candi_tuple_list: # dist, cand, #doc
      if sorted_cand[1] == source_item[1]:
      
        if sorted_cand[1] not in score_dic:
          doc_dic[sorted_cand[1]] = source_item[2]
          score_dic[sorted_cand[1]] = source_item[0]
          
        # debug
          if sorted_cand[1] == 'c' or sorted_cand[1] == 'e':
            print 'find init: ' + str(source_item[0]) + ' ' + str(sorted_cand[1]) + ' '  + str(source_item[2])
            print
        #end debug
          
        elif source_item[0] < score_dic[sorted_cand[1]]:
          doc_dic[sorted_cand[1]] = source_item[2]
          score_dic[sorted_cand[1]] = source_item[0]
          
        # debug
          if sorted_cand[1] == 'c' or sorted_cand[1] == 'e':
            print 'find: ' + str(source_item[0]) + ' '  + str(sorted_cand[1]) + ' '  + str(source_item[2])
            print
        if sorted_cand[1] == 'c' or sorted_cand[1] == 'e':
          print 'compare: ' + sorted_cand[1] + ' ' + str(source_item[0]) + ' vs ' + str(doc_dic[sorted_cand[1]])
          print
        # end debug

  # debug 
  print 'doc list:'
  print doc_dic
  # end debug
          
  # generate result
  for item in doc_dic.items():
    for source_item in candi_tuple_list:
      if source_item[1] == item[0] and source_item[2] == item[1]:
        result.append(source_item)

  return result # dist, cand, #doc
  
if __name__ == '__main__':
  cands = [(1, 'a', 1), (1.2, 'b', 1), (1.5, 'c', 1), (0.9, 'd', 1), (2, 'e', 1) \
           ,(0.7, 'a', 2), (2.3, 'b', 2), (1.2, 'c', 2), (1.2, 'd', 2), (1.2, 'e', 2) \
           ,(2.2, 'a', 3), (0.7, 'b', 3), (0.6, 'c', 3), (2.2, 'd', 3), (3.9, 'e', 3) \
          ]
          
  width = 5
  actual = nsmallestcandidates(width, cands)
  expected = [(0.6, 'c', 3), (0.7, 'a', 2), (0.7, 'b', 3), (0.9, 'd', 1), (1.2, 'e', 2)]
  print 'width 5:'
  for item in actual:
    print item
  print
  
  print ' ------ ------'
  width = 3
  actual = nsmallestcandidates(width, cands)
  expected = [(0.6, 'c', 3), (0.7, 'a', 2), (0.7, 'b', 3)]
  
  print
  print 'width 3:'
  for item in actual:
    print item
  