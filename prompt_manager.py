print("프롬프트 매니저 프로그램을 시작합니다.") 
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
        "category": "업무 자동화",
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
]

print("프롬프트 매니저 프로그램을 시작합니다.")
print(f"등록된 프롬프트: {len(prompts)}개")