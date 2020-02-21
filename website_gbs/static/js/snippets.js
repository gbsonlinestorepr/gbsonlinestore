odoo.define('snippet_shop_categories_options', function(require) {
    'use strict';
    var options = require('web_editor.snippets.options');
    options.registry.snippet_shop_categories_options = options.Class.extend({

        onFocus: function() {

            // alert("okok")
            console.log(this.$target);

        },

    });
});