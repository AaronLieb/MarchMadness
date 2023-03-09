let base = "https://api.jstitt.dev/acmmm/sheet"

export const getToken = async () => {
  return (await fetch(`${base}/get_token`).then(response => response.json())).token
}
