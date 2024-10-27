document.getElementById('spamForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const emailText = document.getElementById('emailText').value;
    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `email_text=${encodeURIComponent(emailText)}`
    });
    
    const result = await response.json();
    document.getElementById('result').innerText = result.prediction || 'Error';
});
