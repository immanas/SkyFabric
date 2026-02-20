# 🌐 SkyFabric

✨ **SkyFabric** is a **central system** that lets you describe **what you want**,  and then **handles everything needed to make it run and stay healthy** across cloud environments.

🧠 You tell SkyFabric **your intent**:
> “I want my service running in production, always available, and not expensive. ”


## 🧩 Real-Life Problems Developers Face (Without SkyFabric)

> In many real companies, infrastructure is spread across clouds:
> - **AWS** for backend services  
> - **GCP** for data and analytics  
> - **Azure** for authentication or enterprise integrations  
## 🔄 Problem → Transformation with SkyFabric

| 🚧 Real Problem Area | 😣 What Happens Without SkyFabric (Reality) | ✅ How SkyFabric Fixes It |
|---------------------|--------------------------------------------|--------------------------|
| Fragmented environments | Backend on AWS, data on GCP, auth on Azure — no unified control | One central system manages services across all clouds |
| Manual deployments | Separate deployment logic per cloud and environment | Single intent-driven deployment workflow |
| No source of truth | Engineers unsure what is running where | Clear visibility into service state and placement |
| Configuration drift | Manual changes silently break production stability | Desired state defined once and continuously enforced |
| Slow incident response | Teams struggle to identify which cloud is failing | Faster detection of mismatches and failures |
| Inconsistent security | Different IAM rules across clouds, leading to gaps | Consistent security and access enforcement |
| Hidden cost behavior | Bills grow independently without clear explanation | Central visibility into cost-related behavior |

💡 SkyFabric shifts the model from:
"managing infrastructure manually" → "declaring intent and letting the system enforce it"

## 📈 Core Features :

| ✅ What This Project IS | ❌ What This Project is NOT |
|------------------------|---------------------------|
| Intent-Based Control Plane — Defines infrastructure using high-level intent and desired state | Not a manual infrastructure management approach |
| Policy-Aware Orchestration — Enforces rules and constraints during provisioning via Terraform | Not an ad-hoc or script-based deployment system |
| Single Source of Truth — Maintains a consistent, declarative representation of infrastructure state | Not a fragmented system with multiple state definitions |
| State Reconciliation Engine — Continuously compares desired vs actual state and detects drift | Not a one-time deployment tool without validation |
| Infrastructure Automation Backend — Focused on execution, control, and lifecycle management | Not a UI-first or dashboard-centric platform |
| Deterministic Infrastructure Behavior — Predictable outcomes based on defined intent and policies | Not a probabilistic or ML-driven infrastructure system |
| Terraform-Driven Execution — Uses proven IaC workflows for provisioning and updates | Not a custom-built provisioning engine replacing Terraform |
| Production-Oriented Design — Built for real infrastructure control and lifecycle management | Not a demo or conceptual architecture without execution |


## 🧠 Simple Mental Model (Uber Analogy)

Think of **SkyFabric like Uber for infrastructure**:

| Uber | SkyFabric |
|---|---|
| You say where to go | You say what you want |
| Uber decides route | SkyFabric decides infra |
| Driver executes | Terraform executes |
| Uber monitors trip | SkyFabric reconciles state |

You never drive the car.  
You never touch the cloud.

## 🧱 System Architecture (Single Source of Truth) :
![Architecture Diagram](skyfebric.png)

## 🧱 Design Rationale (Why This Architecture) :

- **Intent-Driven Model**: Separates *what the user wants* from *how it is implemented*, reducing human error.
- **Terraform as Executor**: Leverages proven IaC tooling instead of reinventing cloud provisioning logic.
- **PostgreSQL as Source of Truth**: Ensures durable, versioned storage of intents and execution state.
- **Reconciliation Loop**: Prevents silent drift by continuously comparing desired and actual cloud state.
- **Control Plane Pattern**: Mirrors real platform-engineering systems used in production environments.


## ## 🔄 Request Lifecycle (End-to-End) :

### 1️⃣ Submit Intent

```http
POST /intents
Example:
{
  "service_name": "orders-api",
  "environment": "production",
  "availability": "high",
  "cost": "low"
}
```

### 2️⃣ Intent Stored
- Stored immutably in PostgreSQL
- Becomes the single source of truth

### 3️⃣ Decision Engine
- Converts intent → decision plan  
- Example:
  - high availability → multi-instance  
  - low cost → cost-optimized

### 4️⃣ Guardrails (Safety)
- Blocks unsafe, expensive, or forbidden changes
- Prevents outages, cost spikes, and human mistakes

### 5️⃣ Execution
- Approved plan → Terraform variables
- Terraform applies cloud infrastructure

### 6️⃣ Reconciliation (Drift Detection)
- Compares desired state vs actual state
- Reports **IN_SYNC** or **DRIFTED**
- Prevents silent infrastructure drift

###📡 Visibility (Status API)
SkyFabric exposes full system visibility:

```http GET /status/{service_name}
🧪 Example Output
{
  "service_name": "orders-api",
  "decision": {
    "availability_plan": "multi-instance",
    "cost_plan": "cost-optimized"
  },
  "execution_plan": {
    "actions": [
      { "type": "deploy_service" },
      { "type": "configure_availability" },
      { "type": "apply_cost_policy" }
    ]
  },
  "reconciliation_status": "IN_SYNC"
}

```
## 🛠 Tech Stack :

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **IaC:** Terraform
- **Cloud:** AWS
- **Architecture:** Control Plane + Reconciliation Loop

## ▶️ How to Run Locally (Minimal) :

```bash
# Start API
uvicorn main:app --reload

# Initialize Terraform
terraform init

# Apply execution plan
terraform apply
```


## 🛡️ Resilience & Security :

### Failure Scenarios
- Terraform apply failures handled with **retry + rollback strategy**
- Partial infrastructure failures do not corrupt global state
- State inconsistencies detected via **reconciliation loop**
- Execution logs stored for debugging and traceability

### Security Considerations
- **IAM-based access control** for execution permissions  
- Separation of **intent definition vs execution roles**  
- No hardcoded credentials (secure secret handling assumed)  
- Policy engine enforces **guardrails before execution**  

### Scalability & Performance
- Stateless control components → horizontally scalable  
- Terraform executions isolated per request  
- Database (PostgreSQL) supports consistent state tracking  
- Async processing enables handling multiple infra requests
- 
## 🧠 Engineering Philosophy :

***Key Decisions***
- Intent-based design > imperative scripts  
  → Separates *what you want* from *how it's executed*, reducing human error and making infra predictable and repeatable  

- Terraform as execution engine > custom provisioning  
  → Uses a battle-tested ecosystem (providers, state management, plan/apply lifecycle) instead of rebuilding fragile infra logic  

- Reconciliation loop > one-time deployment  
  → Infrastructure is not static — continuous drift detection ensures system always converges back to desired state  

- Policy-first validation > post-deployment fixes  
  → Prevents bad infrastructure *before it is created*, instead of reacting after damage is done  

- Backend-first system > UI-first approach  
  → Prioritizes correctness, control, and automation over visuals — UI can be added later, core system must be solid first  
Voice chat ended

***Trade-offs & Decisions***
- No real-time instant provisioning (Terraform latency exists)  
- Increased system complexity due to reconciliation logic  
- Strong dependency on Terraform ecosystem  
- Requires well-defined policies to avoid misconfigurations  

***Explicit Limitations***
- Not multi-cloud abstraction at API level (cloud-specific configs required)  
- No built-in UI/dashboard (backend-focused system)  
- Drift correction depends on detection interval  
- Not optimized for extremely high-frequency infra changes


## 🔮 Future Enhancements

- Multi-cloud execution (AWS / GCP / Azure)
- Policy-as-code (OPA / Sentinel)
- Auto-reconciliation loop
- Web dashboard
- CI/CD integration


### 🛠️ How to Contribute

1. 🍴 Fork the repo
2. 📦 Create a new feature branch: `git checkout -b feature-name`
3. ✅ Make your changes and test them
4. 📬 Submit a pull request describing your enhancement

 🤝 Let's Build This Together!
Made with 🤍 by **Manas Gantait**  
