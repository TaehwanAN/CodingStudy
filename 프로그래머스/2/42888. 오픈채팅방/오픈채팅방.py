# 명령 종류: Enter, Leave, Change
# 전체 순회 구조: 두 개의 for 문
## 첫 for: {유저아이디: 닉네임} => Enter일 경우 create, Change 일경우 update
## 두 번째 for: Enter와 Leave 확인하여 결과 리스트에 추가

def get_id_nick_dict(record):
    id_nick_dict ={}
    for r in record:
        r_list = r.split(" ")
        if r_list[0]=='Enter' or r_list[0] == 'Change':
            id_nick_dict[r_list[1]] = r_list[-1]
    return id_nick_dict

def get_message(r, id_nick_dict):
    r_list = r.split(" ")
    action = ""
    if r_list[0] == "Enter":
        action = "님이 들어왔습니다."
    elif r_list[0] == "Leave":
        action = "님이 나갔습니다."
    else:
        return None
    return f"{id_nick_dict[r_list[1]]}{action}"

def solution(record):
    answer = []
    id_nick_dict = get_id_nick_dict(record)
    # print(id_nick_dict)
    # print(get_message(record[0],id_nick_dict))
    for r in record:
        result = get_message(r,id_nick_dict)
        if result:
            answer.append(result)
    return answer