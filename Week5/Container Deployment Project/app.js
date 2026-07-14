const express = require('express');
const app = express();
const port = 8080;

app.get('/', (req, res) => res.send('Hello from ECS Fargate!'));
app.get('/health', (req, res) => res.status(200).send('OK'));

app.listen(port, () => console.log(`App running on port ${port}`));
