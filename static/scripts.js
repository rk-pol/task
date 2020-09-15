'use strict';

$(document).ready(function(){
   
         var temp = $('.errors-sigin');
         var count_err = temp.data('count_err');
         var old_height = temp.height();
         var new_height = count_err * old_height;
         temp.height(new_height)   
      });

