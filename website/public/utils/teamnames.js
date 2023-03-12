let former = ["The", "Blazing", "Sick", "Flaming", "Stupendous", "Courageous", "Scared", "Bendy"]
let latter = ["Bulldogs", "Flamingos", "Zebras", "Giraffes", "Pomeranians", "Yo-Yo's"]

export const getTeamName = () => {
  let r1 = Math.floor(Math.random() * former.length)
  let r2 = Math.floor(Math.random() * latter.length)
  return `${former[r1]} ${latter[r2]}`
}
