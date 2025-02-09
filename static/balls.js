<script>
    // Function to display the content for the selected box
    function showContent(box) {
        // Hide both Box A and Box B content
        document.getElementById("boxA-content").style.display = "none";
        document.getElementById("boxB-content").style.display = "none";
        
        // Show the selected box content
        var target = document.getElementById("box" + box + "-content");
        if (target) {
            target.style.display = "block";
        }
    }

    // Function to open the appropriate modal
    function revealAnswer(box) {
        // Display the corresponding modal for the selected box
        document.getElementById('answerModal' + box).style.display = "block";
    }

    // Function to close the modal
    function closeModal(box) {
        // Hide the corresponding modal for the selected box
        document.getElementById('answerModal' + box).style.display = "none";
    }

    // When the page loads (or reloads after a POST), show the correct box content and reveal button if applicable.
    window.onload = function() {
        var selectedBox = "{{ selected_box }}";
        
        // If a box is selected, show its content and reveal button if there is a message
        if (selectedBox) {
            showContent(selectedBox);
            
            if ("{{ message }}") {
                document.getElementById("reveal-button-" + selectedBox).style.display = "inline-block";
            }
        }
    };
</script>
