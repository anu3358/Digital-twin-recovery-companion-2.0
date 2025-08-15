from sqlalchemy.orm import Session
from models import AuditLog

def log_action(db: Session, user_id: int, action: str, details: dict | None = None):
    try:
        log = AuditLog(user_id=user_id, action=action, details=details or {})
        db.add(log)
        db.commit()
    except Exception:
        db.rollback()
