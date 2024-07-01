n, w, L = map(int, input().split())
list_ = list(map(int, input().split()))
bridge = [0] * w
time_ = 0

while bridge:
    time_ += 1
    bridge.pop(0)

    if list_:
        if sum(bridge) + list_[0] <= L:
            bridge.append(list_.pop(0))
        else:
            bridge.append(0)

print(time_)