import collections
def solution(message, spoiler_ranges):
    words = message.split(" ")
    words_dict = []
    idx = 0
    start_idx = 0
    for i in range(0, len(message)):
        if message[i] == " ":
            words_dict.append((start_idx, idx, words[idx]))
            idx += 1
            start_idx = i + 1
    words_dict.append((start_idx, idx, words[idx]))
    que = collections.deque(spoiler_ranges)
    
    ans = []
    while que:
        start, end = que.popleft()
        for i, j, val in words_dict:
            word_start, word_end = i, i + len(val)
            if (end>=word_start) and (start<word_end):
                ans.append(j)
    
    not_ans = [i for i in range(len(words)) if i not in ans]
    word_set = list(set([words[i] for i in ans]))
    word_no_ans_set = list(set([words[i] for i in not_ans]))
    
    res = [i for i in word_set if i not in word_no_ans_set]
    
    return len(res)