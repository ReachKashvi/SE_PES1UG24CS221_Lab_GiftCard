# Actors & Use Cases

**Problem Statement #34 — Digital Gift Card & Loyalty Point Exchange**
**SRN:** PES1UG24CS221

---

## 1. Actors

| Actor | Type | Description / Purpose |
|-------|------|-----------------------|
| **Account Holder** | Primary (human) | End user who links loyalty accounts, converts points to credits, and redeems digital gift cards. |
| **Merchant Partner** | Primary (human/organisation) | Brand that issues loyalty points and configures dynamic exchange rates and validity windows. |
| **Payment / Settlement Gateway** | Secondary (external system) | External service that settles the monetary value of redeemed gift cards and confirms funds. |
| **Fraud / Voucher-Locking Service** | Secondary (system) | Subsystem that locks single-use vouchers and flags duplicate/expired redemptions. |

> The lab requires **at least three actors and at least five use cases** — satisfied below.

---

## 2. Use Cases

| Use Case ID | Use Case | Primary Actor | Related Requirement |
|-------------|----------|---------------|---------------------|
| **UC-01** | Link & Aggregate Loyalty Accounts | Account Holder | FR-002 |
| **UC-02** | Convert Points to Exchange Credits | Account Holder | FR-001, FR-003 |
| **UC-03** | Redeem Digital Gift Card | Account Holder | FR-004 |
| **UC-04** | Validate & Lock Voucher (anti-fraud) | Fraud/Voucher-Locking Service | FR-001, FR-004 |
| **UC-05** | Configure Dynamic Exchange Rate | Merchant Partner | FR-005 |
| **UC-06** | Authenticate User | Account Holder / Merchant Partner | NFR-002 |

---

## 3. Relationships (for the UML diagram)

- **«include»** — *Convert Points to Exchange Credits* (UC-02) **always includes** *Validate & Lock Voucher* (UC-04): every conversion generates a locked single-use voucher, so the validation step is mandatory reuse.
- **«include»** — *Redeem Digital Gift Card* (UC-03) **always includes** *Validate & Lock Voucher* (UC-04).
- **«extend»** — *Redeem Digital Gift Card* (UC-03) **is optionally extended by** *Apply Promotional Bonus* : when a merchant promotion is active, extra bonus credit is added; otherwise the base flow runs unchanged.
- **«include»** — *Convert Points to Exchange Credits* (UC-02) and *Redeem Digital Gift Card* (UC-03) both **include** *Authenticate User* (UC-06).

These are visualised in [UseCase_Diagram.md](UseCase_Diagram.md).
