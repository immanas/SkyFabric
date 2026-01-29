from decision_engine import (
    fetch_latest_intent,
    apply_decision_rules,
    generate_execution_plan
)

service_name = "orders-api"

intent = fetch_latest_intent(service_name)
print("INTENT:")
print(intent)

decision = apply_decision_rules(intent)
print("\nDECISION:")
print(decision)

plan = generate_execution_plan(decision)
print("\nEXECUTION PLAN:")
print(plan)
