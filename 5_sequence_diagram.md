# Sequence Diagram: Book Appointment Flow

```mermaid
sequenceDiagram
    autonumber
    actor P as Patient
    participant CS as ClinicSystem
    participant A as Appointment
    participant TS as TimeSlot

    P->>CS: book_appointment(doctor, time_slot)
    CS->>P: get_upcoming_appointments_count()
    P-->>CS: return count

    alt count < 3 (Validation Success)
        CS->>A: create(patient, doctor, time_slot)
        CS->>TS: mark_booked()
        TS-->>CS: status = booked
        CS-->>P: Booking Confirmed (Appointment Object)
    else count >= 3 (Limit Exceeded)
        CS-->>P: Error: Maximum appointment limit reached (N = 3)
    end
