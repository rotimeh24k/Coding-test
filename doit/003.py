
suNo, quizNo = map(int, input().split())
#input문자열을 받은 후 split하여 공백기준으로 list형태로 만듬
#map을 활용하여 list의 각 부분을 int형으로 형변환

numbers = map(int, input().split())
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int ,input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])