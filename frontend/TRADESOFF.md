# TRADEOFFS

## 1. No Real SAP Integration

Real SAP integrations require enterprise infrastructure, credentials, middleware, and significant implementation effort.

CSV ingestion was prioritized to demonstrate ingestion architecture realistically within assignment constraints.

---

## 2. No OCR Pipeline

Utility PDF OCR was intentionally excluded.

OCR introduces:
- extraction inaccuracies
- preprocessing complexity
- document formatting variance

CSV uploads better demonstrated normalization and workflow logic.

---

## 3. No Async Processing

Uploads are processed synchronously in the prototype.

Production systems would likely use:
- Celery
- queues
- background workers

Synchronous handling simplified debugging and infrastructure setup.

---

## 4. Simplified Emission Factors

Prototype uses simplified normalization multipliers.

Production systems would require:
- verified factor libraries
- regional mappings
- methodology versioning

---

## 5. Minimal Authentication

Prototype focuses on workflow demonstration rather than enterprise authentication systems.

Production deployments would include:
- RBAC
- SSO
- audit permissions
- tenant-level security