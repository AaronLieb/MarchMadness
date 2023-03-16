import cookieParser from 'cookie-parser';
import * as dotenv from 'dotenv';
import express from 'express';
import http from 'http';
import path from 'path';

dotenv.config()

const app = express();

app.use(express.urlencoded({extended : false}));
app.use(express.json());
app.use(cookieParser())

app.get('/admin/panel/motivate/:id', async(req, res) => {

  if (req.params.id == "1") {
    res.send("'The only way to do great work is to love what you do.' - Steve Jobs")
    return
  }
  if (req.params.id == "2") {
    res.send("'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.' - Christian D. Larson")
    return
  }
  if (req.params.id == "3") {
    res.send("'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill")
    return
  }
  if (req.params.id == "4") {
    res.send("flag{3xc3pt_th1s_t1m3_pr3t3nd_th3_opp0s1t3_0f_wh4t_y0u_th1nk_1s_tru3_1s_tru3}")
    return
  }

  if (res.headerSent) return;
  res.status(400).send("Message does not exist")
})

app.get('/admin/panel/cookie_jar', async(req, res) => {
if (req.cookies.allowed_to_enter == true) {
    res.send("flag{Th3_l1ght_th4t_burn5_tw1c3_4s_br1ght_burns_h4lf_4s_l0ng}")
    return
  }
  if (res.headerSent) return;
  res.status(400).send("Cookie 'allowed_to_enter' was not correct")
})

app.post('/admin/button/', async(req, res) => {
if (req.body?.msg == "gimme da flag!") {
    res.redirect(301, '/admin/panel?flag=flag{G00d_m0rn1ng_V13tn4m}')
    return
  }
  if (res.headerSent) return;
  res.status(400).send("Wrong msg!")
})

app.post('/admin/', async (req, res) => {
  if (req.body?.user == "admin") {
    if (req.body?.password == "admin" || req.body?.password == "password") {
      res.redirect(301, '/admin/button?flag=flag{Y0u_c4nt_h4ndl3_th3_truth}')
      return
    } else {
      res.status(400).send("Wrong password! Our security is too secure :)")
      return
    }
  } else if (req.body?.user == "super_duper_admin_account") {
    if (req.body?.password == "Super_Duper_Wuper_Extra_Secure_Password!!") {
      res.send('flag{N3v3r_t3ll_m3_th3_0dd5_are_1n_my_f4v0r}')
      return
    } else {
      res.status(400).send("Wrong password! Our security is too secure :)")
      return
    }
  }
  if (res.headerSent) return;
  res.status(400).send("User does not exist!")
})

app.get('/inputs/:day/:part', async (req, res) => {
  if (!req.cookies.team)
    res.status(400).send('You must create a team!');
  const url = `https://api.jstitt.dev/acmmm/sheet/get_index?team_name=${
      req.cookies.team}`;
  const index = (await fetch(url).then(res => res.json())).index;
  const file = `/../inputs/${req.params.day}/${req.params.part}/${index}.in`;
  res.sendFile(path.join(__dirname + file));
});

app.use(express.static('public', {extensions : [ 'html' ]}));

const httpServer = http.createServer(app);
httpServer.listen(process.env.PORT, () => console.log(`Server is running on ${process.env.PORT}`));
