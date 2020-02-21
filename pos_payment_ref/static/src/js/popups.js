odoo.define('pos_payment_ref.popups', function (require) {
"use strict";

var PopupWidget = require('point_of_sale.popups');
var gui = require('point_of_sale.gui');

var PaymentInfoWidget = PopupWidget.extend({
    template: 'PaymentInfoWidget',
    show: function(options){
        options = options || {};
        this._super(options);
        this.renderElement();
        if(options.data){
            var data = options.data;
            this.$('input[name=payment_ref]').val(data.payment_ref);
        }

        $('input[name=payment_ref]').on('keydown',function(event){

            var $me = $(this);
            var pos  = event.target.selectionStart;
            var val  = $me.val();
            var charCode = event.which || event.keyCode;
            var charStr = String.fromCharCode(charCode);
            if (event.keyCode === 46) { // Delete
                $me.val(val.slice(0,pos) + val.slice(pos+1,val.length));
                console.log(val.slice(0,pos) + val.slice(pos+1,val.length));
                event.target.setSelectionRange(pos,pos);
            } else if (event.keyCode === 8) { // Backspace
                $me.val(val.slice(0,pos-1) + val.slice(pos,val.length));
                event.target.setSelectionRange(pos-1,pos-1);
            }
            if (!/\w/.test(charStr)) {
                return;
            }
            $me.val( val + charStr);

        });

    },
    click_confirm: function(){
        var infos = {
            'payment_ref' : this.$('input[name=payment_ref]').val(),
        };
        var valid = true;
        if(this.options.validate_info){
            valid = this.options.validate_info.call(this, infos);
        }

        this.gui.close_popup();
        if( this.options.confirm ){
            this.options.confirm.call(this, infos);
        }
    },
});
gui.define_popup({name:'payment-info-input', widget: PaymentInfoWidget});

return PopupWidget;
});