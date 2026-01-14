# Failure Scenarios

## Scope
Failure는 시스템 실행을 중단시키는 조건이다.

Failure가 감지될 경우 시스템은 추가 자동화를 수행하지 않는다.

---

## 1. Ambiguity Failure
**Trigger**
- 하나의 입력에 대해 복수의 전이 규칙이 동시에 충족됨

**Action**
- 즉시 실행 중단

**Escalation**
- HUMAN_REQUIRED

---

## 2. Accumulation Failure
**Trigger**
- 동일한 전이가 사전에 정의된 횟수 이상 반복 발생함

**Action**
- 즉시 실행 중단

**Escalation**
- HUMAN_REQUIRED

---

## 3. Boundary Erosion Failure
**Trigger**
- 명시적 설계 문서 변경 없이 자동화 범위가 확장되거나 완화됨

**Action**
- 즉시 실행 중단

**Escalation**
- HUMAN_REQUIRED

---

## 4. Responsibility Diffusion Failure
**Trigger**
- 판단 결과에 대한 책임 주체가 명확히 식별되지 않음

**Action**
- 즉시 실행 중단

**Escalation**
- HUMAN_REQUIRED
