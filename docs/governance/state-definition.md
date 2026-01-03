# State Definition

## DEGRADED

### Question this state answers
- 이 상태는 "현재 시스템이 인간 판단에 영향을 주어도 되는가?" 라는 질문에 답한다.

### Definition
- DEGRADED 상태란,
  추가 정보 제공이나 사소한 개입만으로도
  인간 판단의 방향이 왜곡될 수 있어
  시스템이 판단을 유도하거나 강화해서는 안 되는 상태다.

### Allowed actions
- 상태 유지
- 인간 개입 요청 (HUMAN_REQUIRED)

### Forbidden actions
- 요약
- 점수화
- 추천
- 추가 추론
- 새로운 판단 근거를 생성하거나, 기존 판단을 강화하는 정보를 추가로 생성하는 출력

### Semantic Boundary (의미 경계)

이 상태는 다음 질문에 답하지 않는다:

- 판단이 적절한지, 안전한지에 대한 평가
- 전이가 필요한지, 정당한지에 대한 판단
- 다른 state의 상태를 전제로 한 설명이나 해석

이 상태는 자신의 상태 값(DEGRADED)과
그 지속 여부만을 표출한다.

### Transition related responsibilities (전이 관련 책임)


이 state는 전이를 정의하지 않으며,
전이의 필요성, 적절성, 정당성을 판단하지 않는다.
전이는 사전에 정의된 외부 규칙 계층에서만 발생한다.
