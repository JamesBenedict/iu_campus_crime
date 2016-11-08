var map = L.map('map').setView([39.166809, -86.521733], 14);

var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
	// subdomains: 'abcd',
	maxZoom: 19
}).addTo(map);

var geo = L.geoJson.ajax('../data/json/clean_crime.geojson', {

   style: function(feature) {
        if (feature.properties.crime_class == 'alcohol'){
          return {color: '#be4c39'};
        } else if (feature.properties.crime_class == 'Rape'){
          return {color: '#be4c39'};
        }


        else{
          return {color: '#ccc'};
        }
        
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 10, fillOpacity: 0.5});
    },
  
});




map.addLayer(geo);

// var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
// 	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
// 	// subdomains: 'abcd',
// 	maxZoom: 19
// }).addTo(mymap);

// var mymap = L.map('mapid').setView([39.166809, -86.521733], 16)

// var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
// 	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
// 	// subdomains: 'abcd',
// 	maxZoom: 19
// }).addTo(mymap);
