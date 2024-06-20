T = int(input())
tc = list(map(str,range(1,T+1)))

for idx in range(T):
    if "3" in tc[idx] or "6" in tc[idx] or "9" in tc[idx]:
        clap = tc[idx].count("3")+tc[idx].count("6")+tc[idx].count("9")
        tc[idx] = "-"*clap
print(*tc)