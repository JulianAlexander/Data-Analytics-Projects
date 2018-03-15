var select = document.getElementById("samples");
var names_url = "http://127.0.0.1:5000/names"
Plotly.d3.json(names_url, function(error, response){
    if (error) return console.warn(error);
    var names = [response];
    return names;
});

for (var i = 0; i < names.length; i++) {
    var opt = names[i];
    var el = document.createElement("option");
    return opt;
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
}