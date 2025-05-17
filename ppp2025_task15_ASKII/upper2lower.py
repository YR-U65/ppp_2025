

def toggle_text(text: str):
    character_num = ord(text)
    if character_num >= 65 and character_num <= 90 :
        u2l_character = chr(character_num+32)
    else: #character_num >= 97 and character_num <= 122:
        u2l_character = chr(character_num-32)

    return u2l_character


def main():
    
    while True:
        try:
            character = input("알파벳을 입력하세요. : ")
            if 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
                break
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")
        except ValueError:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
    
    print(f"{character} -> {toggle_text(character)}") 


if __name__ == "__main__":
    main()