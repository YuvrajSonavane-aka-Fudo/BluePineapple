const http = require("http");
const fs = require("fs");
const path = require("path");
const csv = require("csv-parser");
const multer = require("multer");
const { Server } = require("socket.io");
const url = require("url");

const CSV_FILE = path.join(__dirname, "data.csv");
const upload = multer({ dest: "uploads/" });

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const method = req.method;
  const pathname = parsedUrl.pathname;

  if (method === "GET" && pathname === "/") {
    fs.readFile("../frontend/index.html", (err, data) => {
      if (err) {
        res.writeHead(500);
        return res.end("Error");
      }
      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(data);
    });
    return;
  }

  if (method === "GET" && pathname === "/employees") {
    const results = [];
    if (!fs.existsSync(CSV_FILE)) {
      res.writeHead(200, { "Content-Type": "application/json" });
      return res.end(JSON.stringify(results));
    }

    fs.createReadStream(CSV_FILE)
      .pipe(csv())
      .on("data", d => results.push(d))
      .on("end", () => {
        let output = results;
        if (results.length) {
          const keys = Object.keys(results[0]);
          if (keys[0] === "0" || keys[0] === "_0") {
            output = results.map(r => ({
              id: r._0 || r["0"],
              name: r._1 || r["1"],
              role: r._2 || r["2"]
            }));
            if (/id/i.test(output[0].id)) output.shift();
          }
        }
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify(output));
      });
    return;
  }

  if (method === "POST" && pathname === "/employees") {
    let body = "";
    req.on("data", c => (body += c));
    req.on("end", () => {
      const { id, name, role } = JSON.parse(body);
      fs.appendFileSync(CSV_FILE, `\n${id},${name},${role}`);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ success: true }));
    });
    return;
  }

  if (method === "POST" && pathname === "/upload") {
    upload.single("file")(req, res, err => {
      if (err) {
        res.writeHead(500);
        return res.end("Upload error");
      }
      fs.renameSync(req.file.path, CSV_FILE);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ success: true }));
    });
    return;
  }

  if (method === "GET" && pathname === "/download") {
    try {
      const stat = fs.statSync(CSV_FILE);
      res.writeHead(200, {
        "Content-Disposition": "attachment; filename=data.csv",
        "Content-Length": stat.size,
        "Content-Type": "text/csv"
      });
      fs.createReadStream(CSV_FILE).pipe(res);
    } catch {
      res.writeHead(500);
      res.end("Download error");
    }
    return;
  }

  res.writeHead(404);
  res.end("Not found");
});

const io = new Server(server);

io.on("connection", socket => {
  setInterval(() => {
    socket.emit(
      "time",
      new Date().toLocaleString("en-AU", { timeZone: "Australia/Sydney" })
    );
  }, 1000);
});

server.listen(3000, () =>
  console.log("Server running at http://localhost:3000")
);
