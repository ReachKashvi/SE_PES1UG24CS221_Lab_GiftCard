# Software Requirements Specification (SRS) — Requirements Table

**Problem Statement #34 — Digital Gift Card & Loyalty Point Exchange**
**SRN:** PES1UG24CS221

This single file contains **both** the Functional Requirements (FR-001 → FR-005)
and the Non-Functional Requirements (NFR-001, NFR-002), each with a measurable
acceptance criterion and a rationale, formatted as an SRS table.

**System story (grounding):** Account Holder links loyalty accounts → points are
validated → points are converted into **universal exchange credits** → user redeems
credits for a digital gift card → the voucher is validated/locked to prevent reuse.

---

## 1. Functional Requirements

| Req ID | Type | Description ("The system shall…") | Priority | Acceptance Criteria (Pass / Fail) | Rationale |
|--------|------|-----------------------------------|----------|-----------------------------------|-----------|
| **FR-001** | Functional | The system shall validate merchant loyalty points, convert them into universal exchange credits, and generate single-use digital voucher codes. | High | **Pass:** Valid points are accepted and converted using the applicable exchange rate, and a unique voucher code is generated when redemption is completed. **Fail:** Expired/invalid points or a duplicate voucher is accepted. | Core functionality of the platform. |
| **FR-002** | Functional | The system shall allow an Account Holder to link multiple brand loyalty accounts and view their aggregated point balances. | High | **Pass:** Linked loyalty accounts and their valid point balances are displayed in the wallet. **Fail:** A linked account is missing or its points are double-counted. | Enables aggregation of fragmented loyalty points. |
| **FR-003** | Functional | The system shall calculate universal exchange credits using the applicable dynamic exchange rate and display the resulting credit amount before conversion. | High | **Pass:** Displayed credits equal the selected points multiplied by the applicable exchange rate. **Fail:** The displayed and credited amounts differ. | Ensures transparent and accurate conversion. |
| **FR-004** | Functional | The system shall allow an Account Holder to redeem universal exchange credits for an available digital gift card and prevent reuse of the generated voucher. | High | **Pass:** Required credits are deducted and the voucher is locked after successful redemption. **Fail:** Redemption succeeds with insufficient credits or a previously used voucher. | Provides the main redemption functionality and prevents fraud. |
| **FR-005** | Functional | The system shall allow a Merchant Partner to configure and update the dynamic exchange rate for its loyalty points. | Medium | **Pass:** New conversions use the updated rate after it is saved. **Fail:** A conversion uses a previous rate after the update. | Supports the dynamic-rate requirement in the problem statement. |

---

## 2. Non-Functional Requirements

| Req ID | Type | Description | Priority | Acceptance Criteria (Pass / Fail) | Rationale |
|--------|------|-------------|----------|-----------------------------------|-----------|
| **NFR-001** | Non-Functional (Performance & Security) | The system shall process point conversion and gift-card redemption operations within 250 ms with zero ledger balance drift. | High | **Pass:** Testing confirms ≤ 250 ms processing time and zero ledger balance drift under simulated peak load. **Fail:** Processing exceeds 250 ms or ledger drift occurs. | Directly satisfies the provided performance and financial-integrity requirement. |
| **NFR-002** | Non-Functional (Security) | The system shall ensure that generated voucher codes are unique and cannot be successfully redeemed more than once. | High | **Pass:** A used voucher is rejected on every subsequent redemption attempt. **Fail:** A voucher can be redeemed more than once or duplicate active codes are generated. | Protects against voucher fraud. |

---

## Legend
- **Priority:** High / Medium / Low
- **Type:** Functional / Non-Functional
- FR-001 and NFR-001 are the instructor-provided samples; FR-002…FR-005 and NFR-002 are authored for this scenario.
