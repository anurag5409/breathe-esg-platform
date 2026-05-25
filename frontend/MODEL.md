# MODEL

## Core Entities

---

## Tenant

Represents an enterprise customer onboarded onto the ESG platform.

Supports:
- logical isolation
- multi-tenant architecture
- enterprise segmentation

---

## DataSource

Tracks uploaded source files and ingestion metadata.

Supports:
- SAP uploads
- utility uploads
- travel uploads

Tracks:
- source type
- uploaded user
- original filename
- upload timestamp

---

## EmissionRecord

Represents normalized ESG activity data.

Tracks:
- category
- activity value
- units
- normalized values
- suspicious flags
- review status
- scope classification

Supports:
- Scope 1
- Scope 2
- Scope 3

---

## AuditLog

Maintains audit trail for analyst actions.

Tracks:
- approval actions
- timestamps
- users
- notes

Supports auditability and workflow traceability.

---

# Multi-Tenancy

Every record belongs to a Tenant.

This ensures:
- customer isolation
- scalable onboarding
- enterprise separation

---

# Auditability

All analyst approvals generate audit logs.

This preserves:
- workflow history
- approval lineage
- review accountability

---

# Source-of-Truth Tracking

Every emission record references the original uploaded DataSource.

This allows:
- ingestion traceability
- debugging
- operational auditing

---

# Normalization Strategy

Prototype normalizes uploaded operational data into simplified kgCO2e-compatible values.

Production implementations would include:
- regional emission factors 
- dynamic conversions
- factor libraries
- time-based calculations