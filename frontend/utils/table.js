// start rendering loading bar
let scoreboard_loading_text = document.getElementById("scoreboard-loading-text")
let scoreboard_loading_bar = document.getElementById("scoreboard-loading-bar")


const jsonTableToMatrix = (raw) => {
  let matrix = {};

  $.each(raw, (idx, obj) => {
    let keys = Object.keys(obj);
    keys.forEach((k) => {
      if (matrix[k] === undefined)
        matrix[k] = [obj[k]];
      else
        matrix[k].push(obj[k]);
    })
  });

  $.each(matrix, (key, team) => {
    if (key == '-') return;
    let sum = team.reduce((a, b) => a + b, 0);
    team.push(sum);
  });

  matrix['-'].push("Total")

  return matrix;
}


const jsonTableToDOM = (raw) => {
  let container = $("#table-container").hide()
  let table = $("#leaderboard");
  let thead = $("<thead>");

  data = jsonTableToMatrix(JSON.parse(raw));

  let tr = $("<tr>");
  let th = $("<th>")
  tr.append(th); // append empty cell

  $.each(data['-'], (_, event_name) => {
    let th = $("<th>"); // create header cell
    th.text(event_name); // change header text
    tr.append(th); // add to row
  });

  thead.append(tr); // add row to header
  table.append(tr); // add row to table

  let teams = Object.keys(data).slice(1,);
  teams.sort(function(a, b) {
    return data[b].slice(-1) - data[a].slice(-1);
  });

  $.each(teams, (_, team) => {
    // row to hold team
    // first append name
    let name = $("<td>").text(team);
    let tr = $("<tr>").append(name);
    // add all scores from row
    $.each(data[team], (_, score) => {
      score = $("<td>").text(score);
      tr.append(score);
    });

    table.append(tr);
  });

  container.append(table);
  container.fadeIn(750).animate({ top: "-=10vh" }, 750);
  if (teams.length > 9) {
    container.css({ "overflow-y": "scroll" })
  }
}

fetch("https://api.jstitt.dev/acmmm/sheet/scoreboard").then(response => response.json()).then((data) => {
  // data = JSON.parse(data);
  // console.log(jsonTableToMatrix(data));
  jsonTableToDOM(data);
  $("#progress-2").animate({ opacity: 0 }, 500).addClass("loaded")
  $("#scoreboard-loading-text").animate({ opacity: 0 }, 100);
});
