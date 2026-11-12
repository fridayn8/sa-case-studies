# References

Books, frameworks and standards, grouped by the [engagement stage](engagement-playbook/README.md) in which
they help most. Each entry has the title, the author or organisation and one line on why it is useful.

> **Verification.** Every web address and title below was opened on **12 November 2026**. Pages
> can move or change; if a link breaks, search for the title. Books are cited by title, authors,
> publisher, year and ISBN-13, checked against Open Library metadata, because the publishers' own
> sites refuse automated access. Paid standards (ISO) link to the public catalogue page only.
> **Not included on purpose:** the Project Management Institute's PMBOK Guide, because its site could not
> be verified automatically; look it up yourself if you want a second view on estimation.

## Cross-stage frameworks and books

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [arc42 architecture documentation template](https://arc42.org/) | Gernot Starke and Peter Hruschka | A practical outline for architecture documents, from goals and constraints to risks and quality requirements |
| [The C4 model](https://c4model.com/) | Simon Brown | Four zoom levels (context, container, component, code) for diagrams that match the audience |
| [TOGAF Standard](https://www.opengroup.org/togaf) | The Open Group | The architecture development method (ADM) for larger organisations; read the phases as a checklist of what to consider |
| [Well-Architected Framework (AWS)](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) | Amazon Web Services | Six pillars (including security, reliability, cost) that work as design criteria even on premises |
| [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) | Microsoft | Similar pillars with design principles and trade-off guidance |
| [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) | Google Cloud | A third view of the same pillars; comparing the three shows what is universal |
| [Fundamentals of Software Architecture](https://openlibrary.org/isbn/9781492043454) | Mark Richards, Neal Ford; O'Reilly, 2020; ISBN 978-1-4920-4345-4 | Architecture characteristics, trade-off analysis and decision-making in plain language |
| [The Software Architect Elevator](https://openlibrary.org/isbn/9781492077541) | Gregor Hohpe; O'Reilly, 2020; ISBN 978-1-4920-7754-1 | How an architect communicates between the boardroom and the engine room; useful from stage 0 to stage 9 |
| [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) (free online) | Google; edited by Betsy Beyer and others, O'Reilly, 2016 | Operations, monitoring, incident response and launches written by practitioners |

## Stage 0: Pitch and first contact

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [NIST Cybersecurity Framework 2.0: Small Business Quick-Start Guide](https://www.nist.gov/publications/nist-cybersecurity-framework-20-small-business-quick-start-guide) | NIST | A short, plain-language frame for a first security conversation with a small client |
| [10 Steps to Cyber Security](https://www.ncsc.gov.uk/collection/10-steps) | UK National Cyber Security Centre | A readable list of what a company should already be doing; useful for "what happens if we do nothing" |
| [#StopRansomware](https://www.cisa.gov/stopransomware) | CISA (US) | Guides and facts on ransomware to ground the cost-of-doing-nothing argument in evidence |
| [The Software Architect Elevator](https://openlibrary.org/isbn/9781492077541) | Gregor Hohpe | Talking to the sponsor in the sponsor's language |

## Stage 1: Discovery

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [BABOK Guide](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/) | International Institute of Business Analysis | The standard reference for elicitation: interviews, workshops, observation, document analysis |
| [arc42: introduction and goals, constraints, context and scope](https://arc42.org/) | Starke, Hruschka | Where to write stakeholders, constraints and the system boundary |
| [C4 model: system context diagram](https://c4model.com/) | Simon Brown | Drawing the as-is and to-be context so that the client can confirm it |

## Stage 2: Requirements

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [What is MoSCoW Prioritization?](https://www.agilebusiness.org/resource/what-is-moscow-prioritization/) | Agile Business Consortium | The definition of Must, Should, Could and Won't from the people who maintain the method |
| [SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | NIST | Business impact analysis, recovery objectives and testing of recovery plans |
| [ISO 22301:2019 Business continuity management systems](https://www.iso.org/standard/75106.html) | ISO | The standard behind recovery time and recovery point objectives (catalogue page; the text is paid) |
| [Fundamentals of Software Architecture](https://openlibrary.org/isbn/9781492043454) | Richards, Ford | Architecture characteristics: how to turn "fast" and "reliable" into measurable requirements |

## Stage 3: Options and decisions

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [Markdown Architectural Decision Records (MADR)](https://adr.github.io/madr/) | ADR GitHub organisation | The template used by the ADRs in this repository |
| [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Michael Nygard | The short essay that started the ADR practice |
| [AWS](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), [Azure](https://learn.microsoft.com/en-us/azure/well-architected/) and [Google Cloud](https://docs.cloud.google.com/architecture/framework) Well-Architected Frameworks | The three providers | Pillars to turn into decision criteria; weights are yours |
| [Fundamentals of Software Architecture](https://openlibrary.org/isbn/9781492043454) | Richards, Ford | Trade-off analysis: "everything in architecture is a trade-off" in practice |

## Stage 4: Design

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [The C4 model](https://c4model.com/) | Simon Brown | The diagram set used in [Case 01](case-01-example-corp/03-design/diagrams/c4-context.md) |
| [arc42](https://arc42.org/) | Starke, Hruschka | A document structure for the HLD: building blocks, runtime view, deployment, risks |
| [Threat Modeling](https://community.owasp.org/Threat_Modeling) | OWASP | An overview of threat-modelling methods, including STRIDE |
| [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | OWASP Cheat Sheet Series | A concise procedure: scope, decompose, identify threats, mitigate, validate |
| [Cybersecurity Framework](https://www.nist.gov/cyberframework) | NIST | Version 2.0 organises security outcomes (govern, identify, protect, detect, respond, recover) |
| [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | ISO/IEC | The information security management standard that many insurers and clients refer to (catalogue page) |
| [TOGAF Standard](https://www.opengroup.org/togaf) | The Open Group | Architecture views and governance for larger programmes |

## Stage 5: Proposal and commercial

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [Software Estimation: Demystifying the Black Art](https://openlibrary.org/isbn/9780735605350) | Steve McConnell; Microsoft Press, 2006; ISBN 978-0-7356-0535-0 | Estimation ranges, uncertainty and how to present estimates honestly |
| [TOGAF Standard](https://www.opengroup.org/togaf) | The Open Group | Architecture contracts and governance between architects and implementers |
| [The Software Architect Elevator](https://openlibrary.org/isbn/9781492077541) | Gregor Hohpe | Writing for decision makers: clear options, clear consequences |

## Stage 6: Build oversight

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [ITIL](https://www.itil.com/) and [ITIL certifications](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1) | PeopleCert | The service management framework behind change enablement and change types |
| [Accelerate: The Science of Lean Software and DevOps](https://openlibrary.org/isbn/9781942788331) | Nicole Forsgren, Jez Humble, Gene Kim; IT Revolution Press, 2018; ISBN 978-1-942788-33-1 | Evidence on which delivery practices correlate with stable, fast change |
| [DORA](https://dora.dev/) | DORA research programme | Delivery metrics (lead time, change failure rate, time to restore) that make build progress measurable |
| [TOGAF Standard](https://www.opengroup.org/togaf) | The Open Group | The implementation governance phase: how an architect checks a build against its design |

## Stage 7: Test and go-live

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [Deployment Strategies for Product Launches](https://sre.google/sre-book/reliable-product-launches/) | Google SRE book | Launch checklists, staged rollouts and rollback, written from real incidents |
| [SP 800-34 Rev. 1: Contingency Planning Guide](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | NIST | How to test a recovery plan and what the test should prove |
| [ISO 22301:2019](https://www.iso.org/standard/75106.html) | ISO | Exercising and testing continuity arrangements (catalogue page) |
| [DORA](https://dora.dev/) | DORA research programme | Change failure rate and time to restore as measures of go-live quality |

## Stage 8: Handover and operate

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) | Google | Monitoring, on-call, incident response and the reasoning behind runbooks and alerts that matter |
| [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/) | Google | Practical exercises and examples for operating services |
| [ITIL](https://www.itil.com/) | PeopleCert | Service desk, incident, problem and change practices behind a support model |

## Stage 9: Review

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/) | Google SRE book | How to run blameless reviews that lead to real changes |
| [Accelerate](https://openlibrary.org/isbn/9781942788331) and [DORA](https://dora.dev/) | Forsgren, Humble, Kim; DORA | Measures to compare "before" and "after" objectively |
| [Fundamentals of Software Architecture](https://openlibrary.org/isbn/9781492043454) | Richards, Ford | Revisiting decisions and technical debt with architecture fitness in mind |

## Estimation and planning

| Title | Author / organisation | Why it is useful |
|-------|-----------------------|------------------|
| [Software Estimation: Demystifying the Black Art](https://openlibrary.org/isbn/9780735605350) | Steve McConnell | The best single reference on ranges, calibration with your own history and communicating uncertainty |
| [DORA](https://dora.dev/) | DORA research programme | Measuring actual delivery time to improve future estimates |
| [Timeline, effort and estimation](engagement-playbook/timeline-and-effort.md) | This repository | The method, scale factors and worked example used in the playbook |
