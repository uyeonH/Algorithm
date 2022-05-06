import math

def solution(fees, records):
    in_time = {}
    results = {}
    answer = []
    for record in records:
        time, number, inout = record.split()
        hour, min = time.split(":")
        hour = int(hour)
        min = int(min)
        if inout == "IN":
            in_time[number] = hour * 60 + min
            if number not in results.keys():
                results[number] = 0

        elif inout == "OUT":
            in_time_tmp = in_time[number]
            in_time[number] = -1
            results[number] = results[number] + hour * 60 + min - in_time_tmp
    for k, v in in_time.items():
        if v != -1:
            results[k] = results[k] + (23 * 60 + 59) - in_time[k]

    sorted_nums = sorted(results.keys())
    # 기본시간, 기본 요금, 단위시간, 단위요금
    for num in sorted_nums:
        v = results[num]
        if v > fees[0]:
            answer.append(fees[1] + (math.ceil((v - fees[0]) / fees[2])) * fees[3])
            print(math.ceil(v - fees[0] / fees[2]))
        else:
            answer.append(fees[1])
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)
