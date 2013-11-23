
def nsmallestcandidates(width, candi_tuple_list):
    result = [] # dist, cand, #doc

    dict = {} # key: cand ; value: [ sum, count, # mini tuple ]

    sorted_list = []

    for item in candi_tuple_list:
        if item[1] not in dict:
            dict[item[1]] = [ item[0], 1, item ]
        else:
#            cur_node = dict[item[1]]
            if item[0] < dict[item[1]][2][0]: # current score < min score
                cur_dist = dict[item[1]][0]
                dict[item[1]] = [ cur_dist + item[0], dict[item[1]][1] + 1, item ] # sum dist, count+1, min node
    
    sorted_list = sorted([ ( x[0]/x[1], x[2] ) for x in dict.values()], key = lambda x:x[0])[:width]

    print 'sorted list:'
    print sorted_list
    print

    result = [ x[1] for x in sorted_list ]

    return result

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
    expected = [ (0.7, 'a', 2), (0.7, 'b', 3), (0.9,'d',1)]
    print 'width 3:'
    for item in actual:
        print item
  
