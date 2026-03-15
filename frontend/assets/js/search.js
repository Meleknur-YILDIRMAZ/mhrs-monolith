async function runSearch() {
  const query = document.getElementById("searchInput").value.trim();
  const container = document.getElementById("searchResults");
  if (!container) return;

  container.innerHTML = "";

  if (!query) {
    container.innerHTML = `
      <div class="empty-state-card">
        <h3>Arama metni gir</h3>
        <p>Devam etmek için hastane, bölüm, doktor veya şehir yaz.</p>
      </div>
    `;
    return;
  }

  const result = await apiRequest(`/search?q=${encodeURIComponent(query)}`, "GET", null, false);

  if (!result.success || !Array.isArray(result.data) || result.data.length === 0) {
    container.innerHTML = `
      <div class="empty-state-card">
        <h3>Sonuç bulunamadı</h3>
        <p>Farklı bir anahtar kelime ile tekrar deneyebilirsin.</p>
      </div>
    `;
    return;
  }

  result.data.forEach((item) => {
    const card = document.createElement("div");
    card.className = "search-result-card";
    card.innerHTML = `
      <div class="search-result-top">
        <h3>${item.hospital || "-"}</h3>
        <span class="search-result-badge">${item.city || "Şehir"}</span>
      </div>

      <div class="search-result-grid">
        <p><strong>İl:</strong> ${item.city || "-"}</p>
        <p><strong>Bölüm:</strong> ${item.department || "-"}</p>
        <p><strong>Doktor:</strong> ${item.doctor || "-"}</p>
      </div>
    `;
    container.appendChild(card);
  });
}

const searchBtn = document.getElementById("searchBtn");
if (searchBtn) {
  searchBtn.addEventListener("click", runSearch);
}

const searchInput = document.getElementById("searchInput");
if (searchInput) {
  searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      runSearch();
    }
  });
}