CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
prompts = [
    {
        "id": 1,
        "title": "쿡트너 광고 영상 (15초)",
        "category": "영상 생성",
        "tags": ["광고", "영상", "쿡트너"],
        "favorite": False,
        "content": """0-1초
A Korean woman in her early 20s, a beginner cook, standing in a cozy 
wood-tone first-apartment kitchen, an open recipe book placed beside 
the induction cooktop, she picks up a wooden spoon and begins stirring 
a pot with a hopeful but slightly nervous expression, warm ambient 
kitchen lighting, static camera, realistic cinematic style, no text
1-2초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
she glances down at the recipe book, reading closely, then looks back 
at the pot, her expression focused and careful, warm lighting maintained, 
no text
2-3초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
she hesitates while adding an ingredient, unsure of the right amount, 
her movements slightly clumsy, showing she is inexperienced at cooking, 
warm lighting maintained, no text
3-4초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
she frowns slightly as the pot's contents don't look right, 
stirring faster now with growing concern, warm lighting maintained, no text
4-5초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
thin wisps of smoke begin rising from the pot on the induction cooktop, 
she is still focused on stirring, not yet noticing the smoke, 
warm lighting maintained, no text
5-6초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
she looks up and notices the smoke, her eyes widen in shock, 
mouth slightly open in surprise, smoke visibly thickening from the pot, 
warm lighting maintained, no text
6-7초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
panic spreads across her face, cold sweat visible on her forehead, 
she waves one hand frantically at the smoke while stepping back slightly, 
smoke continues rising from the burnt pot, warm lighting maintained, no text
7-8초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
she looks down at the blackened, ruined contents of the pot with 
a devastated expression, shoulders slumping in disappointment, 
smoke still lingering, warm lighting maintained, no text
8-9초
Same woman, same kitchen, same camera angle, continuing seamlessly, 
her expression crumples into a distressed, near-tearful look, 
she shouts a short line in Korean, saying "도와주세요!" with a desperate, 
pleading tone, her face showing genuine worry and helplessness, 
warm lighting maintained, no text
9-10초
Continuing directly from the previous clip, same kitchen, same woman, 
same lighting and camera angle, her tearful pleading expression still lingers, 
a warm golden glow begins forming at the center of the induction cooktop surface, 
like the beginning of soft magical light rising, no text
10-11초
Same kitchen, same woman, same camera angle, continuing seamlessly, 
the golden glow rises and takes the soft shape of a small fairy made of warm light, 
gentle sparkles floating around it, the woman's distressed expression 
shifts into surprise, she leans back slightly, no text
11-12초
Same kitchen, same woman, same camera angle, continuing seamlessly, 
the fairy is now fully formed, glowing warmly, light particles floating 
gently around it, it tilts toward the woman with a warm, friendly gesture 
as if about to speak, the woman's expression is a mix of shock and curiosity, 
no text
12-13초
Same kitchen, same woman, same camera angle, continuing seamlessly, 
the fairy gives a warm, gentle, reassuring gesture toward the woman with a 
calm and confident expression, the woman's expression softens from worry 
into relief, no text
13-14초
Same kitchen, same woman, continuing seamlessly, the woman's face relaxes 
into a small relieved smile as she looks at the fairy, the camera begins 
slowly moving in toward the induction cooktop surface, warm cozy atmosphere 
maintained, no text
14-15초
Camera slowly transitions into a close-up shot of the induction cooktop 
surface, revealing the fairy's face engraved onto the cooktop surface, 
glowing softly, a cute, warm, friendly fairy face design etched into the 
cooktop like a brand emblem, the word "Cooktner" appears beside the fairy face, 
merging together into a single finished logo mark, warm golden light 
emanating softly from both the fairy face and the logo text, the woman's 
relieved smiling face slightly visible in the soft-focus background, 
cozy warm kitchen atmosphere, the shot ends here as the final frame of 
the video, clean and legible logo typography, no other text, no subtitles""",
    },
    {
        "id": 2,
        "title": "KT 위즈 자동화 과제 - 핵심 프롬프트 모음",
        "category": "자동화",
        "tags": ["Make", "Discord", "KBO", "자동화"],
        "favorite": False,
        "content": """1. 과제 요구사항 전달

"1. [프로젝트 2] 자유 주제 자동화 설계 및 구현
   * 자동화할 반복 업무 1개 정의
   * 자동화 도구 1개 선정 및 선정 이유 작성
   * 워크플로우 설계 문서 (설명 또는 다이어그램 포함)
   * 구현 화면 캡처
   * 실행 결과 화면 캡처------ 이 프로젝트를 야구경기가 있는 날에 경기가 끝나고 결과가 나오는 자동화 설계를 하고 싶어."

2. 기능 요구사항 상세 전달

"기능 요구 사항
다음 요구사항을 모두 만족해야 한다.

1. 공통 요구 사항
   * 실제로 동작하는 자동화 워크플로우를 구현해야 한다.
      * Trigger 1개 이상 포함
      * Action 2개 이상 포함
      * 조건 분기(Filter/Router) 1개 이상 포함
   * 조건 분기 구조가 포함된 경우 각 분기 경로가 실제로 1회 이상 실행된 결과를 확인할 수 있어야 한다.
2. 프로젝트 1 요구 사항
   * 서로 다른 2개 이상의 자동화 도구를 사용한다.
   * 동일한 워크플로우 구조로 구현한다.
   * 비교 분석 보고서에는 아래 항목을 포함한다.
      * 사용한 도구 이름
      * 구현 과정 요약
      * 최소 5개 이상의 비교 항목 (예: UI/UX, 설정 난이도, 연동 서비스 범위, 무료 플랜 범위, 실행 로그 확인 방식 등)
      * 각 도구의 장단점 정리
      * 어떤 상황에서 적합한지 의견 작성
3. 프로젝트 2 요구 사항
   * 자동화할 반복 업무 1개를 정의한다.
   * 도구 1개를 선정하고 선정 이유를 작성한다.
   * 자동 실행 구조를 구현한다.
   * 워크플로우 흐름 설명을 포함한다.------- 이런 과제를 할 거야."

3. "야구경기 종료 및 결과를 알려주는 걸 만들고 싶어"

* 자동화할 반복 업무 1개 정의
* 자동화 도구 1개 선정 및 선정 이유 작성
* 워크플로우 설계 문서 (설명 또는 다이어그램 포함)
* 구현 화면 캡처
* 실행 결과 화면 캡처----- 이런 거를 만들려고 하는데 야구경기 종료 및 결과를 알려주는 걸 만들고 싶어

4. "경기 도중에 일어나는 사건을 알려줄 수는 없는 건가?"

5. "경기 종료,결과를 알려주고 베스트 플레이어를 알려주는 건 어때?"

6. "승리투수랑 결승타를 친 선수를 알려주는 건?"

7. "http를 사용하고 결과랑 승리 투수, 결승타를 친 타자를 알려주는 걸 하고싶은데"

그럼 http를 사용하고 결과랑 승리 투수, 그리고 결승타를 친 타자를 알려주는 걸 하고싶은데

8. "make로 만들어서 디스코드로 보내는 걸로 하고싶긴해"

그러면 이걸 make로 만들어서 디스코드로 보내는 걸로 하고싶긴해

9. "방금 보내준 링크가 한화랑 kt랑만 경기의 결과잖아 다음에는 어떻게 해야해?"

그런데 방금 보내준 링크가 한화랑 kt랑만 경기의 결과잖아 다음에는 어떻게 해야해?

10. "모듈이 늘어나지만 정확한 정보를 얻는 방식으로 했으면 좋겠어"

11. "승리투수·결승타는 이 API에 없음 이거는 안넣도 될거 같아"

12. "경기가 끝나는 시간이 항상 같진 않잖아 그러면 경기결과를 어떻게 받아?"

드디어 디스코드에 나왔어. 근데 이거 경기가 끝나는 시간이 항상 같진 않잖아 그러면 경기결과를 어떻게 받아?

13. "끝나지 않았거나 경기가 없을때 2nd를 사용한다는거야?"

14. "여태까지 만들었던 것들을 보기 좋게 보고서로 만들어 줄 수 있어? 증거용 이미지를 빼고 말이야"

15. "조건 분기 각 경로 1회 이상 실행 확인" 이게 뭔 뜻이지?"

16. "필터는 필요한데 그걸 없애면 안돼"

아니 필터는 필요한데 그걸 없애면 안돼""",
    },
    {
        "id": 3,
        "title": "AI의 대학 교육 영향 및 미래 전망 보고서 작성",
        "category": "텍스트 생성",
        "tags": ["AI", "교육", "보고서", "대학"],
        "favorite": False,
        "content": """너는 AI 전문가이자 보고서 작성 전문가다. AI가 대학교 학생들의 교육에 미치는 영향과 앞으로의 교육 행보를 예측하는 보고서를 작성해줘.

1. 결과물 형식
최종 결과물은 마크다운(.md) 파일로 작성해줘.
2. 분석 기간
2023년 1월부터 2026년 3월까지의 기간을 다룰거야. 이 기간 동안의 AI 발전과 그 발전이 우리에게 미친 영향을 먼저 작성하고, 그 다음 현재(2026년 3월 기준) 어떤 방식으로 발전하고 있는지를 작성해줘.
3. 독자와 목적
이 보고서는 대학교에 재학 중인 학생들과 대학 진학을 준비하는 고등학생들을 위한 보고서. 이들이 AI를 올바르게 이해하고 활용하는 데 도움을 주는 게 목적이야. 학생들이 쉽게 읽을 수 있도록 작성해줘.
4. 톤/문체
어조는 "~이다, ~한다"와 같은 평서문으로 작성해줘. 불필요한 장문의 추론 과정은 넣지 말고, 답변은 요약과 근거를 중심으로 간결하게 작성해줘.
5. 사실 검증 규칙

* 논문, 뉴스 기사 등을 조사해서 실제 있는 내용으로만 작성해줘.
* 조사해도 알 수 없는 내용은 "확인 불가"로 명시해줘.
* 참고한 논문, 기사, 문헌은 명확한 근거(출처 링크)와 함께 제시해줘.

6. 법적/윤리 제약
보고서는 법적·도덕적으로 문제가 없어야 하며, 개인정보 침해 소지가 없어야 해.
7. 보고서 구성
개요(목차, 핵심 메시지, 리스크)를 가장 먼저 넣고, 그 뒤에 본문을 구성해줘.""",
    },
    {
        "id": 4,
        "title": "라면 먹방 라이브 방송 영상/이미지 생성",
        "category": "영상 생성",
        "tags": ["먹방", "라면", "영상", "이미지"],
        "favorite": False,
        "content": """A high-quality video of a young adult South Korean male in his early 20s with short buzzed hair and sun-kissed skin, wearing a dark navy casual outfit. He is in his cozy bedroom with a wooden bookshelf in the background. He is performing a "Mukbang" (eating show) live stream. In front of him, there is a professional ring light and a camera setup on a desk. He holds chopsticks, lifting a large portion of steaming hot, curly ramen noodles from a white bowl to his open mouth, looking excited and happy. The camera slightly zooms in on his face and the noodles. Soft indoor lighting, illustrative/animated style, natural movements.""",
    },
]


def show_menu():
    print("\n1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def add_prompt():
    print("\n[프롬프트 추가]")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    print("\n카테고리를 선택하세요.")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}. {name}")
    print(f"{len(CATEGORIES) + 1}. 직접 입력")

    while True:
        choice = input("번호 선택: ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(CATEGORIES):
                category = CATEGORIES[num - 1]
                break
            if num == len(CATEGORIES) + 1:
                while True:
                    category = input("카테고리 직접 입력: ").strip()
                    if category:
                        break
                    print("카테고리는 비워둘 수 없습니다. 다시 입력해주세요.")
                break
        print("잘못된 번호입니다. 다시 선택해주세요.")

    new_id = prompts[-1]["id"] + 1 if prompts else 1

    prompts.append({
        "id": new_id,
        "title": title,
        "category": category,
        "tags": [],
        "favorite": False,
        "content": content,
    })

    print(f"\n프롬프트가 추가되었습니다. (id: {new_id})")


def show_list():
    print("\n[전체 프롬프트 목록]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, start=1):
        star = "⭐" if p["favorite"] else "  "
        print(f"{i}. {star} {p['title']} [{p['category']}]")


def show_by_category():
    print("\n[카테고리별 조회]")

    used = []
    for p in prompts:
        if p["category"] not in used:
            used.append(p["category"])

    if not used:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, name in enumerate(used, start=1):
        print(f"{i}. {name}")

    while True:
        choice = input("번호 선택: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(used):
            category = used[int(choice) - 1]
            break
        print("잘못된 번호입니다. 다시 선택해주세요.")

    found = [p for p in prompts if p["category"] == category]

    if not found:
        print(f"'{category}' 카테고리에 프롬프트가 없습니다.")
        return

    print(f"\n[{category}]")
    for i, p in enumerate(found, start=1):
        star = "⭐" if p["favorite"] else "  "
        print(f"{i}. {star} {p['title']}")


def search_prompt():
    print("\n[프롬프트 검색]")

    while True:
        keyword = input("검색어: ").strip()
        if keyword:
            break
        print("검색어는 비워둘 수 없습니다. 다시 입력해주세요.")

    found = []
    for p in prompts:
        if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower():
            found.append(p)

    if not found:
        print(f"'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    print(f"\n검색 결과: {len(found)}개")
    for i, p in enumerate(found, start=1):
        star = "⭐" if p["favorite"] else "  "
        print(f"{i}. {star} {p['title']} [{p['category']}]")


def show_detail():
    print("\n[프롬프트 상세 보기]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, start=1):
        print(f"{i}. {p['title']}")

    while True:
        choice = input("번호 선택: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(prompts):
            target = prompts[int(choice) - 1]
            break
        print("잘못된 번호입니다. 다시 선택해주세요.")

    star = "⭐" if target["favorite"] else "없음"

    print("\n" + "=" * 40)
    print(f"제목: {target['title']}")
    print(f"카테고리: {target['category']}")
    print(f"즐겨찾기: {star}")
    print("-" * 40)
    print(target["content"])
    print("=" * 40)


def toggle_favorite():
    print("준비 중입니다.")


def show_favorites():
    print("준비 중입니다.")


def main():
    print("프롬프트 매니저 프로그램을 시작합니다.")
    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()
        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()