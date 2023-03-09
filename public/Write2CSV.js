//Import moduels 'fs' and 'csv-stringify'
const fs = require("fs");
const { stringify } = require("csv-stringify");
const { resolve } = require("path");

let counter = 0;

function store(data){

    return new Promise((resolve,reject) =>{

    //Time Stamp
    var now = new Date()
    var now_Date = now.getFullYear() + "-" + now.getMonth() + "-" + now.getDate()
    var now_Stamp = now.getHours()+":"+now.getMinutes()+":"+now.getSeconds()+":"+now.getMilliseconds()
    now_Stamp = now_Date + " " + now_Stamp

    //Data Desconstruction
    const test = data.split('"')
 
    var id = test[3]
   
 
    var x = test[6].replace(':','')
    x = x.replace(',','')
 
    var y = test[8].replace(':','')
    y = y.replace(',','')
 
    var z = test[10].replace(':','')
    z = z.replace(',','')
 
    var accX = test[16].replace(':','')
    accX = accX.replace(',','')
 
    var accY = test[18].replace(':','')
    accY = accY.replace(',','')
 
    var accZ = test[20].replace(':','')
    accZ = accZ.replace(',','')
 
    var gyroX = test[22].replace(':','')
    gyroX = gyroX.replace(',','')
 
    var gyroY = test[24].replace(':','')
    gyroY = gyroY.replace(',','')
 
    var gyroZ = test[26].replace(':','')
    gyroZ = gyroZ.replace(',','')
 
  
    //Data of one instance
    const dataList = [now_Stamp, id, x, y, z, accX, accY, accZ, gyroX, gyroY, gyroZ]
 
   
    //Titles for csv setup
    const titles = [
      "Time Stamp",
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
  
    const filename = "test1.csv";
    var stringifier = null;
    var writableStream = null;

    if(counter == 0){
      //First Time
      //Create csv
      
      writableStream = fs.createWriteStream(filename);
      stringifier = stringify({
        header: true,
        columns: titles,
      });

    }
    else{
      writableStream = fs.createWriteStream(filename,{flags:'a'});

      stringifier = stringify({
        header: false,
        columns: titles,
      });

    }

    
  
    stringifier.write(dataList);
    stringifier.pipe(writableStream);
 
    console.log("Original Data: " + data)
    console.log("Data Stored")

    counter += 1

    })
    //JSON object descontruct
    //var { id , x, y, z, accX, accY, accZ, gyroX, gyroY, gyroZ } = {"id": "","x":0,"y":0,"z":0,"w":0,"batt":0,"accX":0,"accY":0,"accZ":0,"gyroX":0,"gyroY":0,"gyroZ":0,"magX":0,"magY":0,"mag":0}
    //const { id = '', x, y, z, accX, accY, accZ, gyroX, gyroY, gyroZ } = data || {}
    //const [id , x, y, z, accX, accY, accZ, gyroX, gyroY, gyroZ ] = data || {}
 
    //id = data.id
 
 


  
 
    
 }

// const myPromise = new Promise((resolve,reject)=>{
//     if (store(data) == "Work"){
//         resolve()
//     }
//     else{
//         reject()
//     }
// })

exports.store = store

// myPromise.then(()=> console.log("Working"))
//             .catch(()=> console.log("Wrong"))



