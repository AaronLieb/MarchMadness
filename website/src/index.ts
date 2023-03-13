import cookieParser from 'cookie-parser';
import * as dotenv from 'dotenv';
import express from 'express';
import http from 'http';
import path from 'path';

dotenv.config()

const app = express();

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(cookieParser())

app.get('/inputs/:day/:part', async (req, res) => {
  console.log(req.cookies)
  if (!req.cookies.team) res.status(400).send('Missing team name');
  const url = `https://api.jstitt.dev/acmmm/sheet/get_index?team_name=${req.query.team_name}`;
  const index = (await fetch(url).then(res => res.json())).index;
  const file = `/../inputs/${req.params.day}/${req.params.part}/${index}.in`;
  res.sendFile(path.join(__dirname + file));
});

app.use(express.static('public', { extensions: ['html'] }));

const httpServer = http.createServer(app);
httpServer.listen(process.env.PORT, () => console.log(`Server is running on ${process.env.PORT}`));
