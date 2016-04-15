# -*- coding: utf-8 -*-
# This is HW for stable-matching algorithm.
import random


def stable_matching(men=[], women=[]):
    assert isinstance(men, list) or isinstance(men, tuple)
    assert isinstance(women, list) or isinstance(women, tuple)

    n = len(men)
    assert n == len(women)

    matched = []
    husband = [0 for _ in xrange(n)]

    men_copy = []
    for m, item in enumerate(men):
        men_copy.append([0, item])

    unmatched_men = range(n)

    women_invert = [[0 for i in xrange(n)] for j in xrange(n)]
    for w in xrange(n):
        for p, m in enumerate(women[w]):
            women_invert[w][m-1] = p

    while len(unmatched_men) > 0:
        m = unmatched_men.pop(0)
        idx, m_pref = men_copy[m]
        assert idx < n
        w = m_pref[idx]-1
        men_copy[m][0] = idx+1
        w_husband = husband[w]-1
        if w_husband == -1:
            pass
        elif women_invert[w][m] < women_invert[w][w_husband]:
            matched.remove((w_husband+1, w+1))
            unmatched_men.append(w_husband)
        else:
            unmatched_men.append(m)
            continue
        husband[w] = m+1
        matched.append((m+1, w+1))

    return matched


def verify_matching(matched_list=[], men=[], women=[]):
    n = len(matched_list)
    assert n == len(men)
    assert n == len(women)
    husband = [-1 for _ in xrange(n)]
    women_invert = [[-1 for i in xrange(n)] for j in xrange(n)]
    for man, woman in matched_list:
        husband[woman-1] = man-1

    for w in xrange(n):
        for p, m in enumerate(women[w]):
            women_invert[w][m-1] = p

    for m, w in matched_list:
        m -= 1
        w -= 1
        for w_candidate in men[m]:
            w_candidate -= 1
            if w_candidate == w:
                break
            m_candidate = husband[w_candidate]
            m_candidate_rank = women_invert[w_candidate][m_candidate]
            m_rank = women_invert[w_candidate][m]
            if m_rank < m_candidate_rank:
                return False
    return True


if __name__ == "__main__":
    # m = ((3, 2, 1), (3, 2, 1), (3, 2, 1))
    # w = ((1, 2, 3), (1, 2, 3), (1, 2, 3))
    m = []
    w = []
    n = input()
    arr = range(1, n+1)
    for i in xrange(n):
        random.shuffle(arr)
        m.append(arr[:])
        random.shuffle(arr)
        w.append(arr[:])
    matched = stable_matching(m, w)
    print verify_matching(matched, m, w)
