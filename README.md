# 🌐 SkyFabric

✨ **SkyFabric** is a **central system** that lets you describe **what you want**,  and then **handles everything needed to make it run and stay healthy** across cloud environments.

🧠 You tell SkyFabric **your intent**:
> “I want my service running in production, always available, and not expensive.”

⚙️ SkyFabric then:
- Decides **where** it should run ☁️
- Deploys it **correctly** 🚀
- Continuously **watches it** 👀
- **Fixes issues or alerts humans** when something goes wrong 🚨

🤝 You stop manually managing infrastructure.  
🎯 You focus on building software.  

💡 **In short:**  
SkyFabric replaces cloud chaos with **one calm, central control** 🌈

---


## 🧩 Real-Life Problems Developers Face (Without SkyFabric)

> In many real companies, infrastructure is spread across clouds:
> - **AWS** for backend services  
> - **GCP** for data and analytics  
> - **Azure** for authentication or enterprise integrations  

| 🚧 Core Problem Area | 😣 What Developers Actually Face in Real Life |
|---------------------|----------------------------------------------|
| Fragmented environments | Backend on AWS, data on GCP, auth on Azure — no single place to manage everything |
| Manual service deployments | Separate deployment logic and workflows for each cloud and environment |
| No single source of truth | Unclear which service version is running where and with which configuration |
| Configuration drift | Manual changes in one cloud silently break production stability |
| Slow incident response | During outages, teams first struggle to identify **which cloud** is failing |
| Inconsistent security rules | Strong IAM rules in one cloud, misconfigured or open access in another |
| Hidden cost behavior | AWS, GCP, and Azure bills grow independently with no unified explanation |

💡 **These problems appear daily in real production teams and grow worse as systems scale across clouds.**


---

## 🔄 How SkyFabric Changes the Developer Experience (Before → After)

| 🚧 Without SkyFabric (Before) | ✅ With SkyFabric (After) |
|------------------------------|--------------------------|
| Services managed separately across AWS, GCP, and Azure | One central system manages services across all clouds |
| Manual, cloud-specific deployments | One intent-driven deployment flow |
| Engineers unsure what is running where | Clear visibility into service state and placement |
| Configuration drift causes unexpected failures | Desired state defined once and continuously enforced |
| Slow and confusing incident investigation | Faster detection of mismatches and failures |
| Security rules differ per cloud | Consistent security and access enforcement |
| Cost issues discovered only after billing | Central visibility into cost-related behavior |

💡 **With SkyFabric, developers describe what they want once,  
and the platform takes responsibility for making reality match that intent.**

---

## 💡 What SkyFabric Does (Very Simply)

SkyFabric becomes the **boss of your cloud**.

Instead of people touching the cloud directly:

> People say:  
> **“I want my service to be highly available and low cost.”**

SkyFabric then:
- Decides **how** to do it
- Checks if it is **safe**
- Blocks **bad changes**
- Applies infrastructure via Terraform
- Detects **drift** continuously

---

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

---
## 🧱 Architecture Overview

```text
User / Team
   │
   ▼
Intent API (FastAPI)
   │
   ▼
Decision Engine (Rules)
   │
   ▼
Guardrails (Policy Checks)
   │
   ▼
Execution Plan
   │
   ▼
Terraform Executor
   │
   ▼
Cloud (AWS)
```

---

## 🔁 How SkyFabric Works (Step-by-Step)

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

---

### 3️⃣ Decision Engine
- Converts intent → decision plan  
- Example:
  - high availability → multi-instance  
  - low cost → cost-optimized

---

### 4️⃣ Guardrails (Safety)
- Blocks unsafe, expensive, or forbidden changes
- Prevents outages, cost spikes, and human mistakes

---

### 5️⃣ Execution
- Approved plan → Terraform variables
- Terraform applies cloud infrastructure

---

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
