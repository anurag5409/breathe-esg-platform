# SOURCES

## SAP Research

Researched:
- SAP procurement exports
- flat-file operational exports
- ingestion workflows

Observed:
- inconsistent units
- irregular formatting
- operational complexity

Prototype simplified handling into structured CSV ingestion.

---

## Utility Data Research

Researched:
- electricity billing exports
- meter-level utility reporting

Observed:
- utilities vary significantly in format
- billing periods often differ
- meter tracking is essential

Prototype simplified ingestion into monthly kWh records.

---

## Corporate Travel Research

Researched:
- Concur exports
- Navan workflows
- travel activity categorization

Observed:
- flights, hotels, and taxis require different factor handling
- airport/location mapping is complex

Prototype simplified ingestion into categorized travel records.

---

## ESG Workflow Research

Researched:
- ESG governance workflows
- analyst review practices
- auditability requirements

Observed:
- operational data often requires manual validation
- suspicious activity review is important
- audit history is critical for compliance

---

## Production Risks

Real implementations would require:
- authentication systems
- scalable async ingestion
- retries
- schema evolution handling
- secure storage
- dynamic factor management