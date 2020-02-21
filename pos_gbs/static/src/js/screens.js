odoo.define('pos_gbs.screens', function (require) {
    "use strict";

    var core = require('web.core');
    var gui = require('point_of_sale.gui');
    var screens = require('point_of_sale.screens');


    var ProductPreferredWidget = screens.ProductListWidget.extend({
        template: 'ProductPreferredWidget',
    });

    function get_preferred_items(self,preferred_products_ids){
        var preferred_products = [];
        for(var a=0;a<preferred_products_ids.length;a++){
            if (self.pos.db.get_product_by_id(preferred_products_ids[a]) != null){
                preferred_products.push(self.pos.db.get_product_by_id(preferred_products_ids[a]));
            }
        }
        return preferred_products
    }

    screens.ProductScreenWidget.include({
        start: function () {
            var self = this;
            this._super();
            if (this.pos.get_order().attributes.client != null){
                this.PreferredItems = new ProductPreferredWidget(self, {
                    click_product_action: function (product) {
                        self.click_product(product);
                    },
                    product_list: get_preferred_items(this,this.pos.get_order().attributes.client.preferred_products)
                });
                this.PreferredItems.replace(this.$('.placeholder-PreferredItems'));
            }
        },
    });

    screens.ClientListScreenWidget.include({
        save_changes: function () {
            this._super();
            var self = this;
            if (this.has_client_changed() && this.new_client) {
                parent.PreferredItems = new ProductPreferredWidget(this, {
                    click_product_action: function (product) {
                        if (product.to_weight && self.pos.config.iface_electronic_scale) {
                            self.gui.show_screen('scale', {product: product});
                        } else {
                            self.pos.get_order().add_product(product);
                        }
                    },
                    product_list: get_preferred_items(this,this.pos.get_order().attributes.client.preferred_products)
                });
                if(parent.$('.placeholder-PreferredItems').length > 0){
                    parent.PreferredItems.replace(parent.$('.placeholder-PreferredItems'));
                }else if(parent.$('.preferred-list-container').length > 0){
                    parent.PreferredItems.replace(parent.$('.preferred-list-container'));
                }
            } else {
                parent.$('.item-list').remove();
            }
        },
    });

    return {
        ProductPreferredWidget: ProductPreferredWidget,
    }
});