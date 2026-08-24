# Actors & Use Cases

**Problem Statement #34 — Digital Gift Card & Loyalty Point Exchange**
**SRN:** PES1UG24CS221

---

## 1. Actors

| Actor | Type | Description / Purpose |
|-------|------|-----------------------|
| **Account Holder** | Primary (human) | Links loyalty accounts, converts points to universal exchange credits, redeems digital gift cards, and views transaction history. |
| **Merchant Partner** | Primary (human/organisation) | Provides the loyalty program and configures the dynamic exchange rate for its loyalty points. |
| **Loyalty Program System** | Secondary (external system) | External brand loyalty system that provides and validates loyalty-point balances during linking and conversion. |

> The lab requires **at least three actors and at least five use cases** — satisfied below.
> The Account Holder and Merchant Partner are named explicitly in the problem statement;
> the Loyalty Program System is a reasonable inference from the requirement to *aggregate and
> validate merchant loyalty points*.

---

## 2. Use Cases

| Use Case ID | Use Case | Primary Actor | Related Requirement |
|-------------|----------|---------------|---------------------|
| **UC-01** | Link & Aggregate Loyalty Accounts | Account Holder | FR-002 |
| **UC-02** | Convert Points to Exchange Credits | Account Holder | FR-001, FR-003 |
| **UC-03** | Redeem Digital Gift Card | Account Holder | FR-004 |
| **UC-04** | Validate & Lock Voucher | (system, invoked via UC-03) | FR-001, FR-004, NFR-002 |
| **UC-05** | Configure Dynamic Exchange Rate | Merchant Partner | FR-005 |
| **UC-06** | View Transaction History | Account Holder | — |
| **UC-07** | Validate Loyalty Points | Merchant Partner / Loyalty Program System | FR-001, FR-002 |
| **UC-08** | Flag Suspicious Redemption | (system, extends UC-03) | NFR-002 |

---

## 3. Relationships (for the UML diagram)

- **«include»** — *Convert Points to Exchange Credits* (UC-02) **always includes** *Validate Loyalty Points* (UC-07): points must be validated against the loyalty system before they can be converted.
- **«include»** — *Redeem Digital Gift Card* (UC-03) **always includes** *Validate & Lock Voucher* (UC-04): every redemption generates and locks a single-use voucher to prevent reuse.
- **«extend»** — *Flag Suspicious Redemption* (UC-08) **optionally extends** *Redeem Digital Gift Card* (UC-03): only abnormal/suspicious redemption attempts trigger the extra fraud-handling behaviour; normal redemptions run unchanged.

> Note on the business flow: conversion (UC-02) does **not** generate a gift-card voucher.
> Vouchers are generated and locked only during redemption (UC-03 → UC-04). This keeps the
> sequence consistent: *loyalty points → validate → convert to exchange credits → redeem gift
> card → validate & lock voucher*.

---

## 4. Actor–Use-Case Connections

```
Account Holder ─── UC-01 Link & Aggregate Loyalty Accounts
              ├──── UC-02 Convert Points to Exchange Credits
              ├──── UC-03 Redeem Digital Gift Card
              └──── UC-06 View Transaction History

Merchant Partner ─── UC-05 Configure Dynamic Exchange Rate
                └──── UC-07 Validate Loyalty Points

Loyalty Program System ─── UC-01 Link & Aggregate Loyalty Accounts
                      └──── UC-07 Validate Loyalty Points
```

These are visualised in [UseCase_Diagram.md](UseCase_Diagram.md).
