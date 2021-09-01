import * as d3 from "d3";

const url =
  "https://raw.githubusercontent.com/GowthamKumar1626/cgenomicstool/main/backend/static/files/result-id-2021-08-12%2012%3A56%3A33.884409.csv";

export default class D3Chart {
  constructor(element) {
    const svg = d3
      .select(element)
      .append("svg")
      .attr("width", 1200)
      .attr("height", 700);

    d3.csv(url).then((csvData) => {
      const rects = svg.selectAll("rect").data(csvData);

      rects
        .enter()
        .append("rect")
        .attr("x", (d, i) => i * 35)
        .attr("y", 25)
        .attr("width", 25)
        .attr("height", 25)
        .attr("fill", "green");
    });
  }
}
