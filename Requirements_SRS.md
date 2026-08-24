# Software Requirements Specification (SRS) — Requirements Table

**Problem Statement #34 — Digital Gift Card & Loyalty Point Exchange**
**SRN:** PES1UG24CS221

This single file contains **both** the Functional Requirements (FR-001 → FR-005)
and the Non-Functional Requirements (NFR-001, NFR-002), each with a measurable
acceptance criterion and a rationale, formatted as an SRS table.

---

## 1. Functional Requirements

| Req ID | Type | Description ("The system shall…") | Priority | Acceptance Criteria (Pass / Fail) | Rationale |
|--------|------|-----------------------------------|----------|-----------------------------------|-----------|
| **FR-001** | Functional | The system shall validate merchant loyalty points, convert them into universal exchange tokens, and generate single-use digital voucher codes. | High | **Pass:** Voucher code generated with a cryptographic checksum. **Fail:** An expired or duplicate voucher is redeemed. | Core value proposition — turns fragmented brand points into spendable, verifiable credit. |
| **FR-002** | Functional | The system shall allow an Account Holder to link multiple brand loyalty accounts and aggregate their point balances into a single wallet view. | High | **Pass:** After linking, the wallet shows the combined balance of all linked brands within 3 s. **Fail:** A linked brand's points are missing or double-counted. | Aggregation is the entry point for every conversion and redemption flow. |
| **FR-003** | Functional | The system shall compute the point-to-credit conversion using the current dynamic exchange rate and display the resulting credit amount before the user confirms. | High | **Pass:** Displayed credit equals `points × live_rate` and matches the amount finally credited. **Fail:** Preview and credited amounts differ. | Users must see and approve an accurate rate; prevents disputes and builds trust. |
| **FR-004** | Functional | The system shall allow an Account Holder to redeem exchange credits for a digital gift card and apply anti-fraud voucher locking so the voucher cannot be reused. | High | **Pass:** Redeemed voucher status becomes `LOCKED`; a second redemption attempt is rejected. **Fail:** The same voucher is redeemed more than once. | Anti-fraud locking protects merchants and the platform's ledger integrity. |
| **FR-005** | Functional | The system shall let a Merchant Partner configure and update the dynamic exchange rate and validity window for their loyalty points. | Medium | **Pass:** An updated rate takes effect for all conversions initiated after the change and is logged with a timestamp. **Fail:** Conversions use a stale rate after an update is saved. | Merchants need control over their own point economics and promotions. |

---

## 2. Non-Functional Requirements

| Req ID | Type | Description | Priority | Acceptance Criteria (Pass / Fail) | Rationale |
|--------|------|-------------|----------|-----------------------------------|-----------|
| **NFR-001** | Non-Functional (Performance & Security) | Point conversion and gift-card redemption operations must process within 250 ms with zero ledger balance drift. | High | **Pass:** Benchmarking under simulated peak load confirms < 250 ms latency and reconciled ledger (drift = 0). **Fail:** Latency exceeds 250 ms or any ledger drift is detected. | Financial trust depends on fast, exact transactions even at peak. |
| **NFR-002** | Non-Functional (Security & Reliability) | All voucher codes and stored point balances shall be encrypted at rest and in transit, and every conversion/redemption shall be recorded in an immutable, tamper-evident audit log. | High | **Pass:** Data is AES-256 encrypted at rest, TLS 1.2+ in transit, and audit-log entries are append-only with a verifiable hash chain. **Fail:** Any value stored/transmitted in plaintext, or an audit entry can be altered without detection. | Protects against fraud, satisfies financial-compliance and dispute-resolution needs. |

---

## Legend
- **Priority:** High / Medium / Low
- **Type:** Functional / Non-Functional
- FR-001 and NFR-001 are the instructor-provided samples; FR-002…FR-005 and NFR-002 are authored for this scenario.
