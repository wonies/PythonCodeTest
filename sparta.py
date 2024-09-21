import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def check_outdated_students():
    # 웹사이트 URL
    url = "https://scc.backoffice.spartacodingclub.kr/superTightManagement/64190608d428f819058cc8b3"


    # 웹페이지 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 오늘 날짜 가져오기
    today = datetime.now()

    # 테이블에서 모든 행 가져오기
    rows = soup.select('tbody tr')

    # 7일 이상 경과된 수강생 정보 저장 리스트
    outdated_students = []

    for row in rows:
        # 관리현황, 수강생 이름, 업데이트 일시 가져오기
        management_status = row.select_one('td:nth-of-type(7)').text.strip()
        name = row.select_one('td:nth-of-type(5) a').text.strip()
        update_date_str = row.select_one('td:nth-of-type(8) p').text.strip()
        
        # '완주-전환 완료'나 '완주 완료' 상태인 경우 건너뛰기
        if management_status in ["완주-전환 완료", "완주 완료"]:
            continue

        # 날짜 문자열을 datetime 객체로 변환
        update_date = datetime.strptime(update_date_str, '%Y-%m-%d')

        # 날짜 차이 계산
        date_diff = (today - update_date).days

        # 7일 이상 경과했다면 리스트에 추가
        if date_diff >= 7:
            outdated_students.append((management_status, name, update_date_str))

    # 가장 긴 관리현황 문자열의 길이 찾기
    max_status_length = max(len(status) for status, _, _ in outdated_students)

    # 결과 출력
    print("\n" + "=" * 80)
    print("7일 이상 경과된 수강생 명단")
    print("(완주-전환 완료와 완주 완료 제외)")
    print("=" * 80)

    if not outdated_students:
        print("해당하는 수강생이 없습니다.")
    else:
        for i, (status, name, date) in enumerate(outdated_students, 1):
            print(f"{i:2d}. {status:<{max_status_length}}. | {name:<10}. | {date:<15}. |")

    print("=" * 80)
    print(f"총 {len(outdated_students)}명")
    print("=" * 80)

    input("\n프로그램을 종료하려면 Enter 키를 누르세요...")

if __name__ == "__main__":
    check_outdated_students()