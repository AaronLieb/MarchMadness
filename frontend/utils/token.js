export const getToken = async () => {
  // TODO: validate team name input
  //
  let team_name_input = document.getElementById('team-name-input');
  // check validity of input field against pattern [a-zA-Z\W]*
  if (!team_name_input.validity.valid) {
    console.log('Invalid Team Name: ');
    return;
  }

  let token_box = document.getElementById('token-box');
  let submit_button = document.getElementById('submit-team');

  let team_name = team_name_input.value;

  let old_content = submit_button.innerText;
  let already_created = false;
  team_name_input.addEventListener("input", () => {
    if (!already_created) return;
    submit_button.setAttribute("class", "");
    submit_button.innerText = old_content;
  })

  submit_button.setAttribute("aria-busy", "true");
  console.log('team_name: ', team_name)

  fetch(`https://api.jstitt.dev/acmmm/sheet/create_team?team_name=${team_name}`, {
    method: "POST",
  }).then(res => {
    if (!res.ok) {
      console.log("TEAM ALREADY CREATED");
      submit_button.setAttribute("class", "secondary outline")
      already_created = true;
      submit_button.innerText = "Team Already Created.";
      submit_button.setAttribute("aria-busy", "false");
    }
    return res.json()
  })
    .then(json => {
      token_box.style.visibility = 'visible';
      token_box.dataset.content = json.token
      submit_button.setAttribute("aria-busy", "false");
      submit_button.innerHTML = "<i>Team Created.</i>"
      submit_button.disabled = true;
    });
}
