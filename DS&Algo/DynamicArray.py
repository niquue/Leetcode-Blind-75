import sys

def ring(S):
    color = {}
    score = 0
    for i in range(len(S)):
        if S[i].isnumeric():
            color[S[i]] = list()

    for i in range(0, len(S), 2):
        color[S[i+1]].append(S[i])
        print(S[i])

    for key in color:
        check = color[key]
        if 'R' in check and 'B' in check and 'G' in check:
            score += 1
    print(score)
    print(color)
    return score

def solution(A):
    counter = 0
    # word = ""
    new_list = set()
    for i in range(len(A)):
        grab_string = A[i]
        if grab_string == grab_string[::-1]:
            new_list.add(grab_string)
    print(new_list)
    word_list = set()
    for i in range(len(A)):
        #print(A[i])
        for j in range(0,len(A),1):
            word = ""
            word += A[i] + A[j]

            if word == word[::-1]:
                new_list.add(A[i])
                new_list.add(A[j])
                word_list.add(word)
            #print(word)
    #print(word_list)
    for i in new_list:
        for j in new_list:
            word = ""
            word += i
            word += j
            print(word)
    print(new_list)
    return len(word_list.pop())


# ring("R0B0")
#["ck", "kc", "ho", "kc"]
numb = solution(["ab", "hu", "ba", "nn"])
#print(numb)