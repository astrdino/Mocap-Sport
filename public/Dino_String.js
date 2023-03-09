//const data = '{"id": "","x":0,"y":0,"z":0,"w":0,"batt":0,"accX":0,"accY":0,"accZ":0,"gyroX":0,"gyroY":0,"gyroZ":0,"magX":0,"magY":0,"mag":0}'
var data = '{"id": "08:3A:F2:66:60:30","x":-0.95,"y":-0.05,"z":0.01,"w":0.31,"batt":0.00,"accX":0.13,"accY":-5.68,"accZ":-7.62,"gyroX":0.01,"gyroY":0.00,"gyroZ":0.00,"magX":-13.19,"magY":-27.94,"mag":0.00}'

const test = data.split('"')

var date = new Date()

var dateTime = date.getHours()+":"+date.getMinutes()+":"+date.getSeconds()+":"+date.getMilliseconds()

console.log(dateTime)