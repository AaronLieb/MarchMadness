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
  let th = $("<th>")
  tr.append(th);

  $.each(data, (idx, obj) => {
    let event_name = obj['-']
    let th = $("<th>");
    th.text(event_name);
    console.log(th);
    tr.append(th);
  });

  thead.append(tr);
  table.append(tr);

  $.each(data, (idx, row) => {
    let names = Object.keys(row).slice(1,);
    let scores = Object.values(row).slice(1,);
    let tr = $("<tr>");
    let td = $("<td>");
    td.text(names[idx]);;
    tr.append(td);
    for (let i = 0; i < names.length; ++i) {
      let td = $("<td>");
      td.text(scores[i]);
      tr.append(td)
    }

    table.append(tr);

  })

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
