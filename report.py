from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime
from io import BytesIO

def generate_report(patient_name: str, metrics: dict) -> bytes:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFillColorRGB(0.18, 0.5, 0.93)
    c.rect(0, height-60, width, 60, fill=1, stroke=0)
    c.setFillColorRGB(1,1,1)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(2*cm, height - 40, "Digital-Twin Recovery Companion")

    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 12)
    c.drawString(2*cm, height - 80, f"Patient: {patient_name}")
    c.drawString(2*cm, height - 98, f"Generated: {datetime.utcnow().isoformat()}Z")

    y = height - 130
    c.setFont("Helvetica-Bold", 14)
    c.drawString(2*cm, y, "Key Metrics")
    y -= 18
    c.setFont("Helvetica", 12)
    for k, v in metrics.items():
        c.drawString(2*cm, y, f"• {k}: {v}")
        y -= 16

    c.showPage()
    c.save()
    return buffer.getvalue()
