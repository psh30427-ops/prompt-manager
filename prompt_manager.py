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
        "title": "KT 위즈 자동화 과제 프롬프트 기록",
        "category": "업무 자동화",
        "tags": ["Make", "Discord", "KBO", "자동화"],
        "favorite": False,
        "content": """# KT 위즈 자동화 과제 — 프롬프트 기록

## 1. 과제 요구사항 파악

1. "1. [프로젝트 2] 자유 주제 자동화 설계 및 구현
   * 자동화할 반복 업무 1개 정의
   * 자동화 도구 1개 선정 및 선정 이유 작성
   * 워크플로우 설계 문서 (설명 또는 다이어그램 포함)
   * 구현 화면 캡처
   * 실행 결과 화면 캡처------ 이 프로젝트를 야구경기가 있는 날에 경기가 끝나고 결과가 나오는 자동화 설계를 하고 싶어."

2. "기능 요구 사항
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

3. "* 자동화할 반복 업무 1개 정의
* 자동화 도구 1개 선정 및 선정 이유 작성
* 워크플로우 설계 문서 (설명 또는 다이어그램 포함)
* 구현 화면 캡처
* 실행 결과 화면 캡처----- 이런 거를 만들려고 하는데 야구경기 종료 및 결과를 알려주는 걸 만들고 싶어"

## 2. 자동화 범위 설정 (무엇을 알려줄지)

4. "api 없이 만들 수도 있는거지?"
5. "경기 도중에 일어나는 사건을 알려줄 수는 없는 건가?"
6. "그러면 api 토큰이 많이 드는거지?"
7. "그러면 경기 종료,결과를 알려주고 베스트 플레이어를 알려주는 건 어때?"
8. "그럼 승리투수랑 결승타를 친 선수를 알려주는 건?"

## 3. 데이터 소스 조사 (HTTP/API/RSS)

9. "[네이버 스포츠](https://m.sports.naver.com/game/20260903HHKT02026/record)"
10. "그럼 htp나 rss를 써야하나?"
11. "HTTP를 사용하려면 api를 꼭 사용해야하는거야?"
12. "그럼 http를 사용하고 결과랑 승리 투수, 그리고 결승타를 친 타자를 알려주는 걸 하고싶은데"

## 4. 구현 착수 — 데이터 구조 확인

13. "그럼 처음은 뭐부터해야해?"
14. "어떤 링크?"
15. "네이버 스포츠로 들어가지고 어제 경기에 대한 정보가 나왔어"
16. "이거 어제 정보가 아닌데"
17. "[네이버 스포츠](link)---- 이거가 9/3 의 경기정보야"
18. [스크린샷 첨부: 경기 상세 기록 화면] "이런 식으로 진행되는 중이야."
19. [스크린샷 첨부: 스코어보드 화면]

## 5. Make + Discord로 방향 결정

20. "그러면 이걸 make로 만들어서 디스코드로 보내는 걸로 하고싶긴해"
21. "그러면 처음에 어떤 앱을 통해서 모듈을 만들어야해?"
22. "Schedule post를 말하는 거야?"
23. "없는데?"

## 6. HTTP 모듈 구현

24. [스크린샷 첨부: HTTP 모듈 Authentication] "해결했어 그리고는?"
25. "https://m.sports.naver.com/kbaseball/schedule/index?date=2026-09-04----- 근데 이걸 집어 넣으면 9월4일만 지정되는거 아니야?"
26. "너가 보내준 링크를 그대로 써도 된다는거지?"
27. [스크린샷 첨부: URL 필드에 formatDate 함수 입력됨] "이런 식으로 진행되는 중이야."
28. [스크린샷 첨부: HTTP 실행 결과 Output] "이렇게 나왔어"
29. "`schedule`이나 `games` 같은 단어가 포함된 항목을 찾아서 클릭 이거는 안보이는 거 같은데?"
30. [스크린샷 첨부: Network 탭 요청 목록] "지금 이런 상황이야"
31. [스크린샷 첨부: Network 탭 필터 후 목록] "이런데"
32. [스크린샷 첨부: API 응답 400 에러] "이렇게 나오는데?"
33. [스크린샷 첨부: 잘린 URL 주소창] "이거 아닌가?"
34. "[Request URL 전체 텍스트]"
35. "https://api-gw.sports.naver.com/schedule/games?...&fromDate={{formatDate(now; \"YYYY-MM-DD\")}}&toDate={{formatDate(now; \"YYYY-MM-DD\")}}&size=500----- 이거를 넣으라는거지?"
36. [스크린샷 첨부: HTTP 실행 성공 결과] "이게 맞나?"
37. [스크린샷 첨부: Data/result/games 구조] "이게 맞나?"
38. "7번을 열었을때 kt가 나왔어"
39. [스크린샷 첨부: games[6] 필드 목록] (gameId, statusCode 등)

## 7. 범위 확장 논의 (다음 경기 자동 조회)

40. "그런데 방금 보내준 링크가 한화랑 kt랑만 경기의 결과잖아 다음에는 어떻게 해야해?"
41. "모듈이 늘어나지만 정확한 정보를 얻는 방식으로 했으면 좋겠어"
42. "Schedule 이거 make에는 없잖아"
43. "다시 계획을 설정해줘."

## 8. 승리투수/결승타 → 단순화 결정

44. "승리투수·결승타는 이 API에 없음 이거는 안넣도 될거 같아"

## 9. Iterator / Filter 구현

45. "1번은 했어"
46. [스크린샷 첨부: HTTP URL 필드] "이제는 뭐 해야해?"
47. "모듈은 하나야"
48. "Iterator 이거 없는데?"
49. "그리고?"
50. [스크린샷 첨부: 필드 목록 검색 결과] "이거 맞아?"
51. "검색했는데 안나와"
52. "homeTeamCode 이건 나오는데 kt가 안나오는데?"
53. [스크린샷 첨부: Filter 조건 설정 화면] "이거 맞나?"
54. "and로만 바꾸면 되는거지?"
55. "or로만 바꾸면 되는거지?"
56. "그 다음에는?"
57. [스크린샷 첨부: Iterator→Router 연결 화면] "여기서?"

## 10. Discord 웹훅/모듈 연결

58. "디스코드에 내 주소를 넣는 건가?"
59. "디스코드 주소를 어떻게 넣어야해?"
60. "서버로 추가하는거지?"
61. "서버랑 연결하는 건 맞는거야?"
62. "디스코드에서 뭘 골라야해?"
63. "모듈에서 말하는 거야?"
64. [스크린샷 첨부: Discord 모듈 목록] "이거에서"
65. "채널을 어떻게 집어넣어?"
66. [스크린샷 첨부: Discord 모듈 설정 화면] "여기서는?"
67. "일반이라고 뜨는데?"
68. [스크린샷 첨부: Discord Message 필드 "테스트"] "이게 맞나?"

## 11. 테스트 및 트러블슈팅

69. "테스트 메세지가 안왔어"
70. "경기가 종료가 안되어서 그런건 아니지?"
71. "그냥 원래 만드려는 거를 테스트 안하고 만들면 안되나?"
72. "⚾ 경기종료 - {{homeTeamName}} {{homeTeamScore}} : {{awayTeamScore}} {{awayTeamName}}----- 이거를 어디에 집어 넣어야해?"
73. "너가 만들어준 거 그대로 복사해서 넣어도 되는 건가?"
74. "대괄호는 내가 직접 넣어야해?"
75. [스크린샷 첨부: Message 필드 완성 화면] "이러면 된거야?"
76. "경기 종료해서 실행했는데 안되는데?"
77. [스크린샷 첨부: 캔버스 실행 배지] "이런데 결과는 안나온거 같아"
78. [스크린샷 첨부: Router 필터 설정] "이게 아닌가?"
79. [스크린샷 첨부: statusCode 필터 조건] "이런데"
80. "안되는데?"
81. "드디어 디스코드에 나왔어. 근데 이거 경기가 끝나는 시간이 항상 같진 않잖아 그러면 경기결과를 어떻게 받아?"

## 12. 스케줄 설정

82. "11시에 설정하려면?"
83. "시계가 안보여"
84. "DAILY가 매일 한번만 되는 건가?"
85. "그리고 세이브 하려는데 save and activate가 뜨는데 지금 실행하냐고 물어보는 건가?"
86. "그러면 프로젝트는 끝난건가?"

## 13. 경기 취소 분기 추가

87. "끝나지 않았거나 경기가 없을때 2nd를 사용한다는거야?"
88. "취소면 샌드 메세지가 맞는건가?"
89. "cancel = true를 할 때 뭘 넣어야해?"
90. [스크린샷 첨부: cancel 필터 설정] "이거 맞지?"
91. "그리고 또 수정해야하는게 뭐가 있을까?"

## 14. 프로젝트 1과의 구분 확인

92. "1. [프로젝트 1] 자동화 도구 비교 구현 ... [전체 요구사항 재게시] ------- 이거 다 한건가?"
93. "프로젝트1은 저번에 했어"

## 15. 보고서 작성 요청

94. "* 자동화할 반복 업무 1개 정의 ... 프로젝트2에대한 걸 보고서로 만들어줘."
95. "이거를 깃허브에 그대로 넣으면 볼 수 없어?"
96. "응"
97. "마크다운 파일로 만들 수 있어?"
98. "압축을 해제하면 여러개의 파일로 나누어지잖아?"
99. "그러면 깃허브에 들어가게 되는 파일이 늘어 나잖아"
100. "줄여서 만들어줘."

## 16. 평가 피드백 대응

101. "[자동 채점 평가 결과 전문 붙여넣기] 이렇다는데?"
102. [스크린샷 첨부: 연속 실행 로그] (파일만 첨부, 텍스트 없음)
103. "[자동화도구_비교분석_보고서_증거포함__1_.docx 첨부]" (파일만 첨부)
104. "사진 파일은 깃허브에 올리면 깨지니까 따로 올렸는데 예전 사진이랑 달라진 건 없는거지?"
105. "마크다운 파일로 수정해줘."
106. "그러면 이제 문제되는 건 없지?"
107. "부족한 점
민감정보(토큰/API Key/비밀번호) 노출 여부를 명시적으로 증명할 문구나 제거 로그가 없음
보완
파일/스크린샷에서 민감정보가 없음을 확인하는 문구 또는 민감정보 마스킹 스크린샷 추가,  평가 항목 #4
부족한 점
프로젝트2의 '무중단 자동실행' 증빙(실행 로그/연속 실행 히스토리/스크린샷) 미제출
보완
프로젝트2의 Trigger가 연속 동작함을 보여주는 실행 로그 또는 연속 실행 스크린샷 첨부 이게 부족해서 fail이라는데 어떻게해야하지?"

## 17. 최종 정리 요청

108. "여태까지 만들었던 것들을 보기 좋게 보고서로 만들어 줄 수 있어? 증거용 이미지를 빼고 말이야"
109. [스크린샷 첨부: 최종 워크플로우 화면] "이게 자동화가 되는 증거로 충분하지 않아?"
110. "디스코드에 실행 된 결과가 나온거가 필요한거야?"
111. "내가 너한테 보내줬던 거 같은데?"
112. "그럼 이제 문제되는 건 없지?"
113. "조건 분기 각 경로 1회 이상 실행 확인" 이게 뭔 뜻이지?"
114. "그럼 어떻게 증명해야할까?"
115. [스크린샷 첨부: Router 2nd 경로 빈 상태] "여기서 어떻게 해야해?"
116. "경기 취소가 없어서 안된거 같은데"
117. "{{3.statusCode}},{{3.statusCode}} 이게 들어 있는데 바꿔야 하는 거지?"
118. "안되는 거 같은데?"
119. "* 저장은 됐는데 Run once를 눌러도 2nd 경로에 실행 배지가 안 뜨나요?
* Discord에 메시지가 안 오나요?---- 이거 두개가 문제인 듯"
120. "없어"
121. "아니 필터는 필요한데 그걸 없애면 안돼"
122. "https://api-gw.sports.naver.com/schedule/games?...---- 이거를 어떻게 수정하라고?"
123. [스크린샷 첨부: Discord 채널 최종 실행 결과] "이러면 된건가?"
""",
    },
]

print("프롬프트 매니저 프로그램을 시작합니다.")
print(f"등록된 프롬프트: {len(prompts)}개")