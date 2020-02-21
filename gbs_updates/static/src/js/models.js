odoo.define('gbs_updates.models', function (require) {
    "use strict";

    var models = require("point_of_sale.models");

    models.load_fields('product.product', ['gbs_average']);
});
