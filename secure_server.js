const { Client } = require("pg");
const express = require("express");

const app = express();
const port = 8000;

const client = new Client({
  database: "sql_injection",
  host: "localhost",
  port: 5432,
  user: "priosan",
  password: "123456789"
});

client.connect();

app.use(express.urlencoded());

app.get("/", async (req, res) => {
  let html = `
        <!DOCTYPE html>
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <form method="POST" action="/test"> 
                        <div>
                            <label>Email</label>
                            <input name="email" type="text" />
                        </div>
                        <div>
                            <label>Name</label>
                            <input name="name" type="text" />
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </body>
            </html>
    `;
  res.send(html);
});

app.post("/test", async (req, res) => {
  try {
    let query = "Select * from users where name iLike '%$1%' and email ilike '%$2%';";
    let values = [req.query.name, req.query.email];
    let result = await client.query(query, values);
    res.status(200).send(result);
  } catch (err) {
    res.status(400).send(err);
  }
});

app.get("/getuser", async (req, res) => {
  let query = "Select * from users where name iLike '%$1%'";
  try {
    let response = await client.query(query, [req.query.name]);
    res.status(200).json(response);
  } catch (err) {
    res.status(404).send("Not found");
  }
});

app.listen(port, () => {
  console.log("Server started");
});
