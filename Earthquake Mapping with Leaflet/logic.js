var queryURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
var queryURL2 = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02&maxlongitude=-69.52148437&minlongitude=-123.83789062&maxlatitude=48.74894534&minlatitude=25.16517337";

d3.json(queryURL, function(error, data){
    if (error) console.warn(error);
    console.log(data.features);
    createMarkers(data.features);
})

function createMarkers(earthquakeData) {
        // Define a function we want to run once for each feature in the features array
        // Give each feature a popup describing the place and time of the earthquake
        function onEachFeature(feature, layer) {
          layer.bindPopup("<h3>" + feature.properties.place +
            "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
        }
        var geojsonMarkerOptions = {
            radius: function findRadius(feature){
                    return feature.properties.mag},
            fillColor: "#ff7800",
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        };
        // Create a GeoJSON layer containing the features array on the earthquakeData object
        // Run the onEachFeature function once for each piece of data in the array
        var earthquakes = L.geoJSON(earthquakeData, {
          onEachFeature: onEachFeature,
          pointToLayer: function (feature, latlng) {
            var color,
                mag,
                radius;
            mag = feature.properties.mag;
            if (mag === null) {
              color = '#000';
              radius = 3;
            } else {
              color = d3.rgb(255/mag, 30/mag, 30/mag);
              radius = 3 * Math.max(mag, 1);
            }
            //if (feature.properties.type === 'quarry blast') {
            //  color = '#f00';
            //}
            return L.circleMarker(latlng, {
              color: color,
              radius: radius
            });
          }
        });
        // Sending our earthquakes layer to the createMap function
        createMap(earthquakes);
      
};

function createMap(earthquakes){

    var darkMapBox = L.tileLayer("https://api.mapbox.com/styles/v1/julianalexander/cjez3ryi74tjx2rqrvnbsiykr/tiles/256/{z}/{x}/{y}?"+
    "access_token=pk.eyJ1IjoianVsaWFuYWxleGFuZGVyIiwiYSI6ImNqZXZwM2puNTBwO"+
    "HIyeW43cjNsNWNnanQifQ.rnM8MJ-3OxfUwtCEQwhshw");

    var lightMapBox = L.tileLayer("https://api.mapbox.com/styles/v1/julianalexander/cjez4l9514to52rmrze17k83n/tiles/256/{z}/{x}/{y}?"+
    "access_token=pk.eyJ1IjoianVsaWFuYWxleGFuZGVyIiwiYSI6ImNqZXZwM2puNTBwO"+
    "HIyeW43cjNsNWNnanQifQ.rnM8MJ-3OxfUwtCEQwhshw");

    var baseMaps = {
        "Normal Map": lightMapBox,
        "Dark Map": darkMapBox
    };

    var overlayMaps = {
        Earthquakes: earthquakes
    }

    var myMap = L.map("map", {
        center: [37.09, -95.71],
        timeDimension: true,
        timeDimensionControl: true,
        zoom: 5,
        layers: [lightMapBox, darkMapBox]
    });

    L.control.layers(baseMaps, overlayMaps,{
        collapsed: false
    }).addTo(myMap);

    var legend = L.control({ position: 'bottomright' })
    legend.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend')
        var limits = earthquakes.options.limits
        var colors = earthquakes.options.colors
        var labels = []
    
    div.innerHTML = '<div class="labels"><div class="min">' + limits[0] + '</div> \
    <div class="max">' + limits[limits.length - 1] + '</div></div>'

    limits.forEach(function (limit, index) {
    labels.push('<li style="background-color: ' + colors[index] + '"></li>')
    })

    div.innerHTML += '<ul>' + labels.join('') + '</ul>'
    return div
    }
    legend.addTo(map)

};