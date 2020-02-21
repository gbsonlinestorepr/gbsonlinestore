odoo.define('pos_gbs.models', function (require) {
    "use strict";

    var models = require("point_of_sale.models");

    models.load_fields('res.partner', ['preferred_products']);
});
