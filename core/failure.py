# Responsibility: 중단 조건을 감지하고 실행을 차단한다
def guard_failure(context, rule_result): ...
    if _failure_detected(context):
        raise StopAutomation
