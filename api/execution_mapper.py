def map_execution_plan_to_terraform_vars(execution_plan: dict):
    """
    Step-3.2: Convert execution plan into Terraform variables
    """

    terraform_vars = {
        "service_name": execution_plan["service_name"],
        "environment": execution_plan["environment"],
        "instance_count": 1,
        "instance_type": "t3.medium"
    }

    # Availability mapping
    for action in execution_plan["actions"]:
        if action["type"] == "configure_availability":
            if action["mode"] == "multi-instance":
                terraform_vars["instance_count"] = 2

        # Cost mapping
        if action["type"] == "apply_cost_policy":
            if action["mode"] == "cost-optimized":
                terraform_vars["instance_type"] = "t3.micro"

    return terraform_vars
