//Code based off code from https://www.tutorialspoint.com/d3js/d3js_graphs.htm

queue()
    .defer(d3.json, "/additional/generate/info")
    .defer(d3.json, "/username")
    .await(makeGraph);

function makeGraph(error, data, username) {
    var svg = d3.select("svg"),
        margin = 120, 
        width = svg.attr("width") - margin,
        height = svg.attr("height") - margin;

    svg.append("text")
        .attr("transform", "translate(100,0)")
        .attr("x", 50).attr("y", 50)
        .attr("font-size", "20px")
        .attr("class", "title")
        .text("Number of repositories the language appears in.")

    var x = d3.scaleBand().range([0, width]).padding(0.4),
        y = d3.scaleLinear().range([height, 0]);

    var color = d3.scaleOrdinal([
        'orange', 'gray', 'pink', 'green', 'cyan', 'brown', 'yellow', 'red', 'violet', 'purple', 'blue', 'lime', 'oliveDrab', 'crimson', 'silver', 'teal', 'tan'
    ]);

    var g = svg.append("g")
        .attr("transform", "translate(" + 100 + "," + 100 + ")");


    x.domain(data.map(function (d) { return d.language; }));
    y.domain([0, d3.max(data, function (d) { return d.numberOfRepos; })]);

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))

    g.append("g")
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "-5.1em")
        .attr("text-anchor", "end")
        .attr("font-size", "18px")
        .attr("stroke", "blue")
        .text("Number of repositories");

    g.append("g")
        .attr("transform", "translate(0, 0)")
        .call(d3.axisLeft(y))

    g.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", function (d) { return x(d.language); })
        .attr("y", function (d) { return y(d.numberOfRepos); })
        .attr("fill", function (d) { return color(d.language); })
        .attr("width", x.bandwidth()).transition()
        .ease(d3.easeLinear).duration(200)
        .delay(function (d, i) {
            return i * 25;
        })
        .attr("height", function (d) { return height - y(d.numberOfRepos); });
}
