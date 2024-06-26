# arr=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# # 카운트할 배열 = 인덱스 수 설정
# cnt=[0]* (max(arr)+1)

# # 각 데이터에 해당하는 인덱스 값 +1을 한다
# for i in range(len(arr)):
# 	cnt[arr[i]] +=1

# for i in range(len(cnt)):
# 	#  cnt의 인덱스 하나를 돈다
# 	for _ in range(cnt[i]):
# 		# i를 cnt의 값만큼 반복출력하고 빠져나와서 다음 인덱스로 이동
# 		print(i, end =' ')

import sys
# 상근이가 가지고 있는 숫자 카드
user_num = int(sys.stdin.readline())
user_card = list(map(int, sys.stdin.readline().split()))

# 상근이가 가지고 있지 않은 숫자 카드
other_num = int(sys.stdin.readline())
other_card = list(map(int, sys.stdin.readline().split()))

#이진 탐색 = 데이터가 정렬되어 있는 배열에서 찾고자 하는 수를 찾아내는 방법
# 데이터가 정렬되어 있는 배열 (오름차순)
other_card.sort()

# 찾고자 하는 수 target 
def binary_search(target, array) :
    start = 0
    end = other_num -1
    mid = (start + end)//2

    while start <= end:
        if array[mid] == target :
            return True
        elif other_card[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return False

for i in other_card:
    if binary_search(i, user_card) :
        print(1, end = ' ')
    else:
        print(0, end = ' ') 