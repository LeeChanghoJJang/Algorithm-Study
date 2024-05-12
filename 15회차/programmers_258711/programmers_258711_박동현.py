def solution(edges):
    input_count = [0 for _ in range(1000001)]
    output_count = [0 for _ in range(1000001)]
    created_node = -1
    doughnut_count = 0
    stick_count = 0
    eight_count = 0
    biggest_node_num = -1

    for a, b in edges:
        biggest_node_num = max(biggest_node_num, a, b)
        output_count[a] += 1
        input_count[b] += 1

    for i in range(1, biggest_node_num + 1):
        if input_count[i] == 0 and output_count[i] >= 2:
            created_node = i
        elif input_count[i] >= 1 and output_count[i] == 0:
            stick_count += 1
        elif input_count[i] >= 2 and output_count[i] == 2:
            eight_count += 1

    doughnut_count = output_count[created_node] - stick_count - eight_count
    return [created_node, doughnut_count, stick_count, eight_count]