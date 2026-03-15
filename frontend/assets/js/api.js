const API_BASE = "http://localhost:5000/api";

async function apiRequest(endpoint, method = "GET", body = null, auth = false) {
  const headers = {
    "Content-Type": "application/json"
  };

  if (auth) {
    const token = localStorage.getItem("token");
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
  }

  const options = {
    method,
    headers
  };

  if (body) {
    options.body = JSON.stringify(body);
  }

  try {
    const response = await fetch(`${API_BASE}${endpoint}`, options);
    const data = await response.json();
    return data;
  } catch (error) {
    return {
      success: false,
      message: "Backend'e bağlanılamadı. Flask sunucusunun çalıştığını kontrol et."
    };
  }
}