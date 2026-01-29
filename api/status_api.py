from reconciler import reconcile
from decision_engine import (
    fetch_latest_intent,
    apply_decision_rules,
    generate_execution_plan
)

def get_system_status(service_name: str):
    intent = fetch_latest_intent(service_name)

    if not intent:
        return {
            "service_name": service_name,
            "status": "NO_INTENT"
        }

    decision = apply_decision_rules(intent)
    plan = generate_execution_plan(decision)
    reconciliation = reconcile(service_name)

    return {
        "service_name": service_name,
        "intent": intent,
        "decision": decision,
        "execution_plan": plan,
        "reconciliation_status": reconciliation["reconciliation_status"]
    }
