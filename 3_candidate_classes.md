# Candidate Classes Analysis

| Class Candidate | Evidence in Requirements / Domain | Category | Justification |
| :--- | :--- | :--- | :--- |
| **User** | R1 (Register and log in) | Inferred | Base abstraction for Patient and Doctor authentication. |
| **Patient** | R1, R3, R4, R5 | Explicit | Primary actor who books and manages appointments. |
| **Doctor** | R2, R3, R6 | Explicit | Primary actor who manages slots and conducts appointments. |
| **Appointment** | R4, R5, R6 | Explicit | Core domain entity representing the booking relationship. |
| **TimeSlot** | R2, R3 | Inferred | Represents specific availability time units created by doctors. |
| **ClinicSystem** | R7 (Enforce business constraints) | Explicit | Controller/Manager handling limits (N=3) and workflows. |
| **NotificationService** | R7 (System notifications) | Rejected | Out of scope for core assignment domain logic. |
| **Database Connection** | Implementation detail | Rejected | Infrastructure concern, not a domain model candidate class. |
