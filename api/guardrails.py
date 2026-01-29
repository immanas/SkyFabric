def enforce_guardrails(terraform_vars: dict):
    """
    Step-6: Security & Cost Guardrails
    """

    # Cost guardrail
    if terraform_vars.get("instance_count", 0) > 3:
        return {
            "allowed": False,
            "reason": "Instance count exceeds allowed limit"
        }

    # Cost guardrail
    if terraform_vars.get("instance_type") in ["t3.large", "t3.xlarge"]:
        return {
            "allowed": False,
            "reason": "Instance type too expensive"
        }

    # Environment guardrail
    if terraform_vars.get("environment") == "production":
        if terraform_vars.get("instance_count", 0) < 2:
            return {
                "allowed": False,
                "reason": "Production requires at least 2 instances"
            }

    return {
        "allowed": True
    }
