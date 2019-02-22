(function($){
  $.fn.charsLeft = function(options){
    var defaults = {
      'source':'input',
      'dest':'.count',
    }
    var options = $.extend(defaults, options);

    var calculate = function(source, dest, maxlength, changeColor){
      var remaining = maxlength - source.val().length;
      dest.html(remaining);

      if (changeColor) {
        /* Over 50%, change colour to orange */
        p = (100 * remaining) / maxlength;
        if(p < 25){
          dest.addClass('orange');
        }else if(p < 50){
          dest.addClass('red');
        }else{
          dest.removeClass('orange red');
        }
      }
    };

    this.each(function(i, el) {
      var maxlength = $(this).find('.maxlength').html();
      var dest = $(this).find(options.dest);
      var source = $(this).find(options.source);
      var changeColor = source.attr('change_color') !== undefined;
      source.keyup(function(){
        calculate(source, dest, maxlength, changeColor)
      });
      source.change(function(){
        calculate(source, dest, maxlength, changeColor)
      });
    });
  };
  $(function() { // Added page ready wrapper
    $(".charsleft-input").charsLeft({
      'source':'input',
      'dest':".count",
    });
  });
})((typeof django !== 'undefined' && django.jQuery) || window.jQuery || jQuery);
