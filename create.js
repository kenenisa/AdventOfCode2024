const fs = require('fs')
const https = require('https')


const day = Number(new Date().toString().split(' ')[2])

fs.writeFileSync(`day${day}.py`, `


# from collections import defaultdict

with open("./sample/day${day}.txt", "r") as f:

    result = 0
    for line in f:
        line = line.strip()
        a, b = list(map(int, line.split()))
    print(result)

`)

const cookie = fs.readFileSync('.cookie').toString().replace('\n', '')

const options = {
  hostname: 'adventofcode.com',
  path: `/2024/day/${day}/input`,
  method: 'GET',
  headers: {
    'Cookie': cookie
  }
};

const req = https.request(options, (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    fs.writeFileSync(`./sample/day${day}.txt`, data)
    console.log(`day${day} created :)`)
  });
});

req.on('error', (err) => {
  console.error('Error:', err.message);
});

req.end();
