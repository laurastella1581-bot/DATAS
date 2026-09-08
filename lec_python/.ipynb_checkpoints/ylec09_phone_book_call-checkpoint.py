from ylec09_phone_book import PhoneBook

addr_list = []
pb = PhoneBook()
while (True):
    print("_______________________________________________")
    print("1:등록 2:수정 3:삭제 4:조회 Q: 종료")
    menu = input("메뉴를 선택하세요")

    if (menu in ["Q", "q"]):
        print("종료")
        break  # ------------------------------

    elif (menu == "1"):
       addr_list = pb.save(addr_list)


    elif (menu == "2"):
        print("수정")
        search_name = input("수정하려는 사람의 이름을 입력하세요")
        update_tel = input("변경될 전화번호을 입력하세요")
        for v in addr_list:
            if v[0] == search_name:
                v[1] = update_tel

    elif (menu == "3"):
        print("삭제")
        search_name = input("삭제하려는 사람의 이름을 입력하세요")
        for v in addr_list:
            if v[0] == search_name:
                addr_list.remove(v)


    elif (menu == "4"):
        print(f"{len(addr_list)}건 조회")
        for v in addr_list:
            print(v)
    else:
        print(f"잘못된 메뉴 번호를 선택하셨습니다.")