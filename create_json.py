#!C:\Users\N.DeInnocentis\Miniconda3\python.exe
# Import modules for CGI handling 
import cgi, cgitb 

import os
import geopandas
import webbrowser
import folium
from shapely.geometry import Point


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
city = form.getvalue('city')
address  = form.getvalue('address')
lat = float(form.getvalue('lat'))
lon = float(form.getvalue('lon'))



print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Create JSON</title>")
print ("</head>")
print ("<body>")
print ("<h2>La tua fontanella in  %s %s</h2>" % (address, city))
print ("<h4>Latitudine:  %s </h4>" % (lat))
print ("<h4>Longitudine:  %s </h4>" % (lon))


filename = 'fontanelle.geojson'
file = open(filename)
fontanelle = geopandas.read_file(file)

data = { 'node': '639832150', 'indirizzo': address, 'img': '', 'status': 2, 'city': city, 'country': '', 'geometry': [Point(lon, lat)]}
row = geopandas.GeoDataFrame(data, crs="EPSG:4326")

fontanelle_new=fontanelle.append(row,ignore_index = True)
#print(fontanelle)
file.close()
fontanelle_new.to_file("fontanelle.geojson",driver='GeoJSON')
print("<p>Aggiunta fontanella</p>")

m = folium.Map(location=[lat,lon])
folium.Marker([lat, lon]).add_to(m)
m.save("index.html")


print("<iframe width='80%' height='300px' src='http://localhost/pythonscript/index.html'></iframe>")
print ("</body>")
print ("</html>")
#webbrowser.open("index.html",new=2)




