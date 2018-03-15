var $tbody = document.querySelector('tbody');
var $stateInput = document.querySelector('#state');
var $searchBtn = document.querySelector('#search');
var $filterInput = document.querySelector('#state');
$searchBtn.addEventListener('click', handleSearchButtonClick);

var alienData = dataSet;
function renderTable() {
  $tbody.innerHTML = '';
  for (var i = 0; i < alienData.length; i++) {
    var address = alienData[i];
    //console.log(alienData[i])
    var fields = Object.keys(address);
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      var field = fields[j];
      //console.log(fields[j]);
      var $cell = $row.insertCell(j);
      $cell.innerText = address[field];
    }
  }
}
function handleSearchButtonClick() {
  var filterState = $stateInput.value.trim().toLowerCase();
  alienData = dataSet.filter(function(address) {
    var addressState = address.datetime.toLowerCase();
    return addressState === filterState;
  });
  renderTable(); 
}


renderTable();