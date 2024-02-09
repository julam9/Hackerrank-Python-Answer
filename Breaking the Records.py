def breakingRecords(scores):
    n = len(scores)
    max_record = [scores[i+1] for i in range(n-1) if max(scores[:i+1]) < scores[i+1]]
    min_record = [scores[i+1] for i in range(n-1) if min(scores[:i+1]) > scores[i+1]]
    return(len(max_record), len(min_record))