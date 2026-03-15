function saveToken(token) {
  localStorage.setItem("token", token);
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}

function showMessage(elementId, message, isSuccess = false) {
  const el = document.getElementById(elementId);
  if (!el) return;

  el.textContent = message;
  el.className = isSuccess ? "form-message success" : "form-message error";
}

function clearMessage(elementId) {
  const el = document.getElementById(elementId);
  if (!el) return;

  el.textContent = "";
  el.className = "form-message";
}

function onlyLetters(value) {
  return /^[A-Za-zÇçĞğİıÖöŞşÜü\s]+$/.test(value);
}

function onlyNumbers(value) {
  return /^\d+$/.test(value);
}

function sanitizeNumericInput(inputElement, maxLength = null) {
  if (!inputElement) return;

  inputElement.addEventListener("input", () => {
    let cleaned = inputElement.value.replace(/\D/g, "");
    if (maxLength) {
      cleaned = cleaned.slice(0, maxLength);
    }
    inputElement.value = cleaned;
  });
}

const logoutBtn = document.getElementById("logoutBtn");
if (logoutBtn) {
  logoutBtn.addEventListener("click", logout);
}

/* REGISTER VALIDATIONS */
const tcInput = document.getElementById("tc_no");
const phoneInput = document.getElementById("phone");
sanitizeNumericInput(tcInput, 11);
sanitizeNumericInput(phoneInput, 11);

/* LOGIN */
const loginForm = document.getElementById("loginForm");
if (loginForm) {
  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    clearMessage("loginMessage");

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!email || !password) {
      showMessage("loginMessage", "E-posta ve şifre zorunludur.");
      return;
    }

    const result = await apiRequest("/auth/login", "POST", { email, password });

    if (result.success) {
      saveToken(result.data.token);
      showMessage("loginMessage", "Giriş başarılı. Yönlendiriliyorsunuz...", true);
      setTimeout(() => {
        window.location.href = "dashboard.html";
      }, 700);
    } else {
      showMessage("loginMessage", result.message || "Giriş başarısız.");
    }
  });
}

/* REGISTER */
const registerForm = document.getElementById("registerForm");
if (registerForm) {
  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    clearMessage("registerMessage");

    const first_name = document.getElementById("first_name").value.trim();
    const last_name = document.getElementById("last_name").value.trim();
    const tc_no = document.getElementById("tc_no").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!first_name || !last_name || !tc_no || !phone || !email || !password) {
      showMessage("registerMessage", "Tüm alanları doldurmanız gerekiyor.");
      return;
    }

    if (!onlyLetters(first_name)) {
      showMessage("registerMessage", "Ad alanında sayı veya özel karakter olamaz.");
      return;
    }

    if (!onlyLetters(last_name)) {
      showMessage("registerMessage", "Soyad alanında sayı veya özel karakter olamaz.");
      return;
    }

    if (!onlyNumbers(tc_no)) {
      showMessage("registerMessage", "T.C. Kimlik No sadece rakamlardan oluşmalıdır.");
      return;
    }

    if (tc_no.length !== 11) {
      showMessage("registerMessage", "T.C. Kimlik No 11 haneli olmalıdır.");
      return;
    }

    if (!onlyNumbers(phone)) {
      showMessage("registerMessage", "Telefon numarası sadece rakamlardan oluşmalıdır.");
      return;
    }

    if (phone.length !== 11) {
      showMessage("registerMessage", "Telefon numarası 11 haneli olmalıdır.");
      return;
    }

    if (password.length < 6) {
      showMessage("registerMessage", "Şifre en az 6 karakter olmalıdır.");
      return;
    }

    const payload = {
      first_name,
      last_name,
      tc_no,
      phone,
      email,
      password
    };

    const result = await apiRequest("/auth/register", "POST", payload);

    if (result.success) {
      showMessage("registerMessage", "Kayıt başarılı. Giriş sayfasına yönlendiriliyorsunuz...", true);
      registerForm.reset();

      setTimeout(() => {
        window.location.href = "login.html";
      }, 1000);
    } else {
      showMessage("registerMessage", result.message || "Kayıt başarısız.");
    }
  });
}