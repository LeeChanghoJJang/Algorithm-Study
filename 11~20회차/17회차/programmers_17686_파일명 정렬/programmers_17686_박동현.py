def solution(files):
    tmp = []
    # files를 순회하면서
    for file_name in files :
        # check = False > 숫자가 아직 안나온 경우
        # check = True > 숫자가 나온 경우
        check = False
        # file_name의 각 철자를 순회하면서
        for i in range(len(file_name)):
            # 최초로 숫자가 나온 경우
            if not check and file_name[i].isnumeric():
                check=True
                # start에 저장
                start = i
            # 숫자가 끝난 경우
            elif check and not file_name[i].isnumeric():
                # end에 저장
                end = i
                break
        # 문자열의 마지막까지 number 부분인 경우
        else :
            # 마지막까지 슬라이싱 할 수 있도록 i+1저장
            end = i+1
        # 각 부분을 tmp에 리스트 형태로 저장
        tmp.append([file_name[:start],file_name[start:end],file_name[end:]])
    # 나눈 값의 header를 우선 비교하고, 이후에 number 부분의 값을 비교
    tmp.sort(key = lambda x : (x[0].lower(), int(x[1])))
    # 다시 합쳐서 answer에 저장
    answer = ["".join(i) for i in tmp]
    return answer