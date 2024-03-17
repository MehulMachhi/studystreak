options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',},
  body: JSON.stringify({
    username: 'Avani02',
    password: 'Avani02*',
  }),
}
fetch('http://localhost:8000/api/login/', options)
.then(response => response.json())
.then(data => {
  console.log(data);
  localStorage.setItem('access', data.token.access);
})


socket = new WebSocket("ws://localhost:8888");
socket.onopen = function () {
  console.log("Connected");
  socket.send(
    localStorage.getItem('access')
  );
};
socket.onmessage = function (e) {
  console.log(e.data);
};

socket.onclose = function () {
  console.log("Disconnected");
};
