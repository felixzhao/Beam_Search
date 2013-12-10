import math

baseline = open('answer.txt','r')
beamsearch = open('out.50.txt','r')
unk_wordmap = open('unk_wordmap.txt','r')

wordmap_dict = {}
baseline_dict = {}
beamsearch_dict = {}

'''
    Create unk work map dict
'''
for line in unk_wordmap.readlines():
    w = line.split()
    wordmap_dict[w[0]] = w[1]

'''
    Create baseline result dict
'''
for line in baseline.readlines():
    if line.startswith(' '):
        continue
    else:
        w = line.split(':')
        if len(w) > 1:
            t = w[1].split('|')
            v = [x.lstrip(' ').split(' ')[0].strip(' ') for x in t][:-1]
            baseline_dict[w[0].strip(' ')] = v

'''
    Create beam search result dict
'''
for line in beamsearch.readlines():
    if line.startswith(' '):
        continue
    else:
        w = line.split(':')
        k = wordmap_dict[w[0]]
        v = w[1].split('|')
        beamsearch_dict[k] = [x for x in v if x != '\n']

'''
    nDCG Algorith for base line
'''
def nDCG(key, candidates, idcg):
    if len(candidates) != idcg:
        return -1

    list = []

    for cand in candidates:
        if key == cand:
            list.append(1)
        else:
            list.append(0)
            
    dcg_score = list[0]

    for i in xrange(1,len(list)):
        dcg_score += list[i] / math.log(i+1,2)
    ndcg_score = dcg_score / idcg
    return ndcg_score

if __name__ == '__main__':
    idcg = 50
    baseline_score = {}
    beamsearch_score = {}

    equal = 0
    bigger = 0
    smaller = 0

    out_file = open('ndcg_score.txt','w')

    '''
        get base line nDCG score
    '''
    for k in baseline_dict.keys():
        print 'baseline count for',k,
        print len(baseline_dict[k])
        for item in baseline_dict[k]:
            print item,'|',
        print ' '
        baseline_score[k] = nDCG(k, baseline_dict[k], idcg)
    '''
        get beam search nDCG score
    '''
    for k in beamsearch_dict.keys():
        beamsearch_score[k] = nDCG(k, beamsearch_dict[k], idcg)

    '''
        print result
    '''
    print >> out_file, 'word : base_line_score | beam_search_score'
    for k in beamsearch_dict.keys():
        print >> out_file, str(k),':', baseline_score[k],'|', beamsearch_score[k], '|', baseline_score[k] - beamsearch_score[k]

        if baseline_score[k] == beamsearch_score[k]:
            equal += 1
        elif baseline_score[k] < beamsearch_score[k]:
            smaller += 1
        else:
            bigger += 1

    print >> out_file, 'Totally, {0} unknown words.', len(beamsearch_dict)
    print >> out_file, ' same score are {0} items.', equal
    print >> out_file, ' beam search score higher {0} items.', smaller
    print >> out_file, ' base line  score higher {0} items.', bigger
