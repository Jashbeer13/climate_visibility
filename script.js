document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        DRYBULBTEMPF: parseFloat(document.getElementById('drybulb').value),
        RelativeHumidity: parseFloat(document.getElementById('humidity').value),
        WindSpeed: parseFloat(document.getElementById('windspeed').value),
        WindDirection: parseFloat(document.getElementById('winddirection').value),
        SealevelPressure: parseFloat(document.getElementById('pressure').value)
    };
    
    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            document.getElementById('prediction').textContent = `${result.visibility.toFixed(2)} miles`;
            document.getElementById('result').classList.remove('hidden');
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Failed to connect to server. Make sure the backend is running.');
    };
});
