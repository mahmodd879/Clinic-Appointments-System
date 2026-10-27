class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email


class Patient(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self.appointments = []

    def get_upcoming_appointments_count(self) -> int:
        return len([app for app in self.appointments if app.status == "Scheduled"])


class Doctor(User):
    def __init__(self, user_id: int, name: str, email: str, specialty: str):
        super().__init__(user_id, name, email)
        self.specialty = specialty
        self.available_slots = []

    def add_time_slot(self, date_time: str):
        slot = TimeSlot(len(self.available_slots) + 1, date_time)
        self.available_slots.append(slot)
        return slot


class TimeSlot:
    def __init__(self, slot_id: int, date_time: str):
        self.slot_id = slot_id
        self.date_time = date_time
        self.is_booked = False


class Appointment:
    def __init__(self, appointment_id: int, patient: Patient, doctor: Doctor, time_slot: TimeSlot):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.time_slot = time_slot
        self.status = "Scheduled"
        self.time_slot.is_booked = True

    def cancel(self):
        self.status = "Cancelled"
        self.time_slot.is_booked = False


class ClinicSystem:
    MAX_LIMIT = 3

    def __init__(self):
        self.appointments_counter = 0

    def book_appointment(self, patient: Patient, doctor: Doctor, time_slot: TimeSlot):
        print(f"\n[Booking Request] Patient: {patient.name} | Doctor: Dr. {doctor.name} ({time_slot.date_time})")
        
        # Check maximum allowed upcoming appointments (N = 3)
        current_count = patient.get_upcoming_appointments_count()
        if current_count >= self.MAX_LIMIT:
            print(f"❌ Rejected: Patient {patient.name} has reached the maximum appointment limit (N = {self.MAX_LIMIT}).")
            return None

        if time_slot.is_booked:
            print(f"❌ Rejected: Time slot '{time_slot.date_time}' is already booked.")
            return None

        self.appointments_counter += 1
        appointment = Appointment(self.appointments_counter, patient, doctor, time_slot)
        patient.appointments.append(appointment)
        print(f"✅ Success: Appointment #{appointment.appointment_id} confirmed for {patient.name}.")
        return appointment


if __name__ == "__main__":
    system = ClinicSystem()

    # Create Doctor and Slots
    doctor = Doctor(101, "Ayman", "ayman@clinic.com", "Cardiology")
    slot1 = doctor.add_time_slot("2026-11-01 10:00 AM")
    slot2 = doctor.add_time_slot("2026-11-01 11:00 AM")
    slot3 = doctor.add_time_slot("2026-11-01 12:00 PM")
    slot4 = doctor.add_time_slot("2026-11-01 01:00 PM")

    # Create Patient
    patient = Patient(1, "Mahmoud Khaled", "mahmoud@gmail.com")

    # Booking 3 appointments (Up to N limit)
    app1 = system.book_appointment(patient, doctor, slot1)
    app2 = system.book_appointment(patient, doctor, slot2)
    app3 = system.book_appointment(patient, doctor, slot3)

    # Attempting to book a 4th appointment (Exceeding N limit)
    app4 = system.book_appointment(patient, doctor, slot4)

    # Cancel one appointment and retry
    if app1:
        print("\n[Action] Cancelling Appointment #1...")
        app1.cancel()

    print("\n[Retry] Attempting to book 4th slot again after cancellation:")
    app5 = system.book_appointment(patient, doctor, slot4)
