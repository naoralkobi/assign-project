function updateBackgroundColor(selectElement) {
    if (selectElement.value === "exist") {
        selectElement.classList.add("exist");
        selectElement.classList.remove("not-exist");
    } else if (selectElement.value === "not exist") {
        selectElement.classList.add("not-exist");
        selectElement.classList.remove("exist");
    } else {
        selectElement.classList.remove("exist", "not-exist");
    }
}

function updatePresence(selectElement, soldierId) {
    const selectedHour = document.getElementById('hour-select').value;
    const hiddenInput = document.getElementById(`hidden_presence_${soldierId}_${selectedHour}`);
    hiddenInput.value = selectElement.value;
    updateBackgroundColor(selectElement);
}

function selectHour(selectElement) {
    const selectedHour = selectElement.value;
    const presenceSelects = document.querySelectorAll('.presence-select');
    presenceSelects.forEach(select => {
        const soldierId = select.id.split('_')[1];  // Extract soldier ID from the select ID
        const hiddenInput = document.getElementById(`hidden_presence_${soldierId}_${selectedHour}`);
        select.value = hiddenInput.value;
        updateBackgroundColor(select);
    });
}

// Initialize the background colors and set the selects to the correct value based on hidden inputs
document.querySelectorAll('.presence-select').forEach(selectElement => {
    const soldierId = selectElement.id.split('_')[1];
    const selectedHour = document.getElementById('hour-select').value;
    const hiddenInput = document.getElementById(`hidden_presence_${soldierId}_${selectedHour}`);
    selectElement.value = hiddenInput.value;
    updateBackgroundColor(selectElement);
});
