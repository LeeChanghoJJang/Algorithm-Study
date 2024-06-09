def solution(files):
    answer = []
    file_names = []
    for idx, file in enumerate(files):
        H = 0
        N = len(file)
        for i in range(len(file)):
            if file[i].isdecimal():
                H = i
                break

        for j in range(H, len(file)):
            if not file[j].isdecimal():
                N = j
                break

        head = file[:H].upper()
        num = int(file[H:N])
        file_names.append((head, num, idx))

    file_names.sort()

    for h, n, i in file_names:
        answer.append(files[i])
        
    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

print(solution(files))