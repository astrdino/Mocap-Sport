


//Import moduels 'fs' and 'csv-stringify'
const fs = require("fs");
const { stringify } = require("csv-stringify");

//Testing data
var data = {"id": "08:3A:F2:66:60:30","x":-0.95,"y":-0.05,"z":0.01,"w":0.31,"batt":0.00,"accX":0.13,"accY":-5.68,"accZ":-7.62,"gyroX":0.01,"gyroY":0.00,"gyroZ":0.00,"magX":-13.19,"magY":-27.94,"mag":0.00}


//JSON object descontruct
const{id,x,y,z,accX,accY,accZ,gyroX,gyroY,gyroZ} = data

//Data of one instance
const dataList = [id,x,y,z,accX,accY,accZ,gyroX,gyroY,gyroZ]

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
    "gyroZ"

];


//csv name
const filename = "test.csv";
const writableStream = fs.createWriteStream(filename)

const stringifier = stringify({
    header:true, columns: titles}
)

stringifier.write(dataList)
stringifier.pipe(writableStream)

     

