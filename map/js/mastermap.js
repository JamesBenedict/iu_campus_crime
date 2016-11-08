var map = L.map('map').setView([39.166809, -86.521733], 14);

var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
	// subdomains: 'abcd',
	maxZoom: 19
}).addTo(map);

// var geojsonLayer = new L.GeoJSON.AJAX("clean_crime.geojson");  

// var geojsonLayer = L.geoJson.ajax('clean_crime.geojson', {
//   filter: function(feature, layer) {
//       return feature.properties.crime_class == 'Rape';
//   }
// });
// geojsonLayer.addTo(map)

// geojson = {
//   "type": "FeatureCollection",
//   "features": [
//     {
//       "type": "Feature",
//       "geometry": {
//         "type": "Point",
//         "coordinates": [
//           -86.50421,
//           39.172518
//         ]
//       },
//       "properties": {
//         "report_num": "153468",
//         "date": "12/22/15 0:00",
//         "crime_class": "Trespass",
//         "crime": "TRESPASS & MALICIOUS TRESPASS",
//         "location": "TULIP TREE PARKING LOT",
//         "address": "na",
//         "city": "Bloomington",
//         "state": "Indiana",
//         "status": "CLOSED"
//       }
//     },
//     {
//       "type": "Feature",
//       "geometry": {
//         "type": "Point",
//         "coordinates": [
//           -86.497986,
//           39.17236
//         ]
//       },
//       "properties": {
//         "report_num": "153441",
//         "date": "12/17/15 0:00",
//         "crime_class": "Traffic",
//         "crime": "TRESPASS & MALICIOUS TRESPASS",
//         "location": "STONEBELT",
//         "address": "na",
//         "city": "Bloomington",
//         "state": "Indiana",
//         "status": "ACTIVE"
//       }
//     }]}




var geo = L.geoJson.ajax('clean_crime.geojson', {

   style: function(feature) {
        if (feature.properties.crime_class == 'Rape'){
          return {color: '#be4c39'};
        } else{
          return {color: '#ccc'};
        }
        
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 10, fillOpacity: 0.5});
    },
    // filter: function(feature, layer) {
    //     return feature.properties.crime_class == 'Rape';
    // }
});




map.addLayer(geo);


// L.geoJSON(mydata).addTo(map);


// new L.GeoJSON('maser_crime.geojson').addTo(map);

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
