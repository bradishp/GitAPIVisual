//Code based off code from https://www.tutorialspoint.com/d3js/d3js_graphs.htm and https://www.tutorialspoint.com/d3js/d3js_working_example.htm

var color = d3.scaleOrdinal([
    'orange', 'gray', 'pink', 'green', 'cyan', 'brown', 'yellow', 'red', 'violet', 'purple', 'blue', 'lime', 'oliveDrab', 'crimson', 'silver', 'teal', 'tan'
]);

function makePieChart(data, title) {
    var svg = d3.select("svg"),
    width = svg.attr("width"),
    height = svg.attr("height"),
    radius = Math.min(width, height) / 2;
    
    var g = svg.append("g")
        .attr("transform", "translate(" + width / 2 + "," + (height / 2 + 20)   + ")");
    
    var pie = d3.pie().value(function(d) { 
        return d.linesOfCode; 
    });
    
    var path = d3.arc()
        .outerRadius(radius - 10).innerRadius(0);
    
    var label = d3.arc()
        .outerRadius(radius).innerRadius(radius - 150);

    var arc = g.selectAll(".arc")
        .data(pie(data))
        .enter()
        .append("g")
        .attr("class", "arc");

    arc.append("path")
        .attr("d", path)
        .attr("fill", function (d) { return color(d.data.language); });

    arc.append("text").attr("transform", function (d) {
        return "translate(" + label.centroid(d) + ")";
    })

    .text(function(d) { return d.data.language; });
    
    svg.append("g")
        .attr("transform", "translate(" + 50 + "," + 20 + ")")
        .append("text").text(title)
        .attr("class", "title")
}


function makeBarChart(data, title, yValueName) {
    var svg = d3.select("svg"),
        margin = 120, 
        width = svg.attr("width") - margin,
        height = svg.attr("height") - margin;

    svg.append("text")
        .attr("transform", "translate(100,0)")
        .attr("x", -75).attr("y", 50)
        .attr("class", "title")
        .text(title)

    var x = d3.scaleBand().range([0, width]).padding(0.4),
        y = d3.scaleLinear().range([height, 0]);

    var g = svg.append("g")
        .attr("transform", "translate(" + 100 + "," + 100 + ")");


    x.domain(data.map(function (d) { return d.language; }));
    y.domain([0, d3.max(data, function (d) { return d.values; })]);

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))

    g.append("g")
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "-5.1em")
        .attr("text-anchor", "end")
        .attr("class", "sideline")
        .text(String(yValueName));

    g.append("g")
        .attr("transform", "translate(0, 0)")
        .call(d3.axisLeft(y))

    g.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", function (d) { return x(d.language); })
        .attr("y", function (d) { return y(d.values); })
        .attr("fill", function (d) { return color(d.language); })
        .attr("width", x.bandwidth()).transition()
        .ease(d3.easeLinear).duration(200)
        .delay(function (d, i) {
            return i * 25;
        })
        .attr("height", function (d) { return height - y(d.values); });
}
