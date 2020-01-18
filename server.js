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
  // let result = await client.query("Select * from users;")
  // console.log('====================================');
  // console.log(result);
  // console.log('====================================');

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
                            <input name="email" type="email" />
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
  console.log("====================================");
  console.log(req.body.email);
  console.log("====================================");

  try {
    let query = "Insert into users(email, name) values ('" + req.body.email + "' , '" + req.body.name + "');";
    console.log("====================================");
    console.log(query);
    console.log("====================================");
    let result = await client.query({
      text: query,
      rawMode: "array"
    });
    console.log("====================================");
    console.log(result);
    console.log("====================================");
    res.status(200).send(result);
  } catch (err) {
    console.log("====================================");
    console.log(err);
    console.log("====================================");
    res.status(400).send(err);
  }
});

app.get("/getuser", async (req, res) => {
  let query = "Select * from users where id = " + req.query.id;
  console.log("====================================");
  console.log(query);
  console.log("====================================");
  try {
    let response = await client.query(query);
    console.log(response);

    res.status(200).json(response);
  } catch (err) {
    res.status(404).send("Not found");
  }
});

app.listen(port, () => {
  console.log("====================================");
  console.log("Server started");
  console.log("====================================");
});
