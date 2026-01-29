from fastapi import FastAPI
from database import get_db_connection
import json

app = FastAPI(title="SkyFabric Control Plane")


@app.get("/")
def root():
    return {"status": "SkyFabric API is running"}


@app.post("/intents")
def create_intent(intent: dict):
    # Step-1.5: minimal required validation
    if "service_name" not in intent or "environment" not in intent:
        return {"error": "service_name and environment are required"}

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO intents (service_name, environment, desired_state)
        VALUES (%s, %s, %s)
        """,
        (
            intent["service_name"],
            intent["environment"],
            json.dumps(intent)
        )
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Intent stored successfully"}


@app.get("/intents/{service_name}")
def get_intent(service_name: str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT service_name, environment, desired_state, created_at
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
        return {"message": "Intent not found"}

    return {
        "service_name": row[0],
        "environment": row[1],
        "desired_state": row[2],
        "created_at": row[3]
    }
from status_api import get_system_status

@app.get("/status/{service_name}")
def status(service_name: str):
    return get_system_status(service_name)
