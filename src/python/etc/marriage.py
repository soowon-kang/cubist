# This is HW for stable-matching algorithm.

def stable_matching(men=[], women=[]):
    assert isinstance(men, list) or isinstance(men, tuple)
    assert isinstance(women, list) or isinstance(women, tuple)
    
    matched = []
    return matched

def verify_matching(matched_list=[], men=[], women=[]):
    pass

if __name__ == "__main__":
    m = ((3,2,1), (3,2,1), (3,2,1))
    w = ((1,2,3), (1,2,3), (1,2,3))
    print stable_matching(m, w)

