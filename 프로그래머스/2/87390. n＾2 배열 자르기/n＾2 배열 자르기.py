# arr = [[3 for i in range(3)] for i in range(3)]
# arr

# for i in range(2):
#     for j in range(2):
#         arr[i][j]=2
# for i in range(1):
#     for j in range(1):
#         arr[i][j]=1
# arr

# def get_arr(n):
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#     for d in range(n):
#         for i in range(n-d):
#             for j in range(n-d):
#                 arr[i][j] = n-d
#     return arr

# def get_flat_arr(arr):
#     flat_arr = []
#     for a in arr:
#         flat_arr.extend(a)
#     return flat_arr

# def get_slice_arr(flat_arr, left,right):
#     slice_arr=[]
#     for i in range(left,right+1):
#         slice_arr.append(flat_arr[i])
#     return slice_arr

# def solution(n, left, right):
#     answer = []
#     arr = get_arr(n)
#     flat_arr = get_flat_arr(arr)
#     slice_arr = get_slice_arr(flat_arr,left, right)
#     return slice_arr

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n  # 몇 번째 행인지 계산
        col = i % n   # 몇 번째 열인지 계산
        value = max(row + 1, col + 1)  # 값 계산 (행, 열 중 큰 값)
        answer.append(value)
    return answer