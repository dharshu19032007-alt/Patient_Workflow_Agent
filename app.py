from flask import Flask, render_template, request
from models.database import db, Doctor, Appointment

app = Flask(__name__)

@app.route("/book", methods=["POST"])
def book():

    patient_id = request.form.get("patient_id")
    patient_name = request.form.get("patient_name")
    issue = request.form.get("issue")
    category = request.form.get("category")
    date = request.form.get("date")

    # simple doctor selection
    doctor = Doctor.query.filter_by(status="Available").first()

    if not doctor:
        return render_template("book_appointment.html", message="No doctor available")

    appointment = Appointment(
        patient_id=patient_id,
        patient_name=patient_name,
        issue=issue,
        category=category,
        date=date,
        doctor_id=doctor.id
    )

    db.session.add(appointment)
    db.session.commit()

    return render_template(
        "book_appointment.html",
        message=f"Appointment booked with Dr {doctor.name}"
    )
