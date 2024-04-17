document.addEventListener("DOMContentLoaded", function() {
    const postForm = document.getElementById("post-form");

    postForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const title = document.getElementById("title").value;
        const content = document.getElementById("content").value;

        // AJAX request to add the post
        fetch("{% url 'add_post' %}", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify({ title: title, content: content })
        })
        .then(response => response.json())
        .then(data => {
            // Add the new post to the posts section
            const postsContainer = document.querySelector(".posts");
            const postElement = document.createElement("div");
            postElement.innerHTML = `
                <h2>${data.title}</h2>
                <p>${data.content}</p>
            `;
            postsContainer.prepend(postElement);

            // Clear the form fields
            document.getElementById("title").value = "";
            document.getElementById("content").value = "";
        })
        .catch(error => console.error("Error:", error));
    });
});
