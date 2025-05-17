

def encoding(text, n):
    if text == " ":
        return " "
    C_txt_num = ord(text) + n
    if C_txt_num > 90 and C_txt_num < 97 or C_txt_num > 122:
        return chr(C_txt_num-26)
    else:
        return chr(C_txt_num)
    

def encoding_sentence(text, n):
    full_txt = []
    for txt in text:
        encode_text = encoding(txt, n)
        full_txt.append(encode_text)
    return "".join(full_txt)


def check_sentence(sentence):
    try:
        for txt in sentence:
            if 65 <= ord(txt) <= 90 or 97 <= ord(txt) <= 122:
                return txt
            else:
                return "error"
            
    except ValueError:
        return "error"



def main():
    shift_n = 3
    while True:
        sentence = input("암호화 하고 싶은 문장을 입력하세요. : ")
        if check_sentence(sentence) == "error":
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
        else:
            print(encoding_sentence(sentence, shift_n))
            break


if __name__ == "__main__":
    main()