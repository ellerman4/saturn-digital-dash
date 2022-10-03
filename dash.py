import eel
import obd
from obd import OBDStatus
from datetime import datetime
import sqlite3
from sqlite3 import Error
import time
from time import strftime
# Set web files folder
eel.init('web')

@eel.expose
def vehicle_data():
    vehicle_dict = {}
    # Try to make a connection via ELM327 OBD-II interface
    try:
        connection = obd.OBD(fast=False) # auto-connects to USB or RF port

        vehicle_dict['vehicle_speed'] = connection.query(obd.commands.SPEED).value.to("mph") # send the command, and parse the response
        vehicle_dict['vehicle_rpm'] = connection.query(obd.commands.RPM).value
        vehicle_dict['vehicle_fuel'] = connection.query(obd.commands.FUEL_LEVEL).value
        vehicle_dict['vehicle_codes'] = connection.query(obd.commands.DTC_count).value
        vehicle_dict['vehicle_voltage'] = connection.query(obd.commands.ELM_VOLTAGE).value
        vehicle_dict['vehicle_coolant'] = connection.query(obd.commands.COOLANT_TEMP).value

    # Use default values if failed
    except:
        vehicle_dict['vehicle_speed'] = 0
        vehicle_dict['vehicle_rpm'] = 800
        vehicle_dict['vehicle_fuel'] = 100
        vehicle_dict['vehicle_codes'] = 0
        vehicle_dict['vehicle_voltage'] = 12.8
        vehicle_dict['vehicle_coolant'] = 200

        print('Connection failed...')

    return vehicle_dict

# Attempt to initialize the connection to the database
# Refactor later to not use global variables
def init_db():
    global con
    try:
        con = sqlite3.connect('db.db')
        con.row_factory = sqlite3.Row   # Use row_factory to return a dictionary
        return con.cursor()

    except Error as e:
        return e


# Test CRUD functionality for vehicle_maintenance
# Read all data from the  vehicle_maintenance table
@eel.expose
def get_maintenance():
    global cursor
    cursor = init_db()
    cursor.execute('select * from vehicle_maintenance')
    return [dict(row) for row in cursor.fetchall()]     # Return as a python dict to access as an array in js

# Create a new item in the vehicle_maintenance table
@eel.expose
def new_item(repair_part, repair_type, repair_miles):
    cursor.execute(f'''INSERT INTO vehicle_maintenance (RepairPart, RepairDate, RepairType, RepairMiles)
                    VALUES ('{repair_part}', date(), '{repair_type}', {repair_miles});''')
    con.commit()

# Update an item in the vehicle_maintenance table
@eel.expose
def update_item(repair_part, repair_type, repair_miles, repair_id):
    cursor.execute(f'''UPDATE vehicle_maintenance
                        SET (RepairPart, RepairType, RepairDate, RepairMiles) = (?, ?, ?, ?)
                        WHERE RepairID = ?;''', (repair_part, repair_type, strftime("%Y-%m-%d"), repair_miles, repair_id ))   # Add primary key to table and use repair_id instead
    con.commit()

# Delete an item in the vehicle_maintenance table
@eel.expose
def delete_item(repair_id):
    cursor.execute(f'''DELETE FROM vehicle_maintenance
                        WHERE RepairID = ?;''', (repair_id,))
    con.commit()


# Start Eel application on the splashscreen
eel.start('templates/splash.html',
        size=(800, 650),
        jinja_templates='templates')  # Point to templates folder for Jinja templating