# State Definition

## DEGRADED

### Question this state answers
DEGRADED는 시스템에서 관측되는 상태 값 중 하나이다.

이 상태 값은 특정 조건 하에서 시스템이 추가 출력을 생성하지 않아야 함을 나타낸다.

### Observable Properties
- DEGRADED 값의 존재 여부
- DEGRADED 상태의 지속 시간

---

### Non-Causal Declaration
DEGRADED 상태는 전이를 발생시키지 않는다.

DEGRADED 상태는 전이의 필요성, 적절성, 정당성을 판단하지 않는다.

DEGRADED 상태는 다른 상태의 의미를 해석하지 않는다.

---

### Usage Constraints
DEGRADED 상태 값이 존재하는 동안 시스템은 다음 행위를 수행하지 않는다.
- 요약 생성
- 점수화
- 추천 생성
- 추가 추론 수행
- 새로운 판단 근거 생성
- 기존 판단을 강화하는 출력 생성

---

### Transition related responsibilities
DEGRADED 상태는 전이를 정의하지 않는다.

모든 전이는 사전에 정의된 규칙 계층에서만 발생한다.
