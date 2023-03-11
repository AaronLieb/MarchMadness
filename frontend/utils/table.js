// start rendering loading bar
let scoreboard_loading_text = document.getElementById("scoreboard-loading-text")
let scoreboard_loading_bar = document.getElementById("scoreboard-loading-bar")

let loading_interval = setInterval(() => {
  scoreboard_loading_bar.value += 1
  if (scoreboard_loading_bar.value >= 100) {
    clearInterval(loading_interval);
  }
}, 10)


const jsonTableToDOM = (data) => {
  let container = $("#table-container");
  let table = $("<table>");
  let thead = $("<thead>");

  data = JSON.parse(data)

  let headers = Object.keys(data[0]);
  let tr = $("<tr>");

  let events = [];

  $.each(headers, (idx, item) => {
    if (idx == 0) {
      item = "";
    }
    let th = $("<th>");
    console.log(idx, item)
    th.text(item);
    console.log(th);
    tr.append(th);
  })
  thead.append(tr);
  table.append(tr);

  data.forEach((item) => {
    let tr = $("<tr>");
    let event = item['-'];
    let scores = Object.values(item);
    scores.forEach((s) => {
      let td = $("<td>");
      td.text(s);
      tr.append(td);

    });
    table.append(tr);
  });

  container.append(table);
  // h1.delay(1000).fadeIn(1000);
}

fetch("https://api.jstitt.dev/acmmm/sheet/scoreboard").then(response => response.json()).then((data) => {
  console.log(data)
  // TODO: convert to table?!?!?!
  //
  jsonTableToDOM(data)
  $("#scoreboard-loading-bar").fadeOut(1200);
  $("#scoreboard-loading-text").fadeOut(1200)
});
