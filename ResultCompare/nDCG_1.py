
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

    beam_width = sys.argv[1]
    
    baseline = 'C:/Users/zhaoqua/Documents/GitHub/Beam_Search/ResultCompare/baseline/baseline_result_33per_' + beam_width + 'width.txt'
    beamsearch = 'C:/Users/zhaoqua/Documents/GitHub/Beam_Search/ResultCompare/updated/updated_out.bw' + beam_width + '.ns0.sfw0.type33.txt'
    idcg = int(beam_width)
    out_file = open('out/ndcg_score__bw' + beam_width + '.ns0.sfw0.type33_vs_baseline.w' + beam_width + '.type33.txt','w')

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

    print >> out_file, 'Totally, ' , len(beamsearch_dict), ' unknown words.'
    print >> out_file, ' same score are ' , equal, ' items.'
    print >> out_file, ' beam search score higher ' , smaller, ' items.' 
    print >> out_file, ' base line  score higher ' , bigger, ' items.' 
    
    '''
        print sum
    '''
    beamsearch_nDCG_score_sum = sum(beamsearch_score.values())
    baseline_nDCG_score_sum = sum(baseline_score.values())
    
    print >> out_file, ' beam search sum of nDCG socre : ', beamsearch_nDCG_score_sum
    print >> out_file, ' base line sum of nDCG socre : ', baseline_nDCG_score_sum
    
    '''
        print match rate
    '''
    beamsearch_match_count = len([x for x in beamsearch_score.values() if x != 0.0])
    baseline_match_count = len([x for x in baseline_score.values() if x != 0.0])
    
    beamsearch_match_rate = beamsearch_match_count / float(len(beamsearch_score.values()))
    baseline_match_rate = baseline_match_count / float(len(baseline_score.values()))
    
    print >> out_file, ' beam search match count : ', beamsearch_match_count
    print >> out_file, ' base line match count : ', baseline_match_count 
    print >> out_file, ' beam search match rate : ', beamsearch_match_rate
    print >> out_file, ' base line match rate : ', baseline_match_rate
    
    '''
        print result list
    '''
    print >> out_file, ''
    print >> out_file, '[ ' + str(len(beamsearch_dict)) + ' , ' + str(equal) + ' , ' + str(smaller) + ' , ' + str(bigger) + ' , ' + \
    str(beamsearch_nDCG_score_sum) + ' , ' + str(baseline_nDCG_score_sum) + ' , ' + \
    str(beamsearch_match_count) + ' , ' + str(baseline_match_count) + ' , ' + \
    str(beamsearch_match_rate) + ' , ' + str(baseline_match_rate) + ' ]'
    