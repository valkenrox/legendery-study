
const fs = require('fs');

const data = 'Caroline Alvarenga Maia,14306052788,2330.00\n';

fs.writeFile('file.csv', data, (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
});
