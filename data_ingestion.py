import io
import pandas as pd
from sqlalchemy.orm import Session
from models import SensorStream

REQUIRED_COLS = ["timestamp", "accel_x", "accel_y", "accel_z", "emg", "spo2", "hr", "step_count"]

def parse_and_store(csv_bytes: bytes, patient_id: int, db: Session):
    df = pd.read_csv(io.BytesIO(csv_bytes))
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    feats = {
        "avg_hr": float(df["hr"].mean()),
        "avg_spo2": float(df["spo2"].mean()),
        "steps_total": int(df["step_count"].sum()),
        "emg_peak": float(df["emg"].max()),
        "accel_mag_mean": float(((df["accel_x"]**2 + df["accel_y"]**2 + df["accel_z"]**2)**0.5).mean())
    }

    head = df.head(30).to_dict(orient="records")
    s = SensorStream(patient_id=patient_id, sensor_type="wearable_csv", payload={"preview": head, "features": feats})
    db.add(s)
    db.commit()

    return df.head(30), feats
