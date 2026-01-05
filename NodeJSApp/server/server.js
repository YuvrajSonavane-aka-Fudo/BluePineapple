const express = require("express");
const fs = require("fs");
const csv = require("csv-parser");
const multer = require("multer");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.json());
app.use(express.static("../client"));

const CSV_FILE = "./employees.csv";
const upload = multer({ dest: "uploads/" });

app.get("/employees", (req, res) => {
  const results = [];
  fs.createReadStream(CSV_FILE)
    .pipe(csv())
    .on("data", data => results.push(data))
    .on("end", () => res.json(results));
});

app.post("/employees", (req, res) => {
  const { id, name, role } = req.body;
  fs.appendFileSync(CSV_FILE, `\n${id},${name},${role}`);
  res.json({ success: true });
});

app.post("/upload", upload.single("file"), (req, res) => {
  fs.renameSync(req.file.path, CSV_FILE);
  res.json({ success: true });
});

app.get("/download", (req, res) => {
  res.setHeader("Content-Disposition", "attachment; filename=employees.csv");
  fs.createReadStream(CSV_FILE).pipe(res);
});

io.on("connection", socket => {
  setInterval(() => {
    const time = new Date().toLocaleString("en-US", {
      timeZone: "Asia/Tokyo"
    });
    socket.emit("time", time);
  }, 1000);
});

server.listen(3000, () =>
  console.log("Server running at http://localhost:3000")
);
