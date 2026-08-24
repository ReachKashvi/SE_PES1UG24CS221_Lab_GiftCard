# UML Use-Case Diagram

**Problem Statement #34 — Digital Gift Card & Loyalty Point Exchange**
**SRN:** PES1UG24CS221

The diagram models the three actors, eight use cases, and includes **two «include»**
relationships and **one «extend»** relationship (as required).

- PlantUML source (source of truth): [diagrams/usecase_diagram.puml](diagrams/usecase_diagram.puml)
- draw.io source: [diagrams/usecase_diagram.drawio](diagrams/usecase_diagram.drawio)
  (open at [app.diagrams.net](https://app.diagrams.net), then `File → Export as → PDF`)
- A GitHub-renderable Mermaid approximation is shown below.

---

## Actors
- **Account Holder** — links loyalty accounts, converts points, redeems gift cards, views history.
- **Merchant Partner** — configures the dynamic exchange rate; validates loyalty points.
- **Loyalty Program System** — external system that provides/validates loyalty-point balances.

## Relationships
- **«include»**: UC-02 *Convert Points to Exchange Credits* → UC-07 *Validate Loyalty Points* (points must be validated before conversion).
- **«include»**: UC-03 *Redeem Digital Gift Card* → UC-04 *Validate & Lock Voucher* (every redemption locks a single-use voucher).
- **«extend»**: UC-08 *Flag Suspicious Redemption* → UC-03 *Redeem Digital Gift Card* (only abnormal redemptions trigger fraud handling).

---

## Mermaid rendering (view on GitHub)

```mermaid
flowchart LR
    AH([Account Holder])
    MP([Merchant Partner])
    LPS([Loyalty Program System])

    subgraph System["Digital Gift Card & Loyalty Point Exchange"]
        UC1(("UC-01<br/>Link & Aggregate<br/>Loyalty Accounts"))
        UC2(("UC-02<br/>Convert Points to<br/>Exchange Credits"))
        UC3(("UC-03<br/>Redeem Digital<br/>Gift Card"))
        UC4(("UC-04<br/>Validate & Lock<br/>Voucher"))
        UC5(("UC-05<br/>Configure Dynamic<br/>Exchange Rate"))
        UC6(("UC-06<br/>View Transaction<br/>History"))
        UC7(("UC-07<br/>Validate Loyalty<br/>Points"))
        UC8(("UC-08<br/>Flag Suspicious<br/>Redemption"))
    end

    AH --- UC1
    AH --- UC2
    AH --- UC3
    AH --- UC6
    MP --- UC5
    MP --- UC7
    LPS --- UC1
    LPS --- UC7

    UC2 -. "«include»" .-> UC7
    UC3 -. "«include»" .-> UC4
    UC8 -. "«extend»" .-> UC3
```

**Legend**
- Rounded pills outside the boundary = **actors**.
- Ovals inside the boundary = **use cases**.
- Dotted arrows labelled «include» / «extend» = **stereotyped dependencies**.
