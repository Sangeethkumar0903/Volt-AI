function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an image file.");
        return;
    }

    // Validate file type
    if (!file.type.match('image/jpeg')) {
        alert("Please upload a valid JPG/JPEG image.");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error: " + data.error);
            return;
        }

        // ✅ Display Heat Prediction Result Only (No Image)
        document.getElementById('status').innerText = 
            `Status: ${data.status} (Heat Risk: ${data.heat_issue_probability.toFixed(2)})`;
        document.getElementById('status').classList.remove("hidden");
    })
    .catch(error => console.error("Upload Error:", error));
}
