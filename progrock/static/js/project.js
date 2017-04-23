window.onload = function() {
  var input = document.getElementById('job-name');
  var value = document.getElementById('prog-val');

  var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
  var ws_path = ws_scheme + '://' + window.location.host + '/prog/';

  var socket = new WebSocket(ws_path);

  socket.onmessage = onmessage;
  document.getElementById('go-button').onclick = onsubmit;

  function onmessage(msg) {
    var data = JSON.parse(msg.data);
    if (data.progress) {
      value.innerHTML = data.progress + '%';
    } else if (data.complete) {
      value.classList.add('complete');
    }
  }

  function onsubmit() {
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
}
