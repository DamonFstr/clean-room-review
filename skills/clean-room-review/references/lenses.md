# Choosing lenses

A lens is a forcing function. It is not a topic. Each lens pushes an architect to optimise for one thing and to follow that choice where it leads, even when the result is uncomfortable. Four lenses that pull in different directions make the judge's comparison meaningful. Four similar lenses produce one design four times.

## A default set that works for most feature designs

| Lens | Push | Optimises for |
|---|---|---|
| **Record-keeping** | Model the domain as an append-only record of events or postings. State is derived, closed periods are immutable, and corrections are new entries. Borrow from accounting or event sourcing. | Audit, explainability, reproducing any past answer |
| **Generic engine** | Build one engine for every variant of the problem, now and later, with rules or configuration as versioned data that non-engineers can change. | Change over time, breadth, many variants |
| **Platform fit** | Build the smallest model that drops into the system as it is today, reusing existing tables, pipelines and patterns, with no new infrastructure. Name the point at which it would have to be replaced. | Delivery speed, operational simplicity, low risk |
| **Delegate** | Decide what the product should not compute at all. Check what vendors, partners or existing services actually offer, from their real documentation, then design the split and the integration contract. | Ownership, buy versus build, integration truth |

The delegate lens tends to surface facts that the others assume, such as "the partner has no API for this", and it often wins. Tell it to fetch the actual documentation and cite URLs, and to say so when it cannot verify something.

## Swapping lenses

Swap a lens out when it does not fit the problem. Alternatives that have pulled apart well:

- **Event-driven:** asynchronous, queue-based, with eventual consistency as a feature. Optimises for throughput and decoupling.
- **Read-model first:** design from the queries and screens back to storage. Optimises for UX and performance.
- **Strict consistency:** single writer, transactions everywhere, correctness over availability. Optimises for money and legal correctness.
- **Multi-tenant scale:** design for 100 times today's load and for noisy neighbours. Optimises for headroom.
- **Migration-first:** design the path from the current state as much as the end state. Optimises for safe rollout.

Choose lenses that disagree on at least two of these: where state lives, synchronous versus asynchronous, data versus code for rules, and build versus buy.

## In each architect's prompt

State the lens in two to four sentences, including what to borrow and what to optimise for, and name the other lenses. The architect agent already knows to commit to its lens and to work read-only outside its one output file.
