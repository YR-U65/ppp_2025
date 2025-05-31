import requests


def submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=False):
    base_url = "http://sfarm.digitalag.kr:8800/submission/create" #8800까지 따고 웹에 검색하면 제출기록 조회할 수 있음
    params = {
        "name": name,
        "affiliation": affiliation,
        "student_id": student_id,
        "param1": answer1,
        "param2": answer2,
        "param3": answer3,
        "param4": answer4,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        if verbose:
            print("응답 코드:", response.status_code)
            print("제출 성공! 응답:", response.text)
        return True
    except requests.exceptions.RequestException as e:
        if verbose:
            print("제출 중 오류 발생:", e)
        return False


def main():
    name = "홍길동"
    affiliation = "스마트팜학과"
    student_id = "202456789"

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)


if __name__ == "__main__":
    main()