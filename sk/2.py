import heapq

def solution(arr, processes):
    answer = []
    heap = []
    time = 1
    cur_process_idx = 0
    work_processes = -1
    end_time = -1
    processes_cnt = 0
    break_time = 0
    while processes_cnt < len(processes):
        if end_time <= time:
            work_processes = -1
        while cur_process_idx < len(processes) and int(processes[cur_process_idx].split()[1]) <= time:
            cmd = processes[cur_process_idx].split()[0]
            if cmd == "read":
                t1, t2, a, b = map(int, processes[cur_process_idx].rstrip().split()[1:])
                data = (a, b)
                cmd_type = 1    #read
            else:
                t1, t2, a, b, c = map(int, processes[cur_process_idx].rstrip().split()[1:])
                data = (a, b, c)
                cmd_type = 0    #write
            heapq.heappush(heap, (cmd_type, t1, t2, data))
            cur_process_idx += 1
        if heap and work_processes == -1:
            cmd_type, t1, t2, data = heapq.heappop(heap)
            end_time = time + t2
            if cmd_type == 0:
                for idx in range(data[0], data[1] + 1):
                    arr[idx] = str(data[2])
                work_processes = 0
                processes_cnt += 1
            elif cmd_type == 1:
                answer.append("".join(arr[data[0] : data[1] + 1]))
                processes_cnt += 1
                while heap and heap[0][0] == 1:
                    cmd_type, t1, t2, data = heapq.heappop(heap)
                    end_time = max(end_time, time + t2)
                    answer.append("".join(arr[data[0] : data[1] + 1]))
                    processes_cnt += 1
                work_processes = 1
        elif work_processes == 1:   #read
            while heap and heap[0][0] == 1:
                cmd_type, t1, t2, data = heapq.heappop(heap)
                end_time = max(end_time, time + t2)
                answer.append("".join(arr[data[0] : data[1] + 1]))
                processes_cnt += 1
            work_processes = 1
        if work_processes == -1:
            break_time += 1
        time += 1
    answer.append(str(end_time - break_time - 1))
    return answer
