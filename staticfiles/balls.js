// Function to display the content for the selected box
function showContent(box) {
    document.querySelectorAll(".content-box").forEach(el => el.style.display = "none");
    document.getElementById("box" + box + "-content").style.display = "block";
}

// Function to open the modal for the correct box
function revealAnswer(box) {
    document.getElementById('answerModal' + box).style.display = "block";
}

// Function to close the modal
function closeModal(box) {
    document.getElementById('answerModal' + box).style.display = "none";
}

// When the page loads (or reloads after a POST), show the correct box content and reveal button if applicable.
window.onload = function() {
    var selectedBox = "{{ selected_box }}";
    if (selectedBox) {
        showContent(selectedBox);
        if ("{{ message }}") {
            document.getElementById("reveal-button-" + selectedBox).style.display = "inline-block";
        }
    }
};
