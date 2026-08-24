# UML Use-Case Diagram

**Problem Statement #34 — Digital Gift Card & Loyalty Point Exchange**
**SRN:** PES1UG24CS221

The diagram models all actors, the primary use cases, and includes **two «include»**
relationships and **one «extend»** relationship (as required).

- PlantUML source: [diagrams/use_case_diagram.puml](diagrams/use_case_diagram.puml)
  (render at [plantuml.com](https://www.plantuml.com/plantuml/uml/), draw.io, or Lucidchart, then export to PDF)
- A GitHub-renderable Mermaid approximation is shown below.

---

## Mermaid rendering (view on GitHub)

```mermaid
flowchart LR
    AH([Account Holder])
    MP([Merchant Partner])
    FS([Fraud / Voucher-Locking Service])
    PG([Payment / Settlement Gateway])

    subgraph System["Digital Gift Card & Loyalty Point Exchange"]
        UC1(("UC-01<br/>Link & Aggregate<br/>Loyalty Accounts"))
        UC2(("UC-02<br/>Convert Points<br/>to Credits"))
        UC3(("UC-03<br/>Redeem<br/>Gift Card"))
        UC4(("UC-04<br/>Validate & Lock<br/>Voucher"))
        UC5(("UC-05<br/>Configure<br/>Exchange Rate"))
        UC6(("UC-06<br/>Authenticate<br/>User"))
        UCX(("Apply<br/>Promotional Bonus"))
    end

    AH --- UC1
    AH --- UC2
    AH --- UC3
    MP --- UC5
    FS --- UC4
    UC3 --- PG

    UC2 -. "«include»" .-> UC4
    UC3 -. "«include»" .-> UC4
    UC2 -. "«include»" .-> UC6
    UC3 -. "«include»" .-> UC6
    UCX -. "«extend»" .-> UC3
```

**Legend**
- Rounded pills on the outside = **actors**.
- Ovals inside the boundary = **use cases**.
- Dotted arrows labelled «include» / «extend» = **stereotyped dependencies**.
- «include»: UC-02 and UC-03 always call UC-04 (Validate & Lock Voucher) and UC-06 (Authenticate).
- «extend»: *Apply Promotional Bonus* optionally extends UC-03 when a promotion is active.
