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


    // Apply color to gas light if fuel < 20%
    if (vehicle_data_array['vehicle_fuel'] < 20) {
        const style = document.createElement('style');

        style.innerHTML = `#fuel-light {
            fill: green !important;
            filter: drop-shadow(0 0 0.75rem #00b815);
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

// Function for accessing maintenance data from python dictionary
async function get_maintenance(){
    // Return an array of vehicle repairs
    let vehicle_maintenance_array = await eel.get_maintenance()();
    
    // Create a sort of empty table string
    var t = "";
    for (var i = 0; i < vehicle_maintenance_array.length; i++){
        var tr = "<tr>";
        tr += "<td id='part' class='p-2 whitespace-nowrap'>"+vehicle_maintenance_array[i]['RepairPart']+"</td>";
        tr += "<td class='p-2 whitespace-nowrap'>"+vehicle_maintenance_array[i]['RepairType']+"</td>";
        tr += "<td class='p-2 whitespace-nowrap'>"+vehicle_maintenance_array[i]['RepairDate']+"</td>";
        tr += "<td class='p-2 whitespace-nowrap'>"+vehicle_maintenance_array[i]['RepairMiles']+"</td>";
        tr += `<td>
                    <a href="#" class="bg-blue-500 p-2 text-white hover:shadow-lg text-xs font-thin">Edit</a>
                    <a href="#" class="bg-red-500 p-2 text-white hover:shadow-lg text-xs font-thin">Remove</a>
                </td>`;
        tr += "</tr>";
        t += tr;
    }
    document.getElementById("posts").innerHTML += t;
}