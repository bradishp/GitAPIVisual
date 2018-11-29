//Code based off code from https://www.tutorialspoint.com/d3js/d3js_graphs.htm

queue()
    .defer(d3.json, "/generate/info")
    .defer(d3.json, "/other/generate/info")
    .defer(d3.json, "/username")
    .await(makeGraph);

function makeGraph(error, otherData, data, username) {
    var svg = d3.select("svg"),
    width = svg.attr("width"),
    height = svg.attr("height"),
    radius = Math.min(width, height) / 2;
    
    var g = svg.append("g")
        .attr("transform", "translate(" + width / 2 + "," + (height / 2 + 20)   + ")");
    
    var color = d3.scaleOrdinal([
        'orange', 'gray', 'pink', 'green', 'cyan', 'brown', 'yellow', 'red', 'violet', 'purple', 'blue'
    ]);
    
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
        .append("text").text("Breakdown of languages in " + String(username) + "'s other section.")
        .attr("class", "title")
}
