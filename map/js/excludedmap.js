// load map on bloomington
var map = L.map('excludedMap').setView([39.171612, -86.521097], 14);

// sets background tiles
var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
	// attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
	// subdomains: 'abcd',
	maxZoom: 19
}).addTo(map);

var crimes = L.geoJson.ajax('../data/json/clean_crime.geojson', {

 
   style: function(feature) {
        if (feature.properties.crime_class =="accidental_death"){
            return {color: '#17655C'};
        } else if (feature.properties.crime_class =="non-criminal"){
            return {color: '#17655C'};
        } else if (feature.properties.crime_class =="traffic"){
            return {color: '#17655C'};
        } else if (feature.properties.crime_class =="nuisance"){
            return {color: '#17655C'};
        } else if (feature.properties.crime_class =="suicide"){
            return {color: '#17655C'};
        } else if (feature.properties.crime_class =="arson"){
            return {color: '#17655C'};
        } else{
            return {color: '#be4c39'};
        }
        
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 5, fillOpacity: 0.3, stroke: 0});
    },

    onEachFeature: function(feature, layer) {
    // does this feature have a property named popupContent?
     if (feature.properties && feature.properties.crime) {
          layer.bindPopup(feature.properties.crime);
      }
    }

  
});

// map.addLayer(crimes);
var bluelights = L.geoJson.ajax('../data/json/bluelights.geojson', {
 style: function(feature) {
//         if (feature.properties.crime_class == 'alcohol'){
//           return {color: '#17655C'};
      return {color: '#4b6892'};
},
 pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 10, fillOpacity: 0.3, stroke: 0})
       

    },
  

});

// map.addLayer(bluelights);
map.addLayer(crimes);


