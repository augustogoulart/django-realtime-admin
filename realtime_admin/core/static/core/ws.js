const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
const ws = new WebSocket(
    ws_scheme
    + '://'
    + window.location.host
    + '/ws/list/'
);
ws.onmessage = function (e) {
    return
};

ws.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};
