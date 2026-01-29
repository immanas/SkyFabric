import subprocess
import json
from decision_engine import (
    fetch_latest_intent,
    apply_decision_rules,
    generate_execution_plan
)

def get_desired_and_planned_state(service_name: str):
    intent = fetch_latest_intent(service_name)
    if not intent:
        return None, None

    decision = apply_decision_rules(intent)
    plan = generate_execution_plan(decision)

    return intent, plan


def get_actual_state():
    """
    Reads Terraform state as actual state
    """
    try:
        result = subprocess.run(
            ["terraform", "show", "-json"],
            cwd="executor/terraform",
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return None
        return json.loads(result.stdout)
    except Exception:
        return None


def detect_drift(plan: dict, actual_state: dict):
    if actual_state is None:
        return "UNKNOWN"

    if len(
        actual_state
        .get("values", {})
        .get("root_module", {})
        .get("resources", [])
    ) == 0:
        return "DRIFT_DETECTED"

    return "IN_SYNC"


def reconcile(service_name: str):
    intent, plan = get_desired_and_planned_state(service_name)
    if not intent:
        return {"status": "NO_INTENT"}

    actual = get_actual_state()
    drift_status = detect_drift(plan, actual)

    return {
        "service_name": service_name,
        "reconciliation_status": drift_status
    }
