import requests

url = "https://cds.nccs.nasa.gov/nex-gddp/data?model=GFDL-ESM2M&scenario=rcp45&variables=tmin,tmax,pr&latitude=34.0522&longitude=-118.2437&start=2030-01-01&end=2040-12-31&format=netCDF"

response = requests.get(url)
with open('climate_data.nc', 'wb') as file:
    file.write(response.content)
