# There is an array of n integers. There are also 2 disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
# Input Format:-
# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.
# Output Format:- Output a single integer, your total happiness.
# Sample Input:-
# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Ouput:- 1

f_in = list(map(int,input().split()))[:2]
n, m= f_in[0], f_in[1]
s_in = list(map(int,input().split()))[:n]
a = set(map(int,input().split()))
b = set(map(int,input().split()))
a_c, b_c = 0,0
a_c = len([a_c+1 for x in s_in if x in a])
b_c = len([b_c+1 for x in s_in if x in b])
print(a_c-b_c)