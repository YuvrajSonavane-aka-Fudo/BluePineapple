const express = require("express");
const fs = require("fs");
const csv = require("csv-parser");
const multer = require("multer");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const path = require("path");
const server = http.createServer(app);
const io = new Server(server);

app.use(express.json());
app.use(express.static(path.join(__dirname, "../frontend")));

const CSV_FILE = path.join(__dirname, "data.csv");
const upload = multer({ dest: "uploads/" });

app.get("/employees", (req, res) => {
  const results = [];
  if (!fs.existsSync(CSV_FILE)) return res.json(results);
  fs.createReadStream(CSV_FILE)
    .on("error", err => {
      console.error("CSV read error:", err);
      return res.status(500).json({ error: "CSV read error", message: err.message });
    })
    .pipe(csv())
    .on("data", data => results.push(data))
    .on("end", () => {
      if (results.length > 0) {
        const keys = Object.keys(results[0]);
        if (keys.length && (/^_?0$/.test(keys[0]) || keys[0] === '0')) {
          const mapped = results.map(r => ({
            id: r._0 || r['0'] || "",
            name: r._1 || r['1'] || "",
            role: r._2 || r['2'] || ""
          }));
          if (mapped.length && /id/i.test(mapped[0].id) && /name/i.test(mapped[0].name)) mapped.shift();
          return res.json(mapped);
        }
      }
      return res.json(results);
    });
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
  try {
    const stat = fs.statSync(CSV_FILE);
    res.setHeader("Content-Disposition", "attachment; filename=data.csv");
    res.setHeader("Content-Length", stat.size);
    res.setHeader("Content-Type", "text/csv; charset=utf-8");
    const stream = fs.createReadStream(CSV_FILE);
    stream.on("error", err => {
      console.error("Download stream error:", err);
      if (!res.headersSent) res.status(500).end();
    });
    stream.pipe(res);
  } catch (err) {
    console.error("Download error:", err);
    return res.status(500).json({ error: "Download error", message: err.message });
  }
});

io.on("connection", socket => {
  setInterval(() => {
    const time = new Date().toLocaleString("en-AU", {
      timeZone: "Australia/Sydney"
    });
    socket.emit("time", time);
  }, 1000);
});

server.listen(3000, () =>
  console.log("Server running at http://localhost:3000")
);
