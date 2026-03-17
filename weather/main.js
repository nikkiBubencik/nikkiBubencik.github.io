const weatherResult = document.getElementById('weather-result');
const weatherForm = document.getElementById('weather-form');

weatherForm.addEventListener('submit', async function(event) {
  event.preventDefault();
  weatherResult.innerHTML = "";
  weatherResult.style.color = "black";

  const city = document.getElementById('city').value;
  
  fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${city}`)
    .then(response => response.json())
    .then(response => {
      if (results.length == 0){
        weatherResult.textContent = `Error fetching location ${city}`;
        weatherResult.style.color = "red";
        return;
      }
      const { latitude, longitude, name } = response.results[0]; 

      fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`)
        .then(response => response.json())
        .then(data => {
          const weather = data.current_weather;
          const locName = document.createElement('h2');
          locName.textContent = name;
          
          const temp = document.createElement('p');
          temp.textContent = `Temp: ${weather.temperature}°C`;
      
          const wind = document.createElement('p');
          wind.textContent = `Wind: ${weather.windspeed} km/h`;
          
          weatherResult.appendChild(locName);
          weatherResult.appendChild(temp);
          weatherResult.appendChild(wind);
        })
        .catch(err => {
          console.error(err)
          weatherResult.textContent = "Error fetching location";
          weatherResult.style.color = "red";
        });
  })
  .catch(err => { console.error(err)
  weatherResult.textContent = "Error fetching location";
  weatherResult.style.color = "red";
});
});
    
  
