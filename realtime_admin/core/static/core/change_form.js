(function ($) {
    $(document).ready(function () {
        const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
        const ws = new WebSocket(
            ws_scheme
            + '://'
            + window.location.host
            + '/ws/list/'
        );

        let product = ""
        let client = ""
        let value = ""

        $("#id_product").focusout(function () {
            product = this.value
        })

        $("#id_client").focusout(function () {
            client = this.value
        })

        $("#id_value").focusout(function () {
            value = this.value
        })

        $("#order_form").on("submit", function () {
            ws.send(JSON.stringify({
                'product': product,
                'client': client,
                'value': value
            }))
        })
    });
})(django.jQuery);
