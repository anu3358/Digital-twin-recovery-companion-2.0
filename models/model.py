import numpy as np

class TwinModel:
    def __init__(self):
        pass

    def predict(self, patient_id, scenario=None, feats=None):
        base = 10.0
        extra = 0.0
        if scenario and isinstance(scenario, dict):
            extra = float(scenario.get("extra_minutes_balance", 0)) * 0.4
        feat_bonus = 0.0
        if feats:
            feat_bonus += (feats.get("avg_spo2", 95) - 92) * 0.2
            feat_bonus += (feats.get("avg_hr", 80) - 70) * -0.1
            feat_bonus += (feats.get("steps_total", 1000) / 1000.0) * 0.5

        gait_speed_change_pct = round(max(2.0, min(35.0, base + extra + feat_bonus + np.random.uniform(-2, 2))), 2)
        adherence_score = round(max(60.0, min(100.0, 80 + extra*0.5 + np.random.uniform(-5, 5))), 1)

        return {
            "gait_speed_change_pct": gait_speed_change_pct,
            "adherence_score": adherence_score
        }
