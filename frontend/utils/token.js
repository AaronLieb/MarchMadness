export const getToken = async () => {
  // TODO: validate team name input
  let team_name = document.getElementById('team-name-input').value;
  let token_box = document.getElementById('token-box');
  let submit_button = document.getElementById('submit-team');

  submit_button.setAttribute("aria-busy", "true");
  console.log('team_name: ', team_name)

  fetch(`https://api.jstitt.dev/acmmm/sheet/create_team?team_name=${team_name}`, {
    method: "POST",
  }).then(res => res.json())
    .then(json => {
      token_box.style.visibility = 'visible';
      token_box.dataset.content = json.token
      submit_button.setAttribute("aria-busy", "false");
    });
}
