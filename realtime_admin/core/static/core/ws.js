(function ($) {
    const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    const ws = new WebSocket(
        ws_scheme
        + '://'
        + window.location.host
        + '/ws/list/'
    );
    ws.onmessage = function (e) {
        const data = JSON.parse(e.data)

        let newRow =
            `<tr class="row2">
               <td class="action-checkbox">
                 <input type="checkbox" name="_selected_action" value="1" class="action-select">
               </td>
               <th class="field-product">
                 <a href="/admin/core/order/1/change/">${data.product}</a>
               </th>
               <td class="field-client">${data.client}</td>
               <td class="field-value">${data.value}</td>
            </tr>`

        $("#result_list tbody").prepend(newRow)
    };

    ws.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };
})(django.jQuery);
