# DECISIONS

## SAP Handling

CSV ingestion was selected because SAP flat-file exports are operationally common and easier to validate during onboarding workflows.

Prototype intentionally avoided:
- IDoc parsing
- OData integrations
- BAPI authentication

---

## Utility Data Handling

Utility ingestion uses CSV uploads because facilities teams frequently export electricity data manually from portals.

Prototype assumptions:
- monthly billing periods
- meter-level aggregation
- structured kWh data

Ignored:
- PDF OCR extraction
- tariff modeling
- timezone handling

---

## Corporate Travel Handling

Travel ingestion was modeled after Concur/Navan-style export workflows.

Prototype assumptions:
- categorized transport modes
- structured distance fields
- known routes

Ignored:
- live API integrations
- geospatial calculations
- hotel emission factor complexity

---

## Review Workflow

All imported records require analyst approval before finalization.

This reflects real ESG governance workflows where operational data must be validated before reporting.

---

## Suspicious Detection

High operational values are flagged automatically for analyst review.

This demonstrates anomaly detection during ingestion.

---

## Technology Stack

Django REST Framework was selected for rapid API development.

React was selected for:
- fast UI iteration
- API integration simplicity
- dashboard flexibility