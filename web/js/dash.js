async function vehicle_data() {
    let mph_div = document.getElementById('mph');
    let rpm_div = document.getElementById('rpm');
    let mpg_div = document.getElementById('mpg');
    let voltage_div = document.getElementById('voltage');
    let coolant_div = document.getElementById('coolant');

    let check_engine = document.getElementById('check-engine');
    
    // Call from Python so we can access the returned array of vehicle data
    let vehicle_data_array = await eel.vehicle_data()();
    mph_div.innerText = vehicle_data_array['vehicle_speed'];
    rpm_div.innerText = vehicle_data_array['vehicle_rpm'];
    mpg_div.innerText = vehicle_data_array['vehicle_fuel'] + '%';
    voltage_div.innerText = vehicle_data_array['vehicle_voltage'] + ' volts';
    coolant_div.innerText = vehicle_data_array['vehicle_coolant'] + 'F';

    // Get DTC count
    check_engine_count = vehicle_data_array['vehicle_codes'];
    
    // Apply color to check engine if DTC > 0
    if (check_engine_count > 0) {
        const style = document.createElement('style');

        style.innerHTML = `#check-engine {
            fill: darkorange !important;
            filter: drop-shadow(0 0 0.75rem #ff6e3d);
        } `

        document.head.appendChild(style);
    }
}

function showTime(){
    var date = new Date();
    var h = date.getHours(); // 0 - 23
    var m = date.getMinutes(); // 0 - 59
    var session = "AM";
    
    if(h == 0){
        h = 12;
    }
    
    if(h > 12){
        h = h - 12;
        session = "PM";
    }
    
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    
    var time = h + ":" + m + " " + session;
    document.getElementById("thetime").innerText = time;
    document.getElementById("thetime").textContent = time;
    
    setTimeout(showTime, 60000);
}
