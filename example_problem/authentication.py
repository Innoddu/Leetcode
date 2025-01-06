import heapq
def authentication(time_to_live, queries):
    dic = {}
    res = []
    heap = []
    cnt = 0
    for query in queries:
        query = query.split(" ")
        event = query[0]

        if event == "generate":
            token_id, current_time = query[1], int(query[2])
            if token_id not in dic:
                expiration_time = current_time + time_to_live
                dic[token_id] = expiration_time
                heapq.heappush(heap, (expiration_time, token_id))
        elif event == "renew":
            token_id, current_time = query[1], int(query[2])
            if token_id in dic and dic[token_id] > current_time:
                expiration_time = current_time + time_to_live
                dic[token_id] = expiration_time
                heapq.heappush(heap, (expiration_time, token_id))
        elif event == "count":
            current_time = int(query[1])
            print(heap)
            while heap and heap[0][0] <= current_time:
                exp_time, tok_id = heapq.heappop(heap)
                # Ensure consistency with the dictionary (only remove if not renewed)
                if dic.get(tok_id) == exp_time:
                    del dic[tok_id]
            res.append(len(dic))
    return res




time_to_live = 5
queries = ["generate aaa 1", "renew aaa 2", "count 6", "generate bbb 7", "renew aaa 8", "renew bbb 10", "count 15"]
print(authentication(time_to_live, queries))
