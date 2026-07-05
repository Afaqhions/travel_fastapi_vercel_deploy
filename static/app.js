const API = "/api/destinations";

const form = document.getElementById("destination-form");
const formTitle = document.getElementById("form-title");
const editId = document.getElementById("edit-id");
const cityInput = document.getElementById("city");
const countryInput = document.getElementById("country");
const descInput = document.getElementById("description");
const submitBtn = document.getElementById("submit-btn");
const cancelBtn = document.getElementById("cancel-btn");
const listEl = document.getElementById("destination-list");
const loadingEl = document.getElementById("loading");

async function fetchAll() {
  const res = await fetch(API);
  return res.json();
}

async function create(data) {
  const res = await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

async function update(id, data) {
  const res = await fetch(`${API}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

async function remove(id) {
  await fetch(`${API}/${id}`, { method: "DELETE" });
}

function renderCard(dest) {
  const card = document.createElement("div");
  card.className = "destination-card";
  card.innerHTML = `
    <div class="destination-info">
      <h3>${escapeHtml(dest.city)}</h3>
      <div class="country">${escapeHtml(dest.country)}</div>
      <div class="description">${escapeHtml(dest.description || "No description")}</div>
    </div>
    <div class="destination-actions">
      <button class="btn-edit" data-id="${dest.id}">Edit</button>
      <button class="btn-delete" data-id="${dest.id}">Delete</button>
    </div>
  `;
  card.querySelector(".btn-edit").addEventListener("click", () => populateForm(dest));
  card.querySelector(".btn-delete").addEventListener("click", async () => {
    await remove(dest.id);
    renderList();
  });
  return card;
}

async function renderList() {
  loadingEl.style.display = "block";
  listEl.innerHTML = "";
  const destinations = await fetchAll();
  loadingEl.style.display = "none";

  if (destinations.length === 0) {
    listEl.innerHTML = '<div class="empty-state">No destinations yet. Add one above!</div>';
    return;
  }

  destinations.forEach((d) => listEl.appendChild(renderCard(d)));
}

function populateForm(dest) {
  formTitle.textContent = "Edit Destination";
  editId.value = dest.id;
  cityInput.value = dest.city;
  countryInput.value = dest.country;
  descInput.value = dest.description || "";
  submitBtn.textContent = "Update";
  cancelBtn.style.display = "inline-block";
}

function resetForm() {
  formTitle.textContent = "Add Destination";
  editId.value = "";
  cityInput.value = "";
  countryInput.value = "";
  descInput.value = "";
  submitBtn.textContent = "Add";
  cancelBtn.style.display = "none";
}

cancelBtn.addEventListener("click", resetForm);

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = {
    city: cityInput.value.trim(),
    country: countryInput.value.trim(),
    description: descInput.value.trim(),
  };

  if (editId.value) {
    await update(editId.value, data);
  } else {
    await create(data);
  }

  resetForm();
  renderList();
});

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

renderList();
