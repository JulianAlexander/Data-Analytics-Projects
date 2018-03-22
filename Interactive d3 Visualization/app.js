// Define SVG area dimensions
var svgWidth = 1200;
var svgHeight = 900;

// Define the chart's margins as an object
var chartMargin = {
  top: 20,
  right: 20,
  bottom: 30,
  left: 40
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3
  .select("body")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth)
  .append("g")
  .attr("transform", "translate(" + chartMargin.left + "," + chartMargin.top + ")")
  .attr("class","main");

// Append a group to the SVG area and shift ('translate') it to the right and down to adhere
// to the margins set in the "chartMargin" object.
//var chartGroup = svg.append("g")
//  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);



//setup x axis
var xValue = function(data){
  return data.meanIncome;},
    xScale = d3.scale.linear().range([0, chartWidth]),
    xMap = function(d) {return xScale(xValue(d));},
    xAxis = d3.svg.axis().scale(xScale).orient("bottom");

//setup y axis
var yValue = function(data){return data.veryGood;},
    yScale = d3.scale.linear().range([chartHeight, 0]),
    yMap = function(data){ return yScale(yValue(data));},
    yAxis = d3.svg.axis().scale(yScale).orient("left");

// setup fill color
var cValue = function(data) {return data.location;},
    color = d3.scale.category10();
// Load data 
d3.csv("d3_data1.csv", function (error, data) {

  // Log an error if one exists
  if (error) return console.warn(error);

  // Print the tvData
  console.log(data);

  // Changing values to a number for each data value
  data.forEach(function (d) {
    d.meanIncome = +d.meanIncome;
    d.excellent = +d.excellent;
    d.veryGood = +d.veryGood;
    d.good = +d.good;
    d.fair = +d.fair;
    d.poor = +d.poor;
  });


//buffer points
xScale.domain([d3.min(data, xValue)-10000, d3.max(data, xValue)+1]);
yScale.domain([d3.min(data, yValue)-5, d3.max(data, yValue)+2]);

//adding tooltip
var tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

var tip = d3.tip()
   .attr('class', 'd3-tip')
   .offset([-1, 0])
   .html(function(d) {
      return "<strong>State:</strong> <span style='color:red'>" + d.location + "</span>" + "</br>" + 
      "<strong>Mean Income:</strong> <span style='color:red'>" + d.meanIncome + "</span>" + "</br>" +
      "<strong>% Health:</strong> <span style='color:red'>" + Math.round(yScale.invert(d3.event.pageY)) + "</span>";
    })
svg.call(tip);

 // x-axis
 svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + chartHeight + ")")
    .call(xAxis)
    .append("text")
    .attr("class", "label")
    .attr("x", chartWidth)
    .attr("y",-6)
    .style("text-anchor", "end")
    .text("Mean Income ($)")
    .attr("font-size", "15px")
    .attr("font-weight", "bold");

// y axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy",".71em")
    .style("text-anchor", "end")
    .text("Excellent Health (%)")
    .attr("id", "excellent")
    .attr("font-size", "15px");

svg.append("g")
    .attr("class", "y axis")
    //.call(yAxis)
    .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy","2em")
    .style("text-anchor", "end")
    .text("Very Good Health (%)")
    .attr("id","veryGood")
    .attr("font-size", "15px")
    .attr("font-weight", "bold");

svg.append("g")
    .attr("class", "y axis")
    //.call(yAxis)
    .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy","3.3em")
    .style("text-anchor", "end")
    .text("Good Health (%)")
    .attr("id", "good")
    .attr("font-size", "15px");

svg.append("g")
    .attr("class", "y axis")
    //.call(yAxis)
    .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy","4.6em")
    .style("text-anchor", "end")
    .text("Fair Health (%)")
    .attr("id", "fair")
    .attr("font-size", "15px");

svg.append("g")
    .attr("class", "y axis")
    //.call(yAxis)
    .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy","5.9em")
    .style("text-anchor", "end")
    .text("Poor Health (%)")
    .attr("id","poor")
    .attr("font-size", "15px");

//draw dots
svg.selectAll(".dot")
    .data(data)
  .enter().append("circle")
    .attr("class", "dot")
    .attr("r", 16)
    .attr("cx", xMap)
    .attr("cy", yMap)
    //.style("fill", 'rgb(31, 119, 180)')
    .style("opacity", 0.9) //function(d){ return color(cValue(d));})
    .on("mouseover", tip.show)
    .on("mouseout", tip.hide)
    ;
    /*  .on("mouseover", function(d){
      tooltip.transition()
          .duration(200)
          .style("opacity", 0.9);
      tooltip.html(d["location"] + "<br/> (" + xValue(d)
      + ", " + yValue(d) + ")")
            .style("left", (d3.event.pageX + 10) + "px")
            .style("top", (d3.event.pageY - 28) + "px"); */
   // });
svg.selectAll(".main")
    .data(data)
  .enter().append("text")
    .attr("class", "text")
    .attr("x", xMap)
    .attr("y", yMap)
    .attr("dx", -8)
    .attr("dy", 5)
    .attr("fill", "white")
    .text(function(d){ return d.abbreviation; })
    //.on("mouseover", tip.show)
    //.on("mouseout", tip.hide)
    //.attr("text-anchor", "start")
    ;
//adding event listeners that will change chart for each y axis selection
 d3.select("#veryGood")
      .on("click", function(){
          d3.select("#excellent").attr("font-weight", "normal");
          d3.select("#good").attr("font-weight", "normal");
          d3.select("#fair").attr("font-weight", "normal");
          d3.select("#poor").attr("font-weight", "normal");
          d3.select(this).attr("font-weight", "bold");
          //setup y axis
           var yValue = function(data){return data.veryGood;};
          yScale = d3.scale.linear().range([chartHeight, 0]),
          yMap = function(data){ return yScale(yValue(data));},
          yAxis = d3.svg.axis().scale(yScale).orient("left");
          yScale.domain([d3.min(data, yValue)-5, d3.max(data, yValue)+5]);
          console.log(yValue);   

          svg.selectAll("circle")
              .data(data)
              .transition()
              .duration(1000)
              .each("start", function() {
                d3.select(this)
              })
              .delay(function(d,i){
                return i / data.length * 500;
              })
              .attr("r", 16)
              .attr("cx", xMap)
              .attr("cy", yMap)
              .each("end", function() {
                d3.select(this)
                  .transition()
                  .duration(500)
              })
              .style("fill", 'rgb(31, 119, 180)')
              .style("opacity", 0.9) //function(d){ return color(cValue(d));})
              //.on("mouseover", tip.show)
              //.on("mouseout", tip.hide)
                ;
              svg.selectAll(".text")
                .data(data)
                .transition()
                .duration(1000)
                .each("start", function() {
                  d3.select(this)
                })
                .delay(function(d,i){
                  return i / data.length * 500;
                })
                .attr("x", xMap)
                .attr("y", yMap)
                .attr("dx", -8)
                .attr("dy", 5)
                .attr("fill", "white")
                .each("end", function() {
                  d3.select(this)
                    .transition()
                    .duration(500)
                })
                .text(function(d){ return d.abbreviation; });

              svg.selectAll(".x axis")
                .transition()
                .duration(1000)
                .call(xAxis);
              
              svg.selectAll(".y axis")
                .transition()
                .duration(1000)
                .call(yAxis);
          

        });
  d3.select("#good")
      .on("click", function(){
          d3.select("#excellent").attr("font-weight", "normal");
          d3.select("#veryGood").attr("font-weight", "normal");
          d3.select("#fair").attr("font-weight", "normal");
          d3.select("#poor").attr("font-weight", "normal");
          d3.select(this).attr("font-weight", "bold");
          //setup y axis
           var yValue = function(data){return data.good;},
          yScale = d3.scale.linear().range([chartHeight, 0]),
          yMap = function(data){ return yScale(yValue(data));},
          yAxis = d3.svg.axis().scale(yScale).orient("left");
          yScale.domain([d3.min(data, yValue)-1, d3.max(data, yValue)+5]); 

          console.log(data);      
          svg.selectAll("circle")
              .data(data)
              .transition()
              .duration(1000)
              .each("start", function() {
                d3.select(this)
              })
              .delay(function(d,i){
                return i / data.length * 500;
              })
              .attr("r", 16)
              .attr("cx", xMap)
              .attr("cy", yMap)
              .each("end", function() {
                d3.select(this)
                  .transition()
                  .duration(500)
              })
              .style("fill", 'rgb(31, 119, 180)')
              .style("opacity", 0.9) //function(d){ return color(cValue(d));})
              //.on("mouseover", tip.show)
              //.on("mouseout", tip.hide)
                ;
              svg.selectAll(".text")
                .data(data)
                .transition()
                .duration(1000)
                .each("start", function() {
                  d3.select(this)
                })
                .delay(function(d,i){
                  return i / data.length * 500;
                })
                .attr("x", xMap)
                .attr("y", yMap)
                .attr("dx", -8)
                .attr("dy", 5)
                .attr("fill", "white")
                .each("end", function() {
                  d3.select(this)
                    .transition()
                    .duration(500)
                })
                .text(function(d){ return d.abbreviation; });

              svg.select("x axis")
                .transition()
                .duration(1000)
                .call(xAxis);
              
              svg.select(".tick")
                .transition()
                .duration(1000)
                .call(yAxis);
        });
    d3.select("#fair")
        .on("click", function(){
            d3.select("#excellent").attr("font-weight", "normal");
            d3.select("#veryGood").attr("font-weight", "normal");
            d3.select("#good").attr("font-weight", "normal");
            d3.select("#poor").attr("font-weight", "normal");
            d3.select(this).attr("font-weight", "bold");
            //setup y axis
             var yValue = function(data){return data.fair;},
            yScale = d3.scale.linear().range([chartHeight, 0]),
            yMap = function(data){ return yScale(yValue(data));},
            yAxis = d3.svg.axis().scale(yScale).orient("left");
            yScale.domain([d3.min(data, yValue)-1, d3.max(data, yValue)+5]); 
            console.log(data);      
            svg.selectAll("circle")
                .data(data)
                .transition()
                .duration(1000)
                .each("start", function() {
                  d3.select(this)
                })
                .delay(function(d,i){
                  return i / data.length * 500;
                })
                .attr("r", 16)
                .attr("cx", xMap)
                .attr("cy", yMap)
                .each("end", function() {
                  d3.select(this)
                    .transition()
                    .duration(500)
                })
                .style("fill", 'rgb(31, 119, 180)')
                .style("opacity", 0.9) //function(d){ return color(cValue(d));})
                //.on("mouseover", tip.show)
                //.on("mouseout", tip.hide)
                  ;
                svg.selectAll(".text")
                  .data(data)
                  .transition()
                  .duration(1000)
                  .each("start", function() {
                    d3.select(this)
                  })
                  .delay(function(d,i){
                    return i / data.length * 500;
                  })
                  .attr("x", xMap)
                  .attr("y", yMap)
                  .attr("dx", -8)
                  .attr("dy", 5)
                  .attr("fill", "white")
                  .each("end", function() {
                    d3.select(this)
                      .transition()
                      .duration(500)
                  })
                  .text(function(d){ return d.abbreviation; });
  
                svg.select("x axis")
                  .transition()
                  .duration(1000)
                  .call(xAxis);
                
                svg.select("y axis")
                  .transition()
                  .duration(1000)
                  .call(yAxis);
          });
    d3.select("#poor")
        .on("click", function(){
            d3.select("#excellent").attr("font-weight", "normal");
            d3.select("#veryGood").attr("font-weight", "normal");
            d3.select("#good").attr("font-weight", "normal");
            d3.select("#fair").attr("font-weight", "normal");
            d3.select(this).attr("font-weight", "bold");
            //setup y axis
             var yValue = function(data){return data.poor;},
            yScale = d3.scale.linear().range([chartHeight, 0]),
            yMap = function(data){ return yScale(yValue(data));},
            yAxis = d3.svg.axis().scale(yScale).orient("left");
            yScale.domain([d3.min(data, yValue)-1, d3.max(data, yValue)+5]);
            console.log(data);       
            svg.selectAll("circle")
                .data(data)
                .transition()
                .duration(1000)
                .each("start", function() {
                  d3.select(this)
                })
                .delay(function(d,i){
                  return i / data.length * 500;
                })
                .attr("r", 16)
                .attr("cx", xMap)
                .attr("cy", yMap)
                .each("end", function() {
                  d3.select(this)
                    .transition()
                    .duration(500)
                })
                .style("fill", 'rgb(31, 119, 180)')
                .style("opacity", 0.9) //function(d){ return color(cValue(d));})
                //.on("mouseover", tip.show)
                //.on("mouseout", tip.hide)
                  ;
                svg.selectAll(".text")
                  .data(data)
                  .transition()
                  .duration(1000)
                  .each("start", function() {
                    d3.select(this)
                  })
                  .delay(function(d,i){
                    return i / data.length * 500;
                  })
                  .attr("x", xMap)
                  .attr("y", yMap)
                  .attr("dx", -8)
                  .attr("dy", 5)
                  .attr("fill", "white")
                  .each("end", function() {
                    d3.select(this)
                      .transition()
                      .duration(500)
                  })
                  .text(function(d){ return d.abbreviation; });
  
                svg.select("x axis")
                  .transition()
                  .duration(1000)
                  .call(xAxis);
                
                svg.select("y axis")
                  .transition()
                  .duration(1000)
                  .call(yAxis);
          });
      d3.select("#excellent")
          .on("click", function(){
              d3.select("#veryGood").attr("font-weight", "normal");
              d3.select("#good").attr("font-weight", "normal");
              d3.select("#fair").attr("font-weight", "normal");
              d3.select("#poor").attr("font-weight", "normal");
              d3.select(this).attr("font-weight", "bold");
              //setup y axis
              var yValue = function(data){return data.excellent;},
              yScale = d3.scale.linear().range([chartHeight, 0]),
              yMap = function(data){ return yScale(yValue(data));},
              yAxis = d3.svg.axis().scale(yScale).orient("left");
              yScale.domain([d3.min(data, yValue)-1, d3.max(data, yValue)+5]);
              console.log(data);      
              svg.selectAll("circle")
                  .data(data)
                  .transition()
                  .duration(1000)
                  .each("start", function() {
                    d3.select(this)
                  })
                  .delay(function(d,i){
                    return i / data.length * 500;
                  })
                  .attr("r", 16)
                  .attr("cx", xMap)
                  .attr("cy", yMap)
                  .each("end", function() {
                    d3.select(this)
                      .transition()
                      .duration(500)
                  })
                  .style("fill", 'rgb(31, 119, 180)')
                  .style("opacity", 0.9) //function(d){ return color(cValue(d));})
                  //.on("mouseover", tip.show)
                  //.on("mouseout", tip.hide)
                    ;
                  svg.selectAll(".text")
                    .data(data)
                    .transition()
                    .duration(1000)
                    .each("start", function() {
                      d3.select(this)
                    })
                    .delay(function(d,i){
                      return i / data.length * 500;
                    })
                    .attr("x", xMap)
                    .attr("y", yMap)
                    .attr("dx", -8)
                    .attr("dy", 5)
                    .attr("fill", "white")
                    .each("end", function() {
                      d3.select(this)
                        .transition()
                        .duration(500)
                    })
                    .text(function(d){ return d.abbreviation; });
    
                  svg.select("x axis")
                    .transition()
                    .duration(1000)
                    .call(xAxis);
                  
                  svg.select("y axis")
                    .transition()
                    .duration(1000)
                    .call(yAxis);
            });
  });
   // @TODO
  // Create code to build the bar chart using the tvData.
