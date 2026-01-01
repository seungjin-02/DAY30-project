# State Definition

## DEGRADED

### Question this state answers
- 이 상태는 "현재 시스템이 인간 판단에 영향을 주어도 되는가?"라는 질문에 답한다.

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
- 제
