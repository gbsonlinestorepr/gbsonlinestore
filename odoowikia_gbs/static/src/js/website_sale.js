odoo.define('odoowikia_gbs.website_sale', function (require) {
    "use strict";
        var base = require("web_editor.base");
    var ajax = require('web.ajax');
    var utils = require('web.utils');
    var translation = require('web.translation');
   var rpc = require('web.rpc');
    var core = require('web.core');
    var config = require('web.config');
    var session = require('web.session');

    require("website.content.zoomodoo");
    var _t = translation._t;

      $(document).on("click","#checkout_button",function(){
            var self = this;

            var div = $("#order_total").children().children().children().text();
                rpc.query({
                model: 'ir.config_parameter',
                method: 'get_param',
                args:['shop_purchase_limit']
            }).then(function(result){
                if (result){
                    if (Number(div) < Number(result) ){
                           $( "#gbs_para").remove();
                          var warning = _t("Aviso! La cantidad mínima de compra debe ser igual o mayor a ")
                          $( "#checkout_button").after("<p  class='pull-right mb32 mr8'><h5 id='gbs_para' ><strong>" + warning + result +"</strong></h5></p>");

                          }

                    else{
                         $( "#gbs_para").css("display","none");
                         window.location.pathname = "/shop/checkout/";
                      }

                }
            });


            });
   });
