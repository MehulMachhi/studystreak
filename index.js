socket = new WebSocket("ws://localhost:8888");
socket.onopen = function () {
  console.log("Connected");
  socket.send(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwNzU5ODg0LCJpYXQiOjE3MTA2NzM0ODQsImp0aSI6IjZlYzk3ZDUyNzg1NDQxYmZiOTIyM2Q0NmM3YWMzMDBjIiwidXNlcl9pZCI6M30.tD8zDMNmEqWj2uZ3HzepcQ7-0HutE-LZUaSMmIdiReI"
  );
};
socket.onmessage = function (e) {
  console.log(e.data);
};

socket.onclose = function () {
  console.log("Disconnected");
};
