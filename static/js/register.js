document.getElementById('registerForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // Prevent page reload

    const messageDiv = document.getElementById('message');
    const submitBtn = document.getElementById('submitBtn');
    
    // 1. Get values
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // 2. Client-side Validation (Check match password)
    if (password !== confirmPassword) {
        messageDiv.textContent = "Error: Passwords do not match!";
        messageDiv.className = "message error";
        return; // Stop here
    }

    if (password.length < 6) {
        messageDiv.textContent = "Error: Password must be at least 6 characters.";
        messageDiv.className = "message error";
        return;
    }

    // 3. Prepare Data (Only send what Backend expects)
    const formData = {
        email: email,
        password: password,
        first_name: firstName,
        last_name: lastName
        // Do NOT send confirmPassword to backend, Pydantic will reject it
    };

    // UI Loading State
    messageDiv.textContent = "Creating account...";
    messageDiv.className = "message";
    submitBtn.disabled = true;
    submitBtn.style.opacity = "0.7";

    try {
        // 4. Call API
        const response = await fetch('/api/users/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        // 5. Handle Response
        if (response.ok) {
            // Success
            messageDiv.textContent = `Success! Welcome, ${result.email}. Redirecting to login...`;
            messageDiv.className = "message success";
            
            // Wait 2 seconds then go to login page
            setTimeout(() => {
                window.location.href = "/login";
            }, 2000);
        } else {
            // Error from Backend (e.g., Email already exists)
            messageDiv.textContent = `Error: ${result.detail || "Something went wrong"}`;
            messageDiv.className = "message error";
            submitBtn.disabled = false;
            submitBtn.style.opacity = "1";
        }

    } catch (error) {
        // Network Error
        console.error('Error:', error);
        messageDiv.textContent = "Network error. Please try again later.";
        messageDiv.className = "message error";
        submitBtn.disabled = false;
        submitBtn.style.opacity = "1";
    }
});