const express = require("express");
const app = express();
const { exec } = require("child_process");

app.use(
  express.urlencoded({
    extended: true
  })
)

app.use(express.json())

app.get("/", async (req, res)  => {
  res.send("Manda una petición post a /post");
});

app.post("/post", async (req, res) => {
  const url = req.body.url;
  if(!url) {
    res.send("Necesitas mandar una url");
  }
  try {
    exec(`python main.py ${url}`);
    res.send("D2 Activado")
  } catch (error) {
    res.send("Error ejecutando el programa");
  }
});

app.listen(5000, async () => {
  console.log("Mande una petición a /post");
});
