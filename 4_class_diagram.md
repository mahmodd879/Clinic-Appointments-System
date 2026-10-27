# Class Diagram

```mermaid
classDiagram
    class User {
        +int user_id
        +str name
        +str email
        +login()
    }

    class Patient {
        +int max_appointments
        +book_appointment(doctor, time_slot)
        +cancel_appointment(appointment_id)
        +get_upcoming_appointments_count()
    }

    class Doctor {
        +str specialty
        +add_time_slot(time_slot)
        +get_schedule()
    }

    class TimeSlot {
        +int slot_id
        +str date_time
        +bool is_booked
    }

    class Appointment {
        +int appointment_id
        +str status
        +cancel()
        +complete()
    }

    class ClinicSystem {
        +int MAX_LIMIT = 3
        +validate_booking(patient)
    }

    User <|-- Patient
    User <|-- Doctor
    Doctor "1" -- "0..*" TimeSlot : manages
    Patient "1" -- "0..*" Appointment : books
    Doctor "1" -- "0..*" Appointment : conducts
    Appointment "1" -- "1" TimeSlot : scheduled_for
    ClinicSystem ..> Appointment : enforces N=3
