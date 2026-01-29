from database import get_db_connection
import json


def fetch_latest_intent(service_name: str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT desired_state
        FROM intents
        WHERE service_name = %s
        ORDER BY created_at DESC
        LIMIT 1
        """,
        (service_name,)
    )

    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        return None

    return row[0]


def apply_decision_rules(intent: dict):
    """
    Step-2.2: Apply simple rules to intent
    Output is a DECISION PLAN, not execution
    """

    decision = {
        "service_name": intent["service_name"],
        "environment": intent["environment"],
        "deployment_strategy": "standard",
        "availability_plan": "single-instance",
        "cost_plan": "balanced"
    }

    # Availability rule
    if intent.get("availability") == "high":
        decision["availability_plan"] = "multi-instance"

    # Cost rule
    if intent.get("cost") == "low":
        decision["cost_plan"] = "cost-optimized"

    return decision
def generate_execution_plan(decision: dict):
    """
    Step-2.3: Convert decision into execution plan
    This plan will be used later by Terraform / cloud layer
    """

    execution_plan = {
        "service_name": decision["service_name"],
        "environment": decision["environment"],
        "actions": []
    }

    # Deployment action
    execution_plan["actions"].append({
        "type": "deploy_service",
        "strategy": decision["deployment_strategy"]
    })

    # Availability action
    execution_plan["actions"].append({
        "type": "configure_availability",
        "mode": decision["availability_plan"]
    })

    # Cost optimization action
    execution_plan["actions"].append({
        "type": "apply_cost_policy",
        "mode": decision["cost_plan"]
    })

    return execution_plan
