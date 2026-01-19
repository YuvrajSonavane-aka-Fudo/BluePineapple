const express = require("express");
const fs = require("fs");
const csv = require("csv-parser");
const multer = require("multer");
const http = require("http");
const { Server } = require("socket.io");
const path = require("path");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.json());
app.use(express.static(path.join(__dirname, "../frontend")));

const CSV_FILE = path.join(__dirname, "data.csv");
const upload = multer({ dest: "uploads/" });

// Helper function to read CSV into an array
const readCSV = () => {
  return new Promise((resolve, reject) => {
    const results = [];
    if (!fs.existsSync(CSV_FILE)) return resolve([]);
    fs.createReadStream(CSV_FILE)
      .pipe(csv())
      .on("data", (data) => results.push(data))
      .on("end", () => resolve(results))
      .on("error", (err) => reject(err));
  });
};

// Helper function to write array back to CSV
const writeCSV = (data) => {
  const header = "id,name,role\n";
  const rows = data.map(emp => `${emp.id},${emp.name},${emp.role}`).join("\n");
  fs.writeFileSync(CSV_FILE, header + rows);
};

app.get("/employees", async (req, res) => {
  try {
    const data = await readCSV();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: "Read error" });
  }
});

// --- NEW: BULK DELETE ---
app.post("/employees/bulk-delete", async (req, res) => {
  const { ids } = req.body; // Array of IDs to delete
  try {
    let data = await readCSV();
    // Filter out the employees whose IDs are in the delete list
    const filteredData = data.filter(emp => !ids.includes(emp.id));
    writeCSV(filteredData);
    res.json({ success: true, count: ids.length });
  } catch (err) {
    res.status(500).json({ error: "Bulk delete failed" });
  }
});

// --- NEW: BULK UPDATE ---
app.post("/employees/bulk-update", async (req, res) => {
  const { employees } = req.body; // Array of employee objects {id, name, role}
  try {
    let data = await readCSV();
    
    // Create a map for quick lookup
    const updateMap = new Map(employees.map(emp => [emp.id, emp]));

    // Update existing rows or keep them as is
    const updatedData = data.map(emp => {
      if (updateMap.has(emp.id)) {
        return updateMap.get(emp.id);
      }
      return emp;
    });

    writeCSV(updatedData);
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: "Bulk update failed" });
  }
});

app.post("/employees", (req, res) => {
  const { id, name, role } = req.body;
  const line = fs.existsSync(CSV_FILE) ? `\n${id},${name},${role}` : `id,name,role\n${id},${name},${role}`;
  fs.appendFileSync(CSV_FILE, line);
  res.json({ success: true });
});

// ... (Rest of your code: upload, download, and socket.io remain the same)
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
    fs.createReadStream(CSV_FILE).pipe(res);
  } catch (err) {
    res.status(500).json({ error: "Download error" });
  }
});

io.on("connection", socket => {
  setInterval(() => {
    const time = new Date().toLocaleString("en-AU", { timeZone: "Australia/Sydney" });
    socket.emit("time", time);
  }, 1000);
});

server.listen(3000, () => console.log("Server running at http://localhost:3000"));