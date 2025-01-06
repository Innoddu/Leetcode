
def find_rebuffering_time(arrivalRate, packets):
    from collections import deque
    buffer = set()
    queue = deque(packets)
    time = 1
    count = 0
    played = set()

    while True:
        if time not in played:
            if time in buffer:
                buffer.remove(time)
                played.add(time)

        while count < arrivalRate and queue:
            get_packet = queue.popleft()
            if get_packet != time and get_packet not in played:
                buffer.add(get_packet)
            else:
                if get_packet in buffer:
                    buffer.remove(get_packet)
                    played.add(get_packet)
                elif get_packet in played:
                    count += 1
                    continue
                elif get_packet == time and count != 0:
                    return get_packet
                else:
                    played.add(get_packet)
            count += 1
        if time not in buffer and time not in played:
            return time
        time += 1
        count = 0
        if not queue and not buffer:
            break
    return  -1



# print("answer: ", find_rebuffering_time(2, [1,2,3,4,4,5]))
# print("answer: ", find_rebuffering_time(2, [1,3,2,1,2,3,3,4]))
print("answer: ", find_rebuffering_time(2, [3,4,5,6]))