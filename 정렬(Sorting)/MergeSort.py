import random
import time

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):

        if left_list_index < left_list_length and right_list_index < right_list_length:

            # 왼쪽 리스트와 오른쪽 리스트의 값을 비교해줄것임
            # 작은 값부터 차례대로 sorted_list에 저장
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # 왼쪽 리스트의 끝까지 저장을 했으면 완료했다는 뜻이므로, 오른쪽 리스트의 값을 저장시킴
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # 오른쪽 리스트의 끝까지 저장을 했으면 완료했다는 뜻이므로, 왼쪽 리스트의 값을 저장시킴
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # 원소가 1개이면 종료
    if len(nums) <= 1:
        return nums

    # 가운데 위치
    mid = len(nums) // 2

    # mid 기준으로 양쪽을 정렬
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # 정렬된 리스트를 병합
    return merge(left_list, right_list)


if __name__ == '__main__':

    random_list_of_nums = []

    for i in range(10000):
        random_list_of_nums.append(random.randint(1, 10000))
    print(random_list_of_nums)
    start_time=time.time()

    random_list_of_nums = merge_sort(random_list_of_nums)

    end_time=time.time()

    print(random_list_of_nums)
    print("걸린 시간: ",end_time-start_time)
