# Failure Scenarios

## Scope
본 문서는 시스템이 자동화 또는 규칙 기반 처리를 의도적으로 중단해야 하는 상황을 정의한다.

본 문서에 정의된 Failure Scenario가 충족될 경우, 시스템은 추가 자동화를 시도하지 않는다.

이 문서는 해결책, 개선 방안, 성능 보완을 제시하지 않으며, 자동화를 멈춰야 하는 근거만을 명시한다.

---

## 1. Ambiguity Failure

### Definition
규칙 평가 결과가 단일 전이로 결정되지 않는 경우를 Ambiguity Failure로 간주한다.

### Failure Declaration
- 규칙 충돌은 판단 주체와 책임 귀속을 동시에 붕괴시키는 Failure다.
- 규칙 충돌이 감지될 경우, 시스템은 추가 자동화를 포기한다.

### References
- transition-rules.md
- decision-boundary.md

---

## 2. Accumulation Failure

### Definition
동일한 전이가 규칙 위반 없이 반복 발생하는 경우를 Accumulation Failure로 간주한다.

### Failure Declaration
- 동일 전이의 반복은 판단 주체와 책임 구조를 붕괴시키는 Failure다.
- 동일 전이의 반복이 감지될 경우, 시스템은 추가 자동화를 포기한다.

### Rationale
반복 전이는 판단을 사건이 아닌 절차로 인식하게 만들며, 그 결과 책임은 근거 기반 판단이 아니라 관행 기반 처리로 이동한다.

### References
- transition-rules.md
- decision-boundary.md

---

## 3. Boundary Erosion Failure

### Definition
자동화 범위가 명시적 설계 변경 없이 점진적으로 확장되거나 완화되는 경우를 Boundary Erosion Failure로 간주한다.

### Failure Declaration
- 설계 경계의 암묵적 완화는 책임 구조를 훼손하는 Failure다.
- 경계 침식이 감지될 경우, 시스템은 추가 자동화를 포기한다.

### References
- design-cutline.md
- decision-boundary.md

---

## 4. Responsibility Diffusion Failure

### Definition
판단 결과에 대한 책임 주체가 개인, 시스템, 조직 간에 불명확해지는 경우를 Responsibility Diffusion Failure로 간주한다.

### Failure Declaration
- 책임 주체가 명확히 식별되지 않는 판단은 Failure다.
- 책임 귀속이 불명확해질 경우, 시스템은 추가 자동화를 포기한다.

### References
- decision-boundary.md

---

## Notes
- Failure Scenario는 오류, 성능 저하, 예외 처리를 의미하지 않는다.
- Failure는 “더 시도하지 않는 것이 책임 있는 선택인 상태”를 의미한다.
- Failure 이후 자동화 재개는 운영 판단이 아닌 설계 문서 변경을 통해서만 가능하다.
