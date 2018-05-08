$(window).load(function(){
    // Ajax Code Here
    $("div.graph").each(function(){
        var id_chart = $(this).attr("id");
        var pk_host = id_chart.split('.')[1];
        var service_name = id_chart.split('.')[2];

        (function update() {
        $.ajax({
//            url: '{% url "get_data" %}',
            url: '/ajax/get_data/' + pk_host + '/' + service_name,
            dataType: 'json',
            success: function (data) {
//                alert(data[0]['max']);
                var dps_max = [];
                var dps_min = [];
                var chart = new CanvasJS.Chart(id_chart, {
                    exportEnabled: true,
                    title: {
//                        text: "HOST"
                    },
                    axisY: {
                        includeZero: false,
                        suffix: " ms"
                    },
                    data: [{
                        name: "Max",
                        type: "spline",
                        markerSize: 0,
                        xValueType: "dateTime",
                        showInLegend: true,
                        dataPoints: dps_max
                    },
                    {
                        name: "Min",
                        type: "spline",
                        markerSize: 0,
                        xValueType: "dateTime",
                        showInLegend: true,
                        dataPoints: dps_min
                    }]
                });

                var xVal = data[0]['time'];
                var yMaxVal = data[0]['max'];
                var yMinVal = data[0]['min'];
//                var updateInterval = 1000;
                var dataLength = data.length;
                var updateChart = function (count) {
                    count = count || 1;
                    // count is number of times loop runs to generate random dataPoints.
                    for (var j = 0; j < count; j++) {
                        yMaxVal = data[j]['max'];
                        yMinVal = data[j]['min'];
                        xVal = data[j]['time'];
                        dps_max.push({
                            x: xVal,
                            y: yMaxVal
                        });
                        dps_min.push({
                            x: xVal,
                            y: yMinVal
                        });
//                        xVal++;
                    }
                    if (dps_max.length > dataLength) {
                        dps_max.shift();
                    }
                    chart.render();
                };

                updateChart(dataLength);
//                setInterval(function () { updateChart() }, updateInterval);
            },
            failure: function(data) {
                alert('Got an error dude');
            }
        }).then(function() {           // on completion, restart
           setTimeout(update, 10000);  // function refers to itself
        });
    })();
    });

});

filterSelection("all")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
  if (c == "all") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1); 
    }
  }
  element.className = arr1.join(" ");
}

// Add active class to the current control button (highlight it)
var btnContainer = document.getElementById("my_service_menu");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = btnContainer.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}