
import sys
import math

def GetDataDict(path):
    infile = open(path, 'r')
    dict = {}
    '''
        Create infile data dict
    '''
    for line in infile.readlines():
        if line.startswith(' '):
            continue
        else:
            w = line.split(':')
            if len(w) > 1:
                t = w[1].split('|')
                v = [x.lstrip(' ').split(' ')[0].strip(' ') for x in t][:-1]
                dict[w[0].strip(' ')] = v
    return dict

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
    baseline = 'C:/Users/zhaoqua/Documents/GitHub/Beam_Search/ResultCompare/baseline/baseline_result_33per_5width.txt'
    beamsearch = 'C:/Users/zhaoqua/Documents/GitHub/Beam_Search/ResultCompare/updated/updated_out.bw5.ns0.sfw0.type33.txt'
    idcg = 5
    out_file = open('out/ndcg_score__bw3.ns0.sfw0.type33_vs_baseline.w5.type33.txt','w')

    baseline_score = {}
    beamsearch_score = {}

    equal = 0
    bigger = 0
    smaller = 0

    baseline_dict = GetDataDict(baseline)
    beamsearch_dict = GetDataDict(beamsearch)
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
