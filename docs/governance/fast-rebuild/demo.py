state = "STABLE"
human_action_required = False

signals = {
    "collision": True,
    "error": False
}

if state == "STABLE":
    state = "DEGRADED"
  
if state == "DEGRADED":
    if signals["collision"] or signals["error"]:
        state = "HUMAN_REQUIRED"
        human_action_required = True

result = {
    "state": state,
    "human_action_required": human_action_required
}

print(result)
