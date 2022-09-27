<p align="center"><img src="https://i.gyazo.com/76824485882a7008dd8238b57278e229.png" width="600px"></p>

<h1 align="center">Saturn Digital Dash</h1>

<h3 align="center">
A digital dash built with <a href="https://github.com/ChrisKnott/Eel">Eel</a>.
</h3>


<br/>

<h3 align="center">
Made with
</h3>

<p align="center"><a href="https://github.com/ChrisKnott/Eel">Eel</a> for GUI design</p>

<p align="center"><a href="https://tailwindcss.com/">Tailwind CSS</a> for for styling</p>

<p align="center"><a href="https://jinja.palletsprojects.com/en/3.1.x/">Jinja2</a> for HTML templating</p>

<p align="center"><a href="https://github.com/brendan-w/python-OBD">python-OBD</a> for reading data via OBD-II</p>

## Todo

#### Live readouts for:
- [ ] Fuel Pressure
- [x] MPH, RPM, Fuel
- [ ] Shift indicator
- [ ] Engine Coolant Temperature
- [ ] Battery voltage


## Usage
#### Note: This project is a WIP and should not be used in any vehicle as a main dash
```
$ git clone https://github.com/ellerman4/saturn-digital-dash
```

Pip install Eel (with jinja2 support) and python-OBD
```cmd

...\> pip install eel[jinja2]

...\> pip install obd

```

Run main dash.py script
```cmd
...\> python dash.py

```

For building a distributable binary with PyInstaller, read more [here](https://github.com/ChrisKnott/Eel).

##
</br>
<p align="center">
<a href="https://github.com/ellerman4/"><img alt="alt_text" width="400px" src="https://user-images.githubusercontent.com/106990217/187055083-ceeb562c-3bed-45ef-937b-4d9b5af5455c.png" /></a></p>
