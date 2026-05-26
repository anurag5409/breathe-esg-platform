import { useEffect, useState } from "react";
import axios from "axios";

const API_URL =
  "https://breathe-esg-platform-production.up.railway.app";

function App() {
  const [records, setRecords] = useState([]);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(
        `${API_URL}/api/reviews/`
      );

      setRecords(response.data);
    } catch (error) {
      console.error("Fetch error:", error);
    }
  };

  useEffect(() => {
    fetchRecords();
  }, []);

  const approveRecord = async (id) => {
    try {
      await axios.post(
        `${API_URL}/api/approve/${id}/`
      );

      fetchRecords();

    } catch (error) {
      console.error("Approval failed:", error);
    }
  };

  const totalRecords = records.length;

  const approvedRecords = records.filter(
    (r) => r.status === "approved"
  ).length;

  const suspiciousRecords = records.filter(
    (r) => r.suspicious
  ).length;

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f4f7fb",
        fontFamily: "Arial, sans-serif",
        paddingBottom: "40px"
      }}
    >
      <div
        style={{
          background: "#0f172a",
          color: "white",
          padding: "30px 50px",
          boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
        }}
      >
        <h1
          style={{
            margin: 0,
            fontSize: "42px"
          }}
        >
          Breathe ESG Platform
        </h1>

        <p
          style={{
            marginTop: "10px",
            color: "#cbd5e1"
          }}
        >
          Emissions ingestion and analyst review workflow
        </p>
      </div>

      <div
        style={{
          display: "flex",
          gap: "20px",
          padding: "30px 50px",
          flexWrap: "wrap"
        }}
      >
        <div style={cardStyle}>
          <h3>Total Records</h3>

          <p style={numberStyle}>
            {totalRecords}
          </p>
        </div>

        <div style={cardStyle}>
          <h3>Approved</h3>

          <p
            style={{
              ...numberStyle,
              color: "green"
            }}
          >
            {approvedRecords}
          </p>
        </div>

        <div style={cardStyle}>
          <h3>Suspicious Records</h3>

          <p
            style={{
              ...numberStyle,
              color: "red"
            }}
          >
            {suspiciousRecords}
          </p>
        </div>
      </div>

      <div
        style={{
          background: "white",
          margin: "0 50px",
          borderRadius: "12px",
          padding: "25px",
          boxShadow: "0 2px 10px rgba(0,0,0,0.08)"
        }}
      >
        <h2 style={{ marginBottom: "10px" }}>
          Analyst Review Queue
        </h2>

        <p
          style={{
            color: "#666",
            marginBottom: "25px"
          }}
        >
          Review imported ESG activity records
        </p>

        <table
          style={{
            width: "100%",
            borderCollapse: "collapse"
          }}
        >
          <thead>
            <tr
              style={{
                background: "#f1f5f9"
              }}
            >
              <th style={thStyle}>Category</th>
              <th style={thStyle}>Value</th>
              <th style={thStyle}>Unit</th>
              <th style={thStyle}>Scope</th>
              <th style={thStyle}>Status</th>
              <th style={thStyle}>Risk</th>
              <th style={thStyle}>Action</th>
            </tr>
          </thead>

          <tbody>
            {records.map((record) => (
              <tr
                key={record.id}
                style={{
                  borderBottom: "1px solid #e2e8f0"
                }}
              >
                <td style={tdStyle}>
                  {record.category}
                </td>

                <td style={tdStyle}>
                  {record.activity_value}
                </td>

                <td style={tdStyle}>
                  {record.activity_unit}
                </td>

                <td style={tdStyle}>
                  {record.scope}
                </td>

                <td style={tdStyle}>
                  <span
                    style={{
                      padding: "6px 12px",
                      borderRadius: "20px",
                      background:
                        record.status === "approved"
                          ? "#dcfce7"
                          : "#fef3c7",
                      color:
                        record.status === "approved"
                          ? "green"
                          : "#92400e",
                      fontWeight: "bold",
                      fontSize: "14px"
                    }}
                  >
                    {record.status}
                  </span>
                </td>

                <td style={tdStyle}>
                  {record.suspicious ? (
                    <span
                      style={{
                        color: "red",
                        fontWeight: "bold"
                      }}
                    >
                      ⚠ Needs Review
                    </span>
                  ) : (
                    <span
                      style={{
                        color: "green"
                      }}
                    >
                      Normal
                    </span>
                  )}
                </td>

                <td style={tdStyle}>
                  {record.status !== "approved" ? (
                    <button
                      onClick={() =>
                        approveRecord(record.id)
                      }
                      style={{
                        background: "#2563eb",
                        color: "white",
                        border: "none",
                        padding: "10px 16px",
                        borderRadius: "8px",
                        cursor: "pointer",
                        fontWeight: "bold"
                      }}
                    >
                      Approve
                    </button>
                  ) : (
                    <span
                      style={{
                        color: "green",
                        fontWeight: "bold"
                      }}
                    >
                      Approved
                    </span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

const cardStyle = {
  background: "white",
  padding: "25px",
  borderRadius: "12px",
  minWidth: "220px",
  boxShadow: "0 2px 10px rgba(0,0,0,0.08)"
};

const numberStyle = {
  fontSize: "42px",
  fontWeight: "bold",
  marginTop: "10px"
};

const thStyle = {
  padding: "15px",
  textAlign: "left"
};

const tdStyle = {
  padding: "15px"
};

export default App;