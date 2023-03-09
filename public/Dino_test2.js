//Import moduels 'fs' and 'csv-stringify'
const fs = require("fs");
const { stringify } = require("csv-stringify");

const hello = (check) => {


    return "hello "+check
}

const store = (data) => {
  //JSON object descontruct
  const { id, x, y, z, accX, accY, accZ, gyroX, gyroY, gyroZ } = data;

  //Data of one instance
  const dataList = null;
  dataList = [id, x, y, z, accX, accY, accZ, gyroX, gyroY, gyroZ]

  //Titles for csv setup
  const titles = [
    "ID",
    "X",
    "Y",
    "Z",
    "accX",
    "accY",
    "accZ",
    "gyroX",
    "gyroY",
    "gyroZ",
  ];

  //csv name
  const filename = "test1.csv";
  const writableStream = fs.createWriteStream(filename);

  const stringifier = stringify({
    header: true,
    columns: titles,
  });

  

  stringifier.write(dataList);
  stringifier.pipe(writableStream);

  return data.id;
}

exports.hello = hello;
exports.store = store;