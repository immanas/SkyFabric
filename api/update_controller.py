from guardrails import enforce_guardrails
import subprocess

def apply_update(terraform_vars: dict):

    # Step-6: Guardrails check (ADD HERE)
    guardrail_result = enforce_guardrails(terraform_vars)
    if not guardrail_result["allowed"]:
        return {
            "status": "BLOCKED_BY_GUARDRAILS",
            "reason": guardrail_result["reason"]
        }

    # Step-5: Safe execution
    plan = subprocess.run(
        ["terraform", "plan"],
        cwd="executor/terraform",
        capture_output=True,
        text=True
    )

    if plan.returncode != 0:
        return {"status": "PLAN_FAILED"}

    apply = subprocess.run(
        ["terraform", "apply", "-auto-approve"],
        cwd="executor/terraform",
        capture_output=True,
        text=True
    )

    if apply.returncode != 0:
        return {"status": "APPLY_FAILED", "action": "ROLLBACK"}

    return {"status": "UPDATE_SUCCESS"}
