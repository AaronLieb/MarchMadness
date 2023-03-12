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

// app.get('/problems/:id', async (req, res) => {
//   if (req.cookies.pass && req.cookies.pass === process.env.PHISHING_PASSWORD) {
//     await query("INSERT INTO Clicks (userName, linkName) VALUES ('Aaron', ?);", [req.params.id])
//   }
//   res.sendFile(path.join(__dirname + '/../public/youJustGotPhished.html'));
// });

app.use(express.static('public', { extensions: ['html'] }));

const httpServer = http.createServer(app);
httpServer.listen(process.env.PORT, () => console.log(`Server is running on ${process.env.PORT}`));
