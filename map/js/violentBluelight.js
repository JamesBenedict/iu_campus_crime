// load map on bloomington
var map = L.map('violentBluelight').setView([39.171612, -86.521097], 14);

// sets background tiles
var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
  // attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
  // subdomains: 'abcd',
  maxZoom: 19
}).addTo(map);

var crimes = L.geoJson.ajax('../data/json/clean_crime.geojson', {

 
   style: function(feature) {
        // if (feature.properties.crime_class == 'alcohol'){
        //   return {color: '#17655C'};
        // } else if (feature.properties.crime_class == 'fake_id'){
        //   return {color: '#b2df8a'};
        // } else if (feature.properties.crime_class == 'marijuana'){
        //   return {color: '#055d00'};
        // } else if (feature.properties.crime_class == 'possession'){
        //   return {color: '#63c29d'};
        // }

        // else if (feature.properties.crime_class == 'disorderly_conduct'){
        //   return {color: '#63c29d'};
        // } else if (feature.properties.crime_class == 'drug_sale'){
        //   return {color: '#63c29d'};
        // } else if (feature.properties.crime_class == 'DUI'){
        //   return {color: '#63c29d'};
        // }

        // else if (feature.properties.crime_class == 'assault'){
        //   return {color: '#7F3663'};
        // } else if (feature.properties.crime_class == 'missing_person'){
        //   return {color: '#c3519e'};
        // } else if (feature.properties.crime_class == 'resisting_arrest'){
        //   return {color: '#C18BDA'};
        // } else if (feature.properties.crime_class == 'robbery'){
        //   return {color: '#6F2ED0'};
        // }

        // else if (feature.properties.crime_class == 'sexual_misconduct'){
        //   return {color: '#8B2700'};
        // } else if (feature.properties.crime_class == 'domestic'){
        //   return {color: '#E04119'};
        // } else if (feature.properties.crime_class == 'harrassment'){
        //   return {color: '#d48d40'};
        // } else if (feature.properties.crime_class == 'rape'){
        //   return {color: '#bf6363'};
        // } else if (feature.properties.crime_class == 'stalking'){
        //   return {color: '#ffcc00'};
        // }

        // else if (feature.properties.crime_class == 'property'){
        //   return {color: '#63c29d'};
        // } else if (feature.properties.crime_class == 'theft'){
        //   return {color: '#63c29d'};
        // } else if (feature.properties.crime_class == 'tresspass'){
        //   return {color: '#63c29d'};
        // }
      
        // else{
        //   return {color: '#000'};
        // } 


        return {color: '#be4c39'}
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
      
      if (feature.properties.crime_class == "assault") return true
      if (feature.properties.crime_class == "disorderly_conduct") return true
      if (feature.properties.crime_class == "missing_person") return true
      if (feature.properties.crime_class == "resisting_arrest") return true
      if (feature.properties.crime_class == "robbery") return true
      if (feature.properties.crime_class == "sexual_misconduct") return true
      if (feature.properties.crime_class == "domestic Violence") return true
      if (feature.properties.crime_class == "harrassment") return true
      if (feature.properties.crime_class == "rape") return true
      if (feature.properties.crime_class == "stalking") return true
      if (feature.properties.crime_class == "property") return true
      if (feature.properties.crime_class == "theft") return true
      if (feature.properties.crime_class == "tresspass") return true
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

map.addLayer(bluelights);
map.addLayer(crimes);


