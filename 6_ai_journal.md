# AI Journal & Verification Record

## Prompt Log & Verification Checklist
1. **P1 (Requirements):** Checked requirement mapping. Corrected FR/NFR split for $N=3$ constraint.
2. **P2 & P3 (Use Cases & Mermaid UC Diagram):** Verified alternative flow logic when $N=3$ limit is exceeded.
3. **P4 (Candidate Classes):** Verified explicit vs inferred categories; rejected `NotificationService` and database details.
4. **P5 (Class Diagram):** Ensured class relationships match candidate classes and $N=3$ attribute constraint.
5. **P6 (Sequence Diagram):** Added `alt / else` block for constraint validation step.
6. **P7 (Implementation):** Verified OOP implementation against class diagram and checked runtime execution.

---

## AI Incorrect Outputs & Corrections Log

### Misconception 1: Hardcoded Unlimited Appointments
- **What the AI said:** The AI initially generated a standard booking logic without enforcing the $N = 3$ maximum active upcoming appointments constraint.
- **Why it was wrong:** It violated requirement R4, which strictly limits patients to $N=3$ active appointments.
- **How it was noticed:** Noticed during Class & Sequence Diagram alignment verification.
- **Correction:** Added `MAX_LIMIT = 3` and `get_upcoming_appointments_count()` logic in both diagrams and `main.py`.

### Misconception 2: Diagram Attribute Mismatch
- **What the AI said:** The AI omitted the `is_booked` attribute in `TimeSlot` in the initial class diagram draft.
- **Why it was wrong:** Without `is_booked`, checking slot availability dynamically in Python runtime was impossible.
- **How it was noticed:** Noticed when mapping `main.py` back to `4_class_diagram.md`.
- **Correction:** Updated both `4_class_diagram.md` and `main.py` to include `is_booked: bool`.

---

## Output of `main.py`
