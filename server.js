

const express = require('express');
const app = express();
const server = require('http').Server(app);
const url = require('url');
const WebSocket = require('ws');



let counter = 0



const port = 3000;


const write2csv = require('./public/Write2CSV');
const { count } = require('console');







// const express_config= require('./config/express.js');

// express_config.init(app);

const wss1 = new WebSocket.Server({ noServer: true });
const wss2 = new WebSocket.Server({ noServer: true });


var cameraArray={};




//sensor nodes
wss1.on('connection', function connection(ws) {
 

  ws.on('message', function incoming(message) {
    var tmp = message.toString()  

    //Filter
    if(tmp != 'Connected'){

      write2csv.store(tmp)
      
    }

    
    if(counter < 2){
              

          if(counter == 1){
            //console.log(hello.store(tmp))
            //write2csv.store(tmp)
           
            //console.log(typeof(message))
          }
          
          counter +=1
    }
	  //console.log(message.toString());

    wss2.clients.forEach(function each(client) {
      if (client.readyState === WebSocket.OPEN) {


        client.send(message);
      }
    });
  });
});

//webbrowser
wss2.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
  	// nothing here should be received
    //console.log('received wss2: %s', message);
    console.log("Received from web browser");
  });
});

server.on('upgrade', function upgrade(request, socket, head) {
  const pathname = url.parse(request.url).pathname;


  
  if (pathname === '/hub') {
    wss1.handleUpgrade(request, socket, head, function done(ws) {
      wss1.emit('connection', ws, request);
    });
  } else if (pathname === '/web_client') {
    wss2.handleUpgrade(request, socket, head, function done(ws) {
      wss2.emit('connection', ws, request);
    });
  } else {
    socket.destroy();
  }
});

app.get("/", function (req, res) {
    res.redirect("index.html")
});

app.use(express.static(__dirname + '/public'));


server.listen(port, () => {
	  console.log(`App listening at http://localhost:${port}`)
})


