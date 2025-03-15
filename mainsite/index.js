const express = require("express");
const fs = require("fs");
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.post("/update", (req, res) => {
    const { content } = req.body;
    if (!content) return res.status(400).send("No content provided");

    fs.writeFileSync("index.html", content, "utf8");
    res.send("HTML updated");
});

app.listen(PORT, '0.0.0.0', () => console.log(`Server running on http://0.0.0.0:${PORT}`));
