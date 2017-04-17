window.onload = function() {
  var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
  var ws_path = ws_scheme + '://' + window.location.host + '/prog/';
  console.log("Connecting to " + ws_path);
  var socket = new WebSocket(ws_path);
  var input = document.getElementById('job-name');

  function onsubmit(e) {
    var name = input.value;
    console.log(name);
    if (!name) {
      return;
    }

    var msg = {
      action: 'start',
      name: name
    };

    socket.send(JSON.stringify(msg));

    input.value = '';
    input.focus();
  }

  document.getElementById('go-button').onclick = onsubmit;
}
