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
    var _t = core._t;

    $(document).on("click","#checkout_button",function(){
            var self = this;
            var div = $("#order_total").children().children().children().text();
            var a = $("#temp-value").text();
            var domain = []
            if (parseFloat(div) < parseFloat(a)){
                    console.log("************")
                   // $( "#gbs_para").remove();
                    $( "#gbs_para").css("display","inline");
//                    var warning = _t("Warning! Minimum Purchase price should be more than ")
//                    $( "#checkout_button").after("<p  class='pull-right mb32 mr8' ><h5 id='gbs_para' ><strong style='font-size:18px'>" + warning + a +"</strong></h5></p>");
            }
            else{
            console.log("==========zeee==",)
            $( "#gbs_para").css("display","none");
             window.location.pathname = "/shop/checkout/";
            }
//            rpc.query({
//                model: 'ir.config_parameter',
//                method: 'get_param',
//                args:['shop_purchase_limit']
//            }).then(function(result){
//                console.log("=======result======",result)
//                if (result){
//                    if (div <  result ){
//                          $( "#gbs_para").remove();
//                          var warning = _t("Warning! Minimum Purchase price should be more than ")
//                          console.log("warnicevdfvvvvvvng",_t(warning))
//                          $( "#checkout_button").after(_t("<p  class='pull-right mb32 mr8' ><h5 id='gbs_para' ><strong style='font-size:18px'>" + warning + result +"</strong></h5></p>"));
//
//                          }
//
//                    else{
//                         $( "#gbs_para").css("display","none");
//                         window.location.pathname = "/shop/checkout/";
//                      }
//
//                }
//            });


            });
   });
