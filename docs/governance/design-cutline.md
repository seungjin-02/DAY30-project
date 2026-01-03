# Design Cutline

## Intentional Non-Implementation (의도적 비구현)

본 시스템은 DEGRADED 상태에서
판단 정확도를 높이기 위한 추가 추론,
보조 판단, 추천 알고리즘을
의도적으로 구현하지 않는다.

이는 기술적 한계나 구현 난이도 때문이 아니라,
판단 책임이 시스템에서 인간으로
조용히 이전되는 것을 방지하기 위한
설계적 선택이다.

## Separation of transition responsibilities (전이 책임 분리)

- 전이는 state의 결과로 발생하지 않는다.
- 전이는 decision의 판단으로 발생하지 않는다.
- 전이는 사전에 정의된 규칙 계층에서만 발생한다.

이로써 상태 표현과 시스템 변화의 책임을 분리한다.  

## Transition Rule Principles (전이 규칙 원칙)

- 규칙은 판단하지 않는다.
- 규칙은 목적을 가지지 않는다.
- 규칙은 인간 행위를 전이의 원인으로 삼지 않는다.
- 규칙은 조건이 충족될 경우 전이를 발생시킨다.
