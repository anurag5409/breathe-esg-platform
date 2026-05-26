# Breathe ESG Platform

A full-stack ESG data ingestion and analyst review workflow platform built using Django REST Framework and React.

---

## Live Demo

Frontend:
https://vercel.com/anurag-singh-s-projects3/breathe-esg-platform

Backend:
https://breathe-esg-platform-production.up.railway.app/api/reviews/

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Approved Records

![Approved](screenshots/approved-records.png)

### Backend API

![API](screenshots/backend-api.png)

---

## Features

- SAP CSV ingestion
- Utility data ingestion
- Corporate travel ingestion
- Scope 1/2/3 support
- Suspicious activity detection
- Analyst approval workflow
- Audit logging
- Multi-tenant architecture
- REST APIs
- React dashboard
- Railway deployment
- Vercel deployment 

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

# Breathe ESG Platform

A prototype ESG ingestion and analyst review platform built using Django REST Framework and React.

---

# Features

- SAP-style CSV ingestion
- Utility electricity ingestion
- Corporate travel ingestion
- Multi-tenant architecture
- Suspicious activity detection
- Analyst review workflow
- Approval system
- Audit logging
- Scope 1, Scope 2, Scope 3 handling
- REST APIs
- React dashboard

---

# Tech Stack

## Backend
- Django
- Django REST Framework
- SQLite
- Pandas

## Frontend
- React
- Axios
- Vite

---

# Workflow

Data Sources → Ingestion → Normalization → Review Queue → Approval → Audit Trail

---

# Supported Data Sources

## 1. SAP Procurement Uploads
Handles:
- fuel procurement
- material procurement
- operational activity exports

---

## 2. Utility Electricity Uploads
Handles:
- meter-based electricity consumption
- kWh normalization

---

## 3. Corporate Travel Uploads
Handles:
- flights
- taxi travel
- hotel travel records

---

# Core Capabilities

## Normalization
Uploaded records are normalized into simplified kgCO2e-compatible values.

## Suspicious Detection
Large operational values are automatically flagged for analyst review.

## Analyst Workflow
Imported records remain pending until approved by analysts.

## Audit Trail
All approvals create audit log entries.

## Multi-Tenancy
Records are linked to tenants for enterprise isolation.

---

# Local Setup

## Backend

```bash
cd backend
venv\Scripts\activate
python manage.py runserver
```

---

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

# API Endpoints

## SAP Upload
POST `/api/upload/sap/`

## Utility Upload
POST `/api/upload/utility/`

## Travel Upload
POST `/api/upload/travel/`

## Review Queue
GET `/api/reviews/`

## Approve Record
POST `/api/approve/<id>/`

---

# Sample Files

- sap_sample.csv
- utility_sample.csv
- travel_sample.csv

---

# Future Improvements

- OCR-based utility bill ingestion
- Real SAP integrations
- Async ingestion pipelines
- Role-based access control
- Dynamic emission factor libraries
- Production authentication
- Cloud storage integration