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
  let container = $("#table-container").hide();
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

  let tht = $("<th>").text("Total");
  tr.append(tht);

  thead.append(tr);
  table.append(tr);

  $.each(data, (idx, row) => {
    let names = Object.keys(row).slice(1,);
    let scores = Object.values(row).slice(1,);
    let tr = $("<tr>");
    let td = $("<td>");
    td.text(names[idx]);;
    tr.append(td);
    let total = 0;
    for (let i = 0; i < data.length; ++i) {
      let td = $("<td>");
      score = data[i][names[idx]];
      td.text(score);
      total += parseInt(score);
      tr.append(td);
    }
    let td2 = $("<td id='total'>").text(total);
    tr.append(td2);

    table.append(tr);
  })

  container.append(table);
  container.delay(300).fadeIn(1000);
}

fetch("https://api.jstitt.dev/acmmm/sheet/scoreboard").then(response => response.json()).then((data) => {
  console.log(data)
  jsonTableToDOM(data)
  $("#scoreboard-loading-bar").fadeOut(600);
  $("#scoreboard-loading-text").fadeOut(600)
});
