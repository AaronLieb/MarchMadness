let former = ["The", "Blazing", "Sick"]
let latter = ["Bulldogs", "Flamingos"]

export const getTeamName = () => {
  let r1 = Math.floor(Math.random() * former.length)
  let r2 = Math.floor(Math.random() * latter.length)
  return `${former[r1]} ${latter[r2]}`
}
