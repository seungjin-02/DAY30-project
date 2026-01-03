# Decision Boundary

## Scope
본 시스템에서 자동화가 허용되는 범위와
판단 책임이 귀속되는 지점을 정의한다.

## Fixed Boundaries
- 시스템은 판단을 수행하지 않는다.
- 전이는 규칙 평가의 결과로만 발생한다.
- AI는 요약·정리·가시화만 수행한다.
- 판단 책임은 항상 인간에게 귀속된다.
- 
## Prohibited Capabilities
- AI 기반 전이 결정
- 조건부 자동화 예외
- 전이 결과의 자동 평가
- 인간 판단을 우회하는 모든 로직


## Enforcement Rules
- 규칙 충돌 시 자동 전이 중단
- 불확실성 증가 시 HUMAN_REQUIRED 고정
- 정의되지 않은 입력 발생 시 판단 위임


## Change Policy
- 수정은 설계 철학 변경으로 간주한다.
- 모든 변경은 별도 결정 로그에 기록한다.
