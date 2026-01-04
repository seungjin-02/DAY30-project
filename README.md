# DAY30-project
AI judgment boundary &amp; state-based decision system

## What This System is
- 본 시스템은 AI가 결정을 내리지 않도록 설계된, 판단 책임 분리 기반의 자동화 보조 시스템이다.
- 자동화는 규칙 평가까지만 수행되며, 판단과 책임은 항상 인간에게 귀속된다.

---

## Design Principles
이 프로젝트의 모든 동작은 아래 문서들을 절대 기준으로 한다.
- `governance/decision-boundary.md`
- `governance/transition-rules.md`
- `governance/design-cutline.md`
- `governance/state-definition.md`

본 README는 위 문서들을 요약하지 않으며, 이를 대체하지 않는다.

---

## What This System Intentionally Does Not Do
- 판단을 자동화하지 않는다. (시스템은 조건을 평가할 수 있으나, 선택·결정·책임을 수행하지 않는다.)
- 상태나 결과를 원인으로 해석하지 않는다. (상태는 관측 결과이며, 전이는 규칙의 결과로만 발생한다.)
- 반복, 성공률, 일관성을 자동화 확장의 근거로 사용하지 않는다. (잘 작동한다는 사실은 권한을 확장할 이유가 아니다.)
- 모델 추론 결과나 점수를 전이 또는 판단의 직접 입력으로 사용하지 않는다. (해석 결과는 관측값이 아니다.)
- 인간의 판단을 패턴화하거나 규칙으로 흡수하지 않는다. (판단은 명시적 행위로만 존재하며, 축적되지 않는다.)
- 기술적으로 가능하다는 이유로 설계 경계를 완화하지 않는다. (미구현은 한계가 아니라 선택이다.)

---

## Why This Matters
- 자동화의 확장은 성능 문제가 아니라 책임과 경계의 문제이기 때문이다.
- 본 시스템은 더 많은 자동화를 지향하지 않으며, 멈춰야 할 지점을 명확히 설명할 수 있도록 설계되었다.
