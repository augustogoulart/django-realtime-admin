const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
const ws = new WebSocket(
    ws_scheme
    + '://'
    + window.location.host
    + '/ws/list/'
);
ws.onmessage = function (e) {
    const elem = document.querySelector('#result_list');
    elem.style.display = 'none';
};

ws.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};
