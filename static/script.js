console.log('Script loaded successfully!');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');
    
    const form = document.getElementById('predictionForm');
    if (!form) {
        console.error('Form not found!');
        return;
    }
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        console.log('Form submitted!');
        
        const data = {
            DRYBULBTEMPF: parseFloat(document.getElementById('drybulb').value),
            RelativeHumidity: parseFloat(document.getElementById('humidity').value),
            WindSpeed: parseFloat(document.getElementById('windspeed').value),
            WindDirection: parseFloat(document.getElementById('winddirection').value),
            SealevelPressure: parseFloat(document.getElementById('pressure').value)
        };
        
        console.log('Sending data:', data);
        
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            console.log('Response status:', response.status);
            const result = await response.json();
            console.log('Result:', result);
            
            if (response.ok) {
                const predictionElement = document.getElementById('prediction');
                const resultElement = document.getElementById('result');
                
                predictionElement.textContent = `${result.visibility.toFixed(2)} miles`;
                resultElement.classList.remove('hidden');
                
                console.log('Prediction displayed:', result.visibility);
            } else {
                alert('Error: ' + result.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to connect to server: ' + error.message);
        }
    });
});
