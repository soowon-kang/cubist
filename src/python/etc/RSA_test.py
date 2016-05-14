# -*- coding: utf-8 -*-

W = ''
e = 65537
N = '251959084756578934940271832400483985714292821262040320277771378360' + \
    '436620207075955562640185258807844069182906412495150821892985591491761' + \
    '845028084891200728449926873928072877767359714183472702618963750149718' + \
    '246911650776133798590957000973304597488084284017974291006424586918171' + \
    '951187461215151726546322822168699875491824224336372590851418654620435' + \
    '767984233871847744479207399342365848238242811981638150106748104516603' + \
    '773060562016196762561338441436038339044149526344321901146575444541784' + \
    '240209246165157233507787077498171257724679629263863563732899121548314' + \
    '38167899885040445364023527381951378636564391212010397122822120720357'

C = '473463379097395072539382495898454906162085639659681879026616405399' + \
    '495428424451169861087052967202641507260707838025696748306386596983605' + \
    '617023159825207980919535323747249313079619320923847473538628418896959' + \
    '924332987550448551320389957960312333459727231630200163526404478615036' + \
    '000545814295023512771540109722801728543731516146595003846162482291799' + \
    '055705196472613129901599055808522390957417668596322767896856368879132' + \
    '056761699370403966369802707137725838745346719636653335034558017593217' + \
    '972700982640056697620610010799294669918826078072748492675616914943800' + \
    '1601988621860821660494703813190215928005980318603191982012282039859'

#word_list = [1] #+[0 for i in xrange(10)]

#print int("3542253452435432543435", 10)
#print bin(int(N, 10))
#print bin(int(C, 10))
#print len(N)

def make_candidate(lst, radix):
    n = 0
    for idx in xrange(len(lst)):
        n += lst[-(idx+1)] * (radix**idx)
    return n

def find_word(word_list):
    large_n = int(N)
    large_c = int(C)
    while len(word_list) < 10:
        word_list[-1] += 1
        for idx in xrange(len(word_list)-1, -1, -1):
            if word_list[idx] == 36:
                word_list[idx] = 0
                if idx == 0:
                    word_list = [1] + word_list
                    print word_list
                else:
                    word_list[idx-1] += 1
        cand = make_candidate(word_list, 36)
        if encrypt(cand, e, large_n) == large_c:
            return True, word_list
    print 'NO'
    return False, word_list

def find_p(start, end):
    P = start
    large_n = int(N)
    large_c = int(C)
    #length = len(str(P))
    while P < end:
        if encrypt(P, e, large_n) == large_c:
            return True, P
        if P%100 == 0:
            print P
        P += 1
    return False, P

def encrypt(value, e, n):
    val = 1
    for i in xrange(e):
        val *= value
        val %= n
    return val % n

#print find_word([1]) #[22, 10, 7, 17]
#print find_p(1, int(N))
p = 3
large_n = int(N)
while large_n%p > 0:
    p += 2
print p
print large_n/float(p)

def factoring(n):
    p = 2
    lst = []
    while n > 1:
        if is_prime(p):
            count = 0
            while n%p == 0 and n > 1:
                count += 1
                n /= p
            lst.append((p, count))
        else:
            p += 1

