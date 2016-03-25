# This is HW for stable-matching algorithm.

def stable_matching(man=[], woman=[]):
    assert instance(man, list) or instance(man, tuple)
    assert instance(woman, list) or instance(man, tuple)
    
    matched = []
    return matched

if __name__ == "__main__":
    m = ((3,2,1),(3,2,1),(3,2,1))
    w = ((1,2,3),(1,2,3),(1,2,3))
    print stable_matching(m, w)

