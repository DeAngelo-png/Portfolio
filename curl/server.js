const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    const userAgent = req.get('User-Agent');

    if (userAgent && userAgent.includes('curl')) {
        // Respond to curl requests
        res.send('Hello, curl!');
    } else {
        // Respond to regular web browser requests
        res.send('<h1>Hello, Web Browser!</h1>');
    }
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
