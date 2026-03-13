class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    patient_name = db.Column(db.String(100))
    issue = db.Column(db.String(100))
    category = db.Column(db.String(50))
    date = db.Column(db.String(20))
    doctor_id = db.Column(db.Integer)
