function showAppointmentMessage(message, isSuccess = false) {
  const el = document.getElementById("appointmentMessage");
  if (!el) return;

  el.textContent = message;
  el.className = isSuccess ? "form-message success" : "form-message error";
}

function clearAppointmentMessage() {
  const el = document.getElementById("appointmentMessage");
  if (!el) return;

  el.textContent = "";
  el.className = "form-message";
}

async function loadAppointments() {
  const result = await apiRequest("/appointments", "GET", null, true);
  const list = document.getElementById("appointmentsList");
  if (!list) return;

  list.innerHTML = "";

  if (!result.success || !Array.isArray(result.data) || result.data.length === 0) {
    list.innerHTML = `
      <div class="empty-state-card">
        <h3>Henüz aktif randevu yok</h3>
        <p>Yeni bir randevu oluşturduğunda burada görüntülenecek.</p>
      </div>
    `;
    return;
  }

  result.data.forEach((item) => {
    const card = document.createElement("div");
    card.className = "appointment-item-card";
    card.innerHTML = `
      <div class="appointment-item-top">
        <div>
          <h3>${item.hospital}</h3>
          <span class="appointment-status-badge">Aktif</span>
        </div>
      </div>

      <div class="appointment-item-grid">
        <p><strong>İl:</strong> ${item.city || "-"}</p>
        <p><strong>Bölüm:</strong> ${item.department}</p>
        <p><strong>Doktor:</strong> ${item.doctor}</p>
        <p><strong>Tarih:</strong> ${item.appointment_date}</p>
        <p><strong>Saat:</strong> ${item.appointment_time}</p>
      </div>

      <button class="appointment-cancel-btn" onclick="cancelAppointment('${item._id}')">
        Randevuyu İptal Et
      </button>
    `;
    list.appendChild(card);
  });
}

async function cancelAppointment(id) {
  const result = await apiRequest(`/appointments/${id}`, "DELETE", null, true);
  alert(result.message || "İşlem tamamlandı.");
  loadAppointments();
}

const appointmentForm = document.getElementById("appointmentForm");
if (appointmentForm) {
  appointmentForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    clearAppointmentMessage();

    const payload = {
      city: document.getElementById("city").value.trim(),
      hospital: document.getElementById("hospital").value.trim(),
      department: document.getElementById("department").value.trim(),
      doctor: document.getElementById("doctor").value.trim(),
      appointment_date: document.getElementById("appointment_date").value,
      appointment_time: document.getElementById("appointment_time").value
    };

    if (
      !payload.city ||
      !payload.hospital ||
      !payload.department ||
      !payload.doctor ||
      !payload.appointment_date ||
      !payload.appointment_time
    ) {
      showAppointmentMessage("Tüm randevu alanlarını doldurmanız gerekiyor.");
      return;
    }

    const result = await apiRequest("/appointments", "POST", payload, true);

    if (result.success) {
      showAppointmentMessage("Randevu başarıyla oluşturuldu.", true);
      appointmentForm.reset();
      loadAppointments();
    } else {
      showAppointmentMessage(result.message || "Randevu oluşturulamadı.");
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  loadAppointments();
});