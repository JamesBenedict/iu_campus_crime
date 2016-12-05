// load map on bloomington
var map = L.map('workingMap').setView([39.171612, -86.521097], 14);

// sets background tiles
var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
	// attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
	// subdomains: 'abcd',
	maxZoom: 19
}).addTo(map);

var crimes = L.geoJson.ajax('../crime_map/data/json/clean_crime.geojson', {

 
   style: function(feature) {
        if (feature.properties.crime_class == 'alcohol'){
          return {color: '#6cd05f'};
        } else if (feature.properties.crime_class == 'fake_id'){
          return {color: '#000'};
        } else if (feature.properties.crime_class == 'marijuana'){
          return {color: '#6f3fcc'};
        } else if (feature.properties.crime_class == 'possession'){
          return {color: '#c3db42'};
        }

        else if (feature.properties.crime_class == 'disorderly_conduct'){
          return {color: '#c84eca'};
        } else if (feature.properties.crime_class == 'drug_sale'){
          return {color: '#84d1ad'};
        } else if (feature.properties.crime_class == 'DUI'){
          return {color: '#462a79'};
        }

        else if (feature.properties.crime_class == 'assault'){
          return {color: '#cd7f38'};
        } else if (feature.properties.crime_class == 'missing_person'){
          return {color: '#000'};
        } else if (feature.properties.crime_class == 'resisting_arrest'){
          return {color: '#d1bd60'};
        } else if (feature.properties.crime_class == 'robbery'){
          return {color: '#8B2700 '};
        }

        else if (feature.properties.crime_class == 'sexual_misconduct'){
          return {color: '#d94a86'};
        } else if (feature.properties.crime_class == 'domestic'){
          return {color: '#cd7f38'};
        } else if (feature.properties.crime_class == 'harrassment'){
          return {color: '#d48d40'};
        } else if (feature.properties.crime_class == 'rape'){
          return {color: '#dd0606'};
        } else if (feature.properties.crime_class == 'stalking'){
          return {color: '#ffcc00'};
        }

        else if (feature.properties.crime_class == 'property'){
          return {color: '#63c29d'};
        } else if (feature.properties.crime_class == 'theft'){
          return {color: '#606a90'};
        } else if (feature.properties.crime_class == 'tresspass'){
          return {color: '#63c29d'};
        }
      
        else{
          return {color: '#000'};
        } 
        // return {color: '#be4c39'}
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 5, fillOpacity: 0.3, stroke: 0});
    },

    onEachFeature: function(feature, layer) {
    // does this feature have a property named popupContent?
     if (feature.properties && feature.properties.crime) {
          layer.bindPopup(feature.properties.crime);
      }
    },

     filter: function(feature){
      if (feature.properties.crime_class == "accidental_death") return false
      if (feature.properties.crime_class == "non-criminal") return false
      if (feature.properties.crime_class == "traffic") return false
      if (feature.properties.crime_class == "nuisance") return false
      if (feature.properties.crime_class == "suicide") return false
      if (feature.properties.crime_class == "arson") return false


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


