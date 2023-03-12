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
  let token_hint = document.getElementById('token-hint')
  let submit_button = document.getElementById('submit-team');

  let team_name = team_name_input.value;

  let old_content = submit_button.innerText;
  let already_created = false;
  team_name_input.addEventListener("input", () => {
    if (!already_created) return;
    submit_button.setAttribute("class", "");
    console.log(submit_button.innerText)
    if (submit_button.innerText.search("Already") != -1) {
      submit_button.disabled = false;
    }
    submit_button.innerText = old_content;
  })

  submit_button.setAttribute("aria-busy", "true");

  fetch(`https://api.jstitt.dev/acmmm/sheet/create_team?team_name=${team_name}`, {
    method: "POST",
  }).then(res => {
    if (!res.ok) {
      submit_button.setAttribute("class", "secondary outline")
      already_created = true;
      submit_button.innerText = "Team Already Created.";
      submit_button.disabled = true;
      submit_button.setAttribute("aria-busy", "false");
    }
    return res.json()
  })
    .then(json => {
      token_box.style.visibility = 'visible';
      token_hint.style.visibility = 'visible';
      token_box.dataset.content = json.token
      submit_button.setAttribute("aria-busy", "false");
      submit_button.innerHTML = "<i>Team Created.</i>"
      submit_button.disabled = true;
    });
}
