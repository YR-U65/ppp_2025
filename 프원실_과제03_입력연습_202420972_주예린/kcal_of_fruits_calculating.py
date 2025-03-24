
#gpt의 도움을 열심히 받아 작성되었습니다.....아직 전부 다 짤 수 있는 참은 아닌 것 같아요

#파일 읽을 pandas 라이브러리를 가져와서 pd라고 간단하게 이름 부르기
import pandas as pd

#파일 경로 가져오기 (다른 컴퓨터에서는 그 파일 저장된 경로 가져와야함)
file_where = "C:/Users/user/Downloads/국가표준식품성분 Database 10.2 - 공개용_VF.xlsx"

#파일 시트 여러개 중에 어떤 시트 볼 건지
df = pd.read_excel(file_where, sheet_name = '국가표준식품성분 Database 10.1', header= 1)

'''pandas는 첫번째 행을 제대로 지정하지 않으면 무조건 [0](첫번째)행을 기준으로 잡음.
그래서 header = 1이라고 지정하지 않으면 자꾸 비어있는 데이터를 읽어서 오류가 남.
이런 이유로 첫번째 행의 기준을 [1](즉 엑셀 파일에서는 두번째 행)으로 수동 지정.'''

#과일 이름 입력 받기
fruit_ate = input("어떤 과일을 드셨나요?(명사) : ")

#입력받은 과일 이름이 식품명 중에 있는지 찾기
filter_fruit_ate = df[df['식품명'] == f"{fruit_ate}, 생것"]

'''등치문(==)를 쓰지 않고 and문(&)을 쓰면 입력받은 과일과 생것을 포함한 모든 데이터값이 선택됨.
따라서 아예 똑같은 값의 행에 있는 데이터만 가져올 수 있도록 제한을 건 것.'''

#없으면 없다고 하기
if filter_fruit_ate.empty: #filter_fruit_ate 값이 비어있을 경우
    print(f"{fruit_ate}이(가) 현재 목록에 없습니다. 다른 과일을 입력해주세요.")
    '''없는 걸 계산하라고 하니 오류가 남.... 그래서 if 문으로 빼줌'''

#있으면 진행
else:
    #거기서 kcal(1g당)는 얼마인지 값 가져오기
    kcal = filter_fruit_ate.iloc[0]['에너지']/100
    '''엑셀 값에서는 100g당 kcal니까 100으로 나눠서 1g당 kcal 구하기.'''
    '''.iloc는 그 데이터 값 중에 0번 인덱스의 값을을 가져오겠다는 소리.'''


    how_much_ate = int(input("얼마나 드셨나요?(g) : "))

    calorie_calculation = kcal * how_much_ate

    print(f"{fruit_ate}을(를) {how_much_ate}g 만큼 섭취하셨습니다. 섭취하신 총 칼로리는 {calorie_calculation}kcal 입니다.")
