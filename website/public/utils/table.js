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
    $.each(data[team], (_idx, score) => {
      // console.log(score, score > 1337, _)
      if (score > 1337 && _idx == 4) {
        console.log('here')
        score = $("<td>").text(score + '*').css({"background-color": "#efe4c1", "opacity": "0.8", "border-radius": "10%"})
      } else {
        score = $("<td>").text(score);
      }

      tr.append(score);
    });

    if (getCookie('team') && name[0].textContent == getCookie('team')) {
      name.css({ 'background-color': 'var(--primary)', 'color': 'var(--primary-inverse)' });
      setTimeout(() => {
        name[0].scrollIntoView({ behavior: 'smooth', block: 'end' });
      }, 750)
    }

    table.append(tr);
  });

  if (teams.length == 0) { // no teams registered
    console.log('here')
    let no_team_text = $("<h4>").text("No teams have registered. Check back later.").hide().delay(300).fadeIn(300);
    $("#main-container").append(no_team_text);

  }
  else {
    container.append(table);
    container.fadeIn(750).animate({ top: "-=10vh" }, 750);
  }
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
