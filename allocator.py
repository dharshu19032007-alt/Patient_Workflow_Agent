from models.database import Doctor

def allocate_doctor(issue):

    doctor = Doctor.query.filter_by(status="Available").first()

    return doctor
