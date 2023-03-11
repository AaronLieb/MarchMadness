// start rendering loading bar
let scoreboard_loading_text = document.getElementById("scoreboard-loading-text")
let scoreboard_loading_bar = document.getElementById("scoreboard-loading-bar")


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
  container.fadeIn(750).animate({ top: "-=10vh" }, 750);
}

fetch("https://api.jstitt.dev/acmmm/sheet/scoreboard").then(response => response.json()).then((data) => {
  jsonTableToDOM(data);
  $("#progress-2").animate({ opacity: 0 }, 500).addClass("loaded")
  $("#scoreboard-loading-text").animate({ opacity: 0 }, 100);
});
