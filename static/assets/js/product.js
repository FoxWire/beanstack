$(function(){
    $('#modal-message').hide();
    $('#review-modal').hide();

    // If the boolean flag exists on page load, scroll to the reviews section
    if (displayReviews){
        document.getElementById('reviews').scrollIntoView({behavior: "smooth"});
    }

    // If the user has already posted, show the modal
    if(hasPosted){
        $('#review-modal').modal('toggle');
    }
});

/*
    This code is from stack overflow
    In order to have the map adapt to the screen as the screen size changes
    we reload the screen when ever the browser window size is changed, however
    we don't want to do this when using a touch screen device as this causes
    the page to constantly reload
*/

if (!('ontouchstart' in document)){
    $(window).bind('resize', function(e){
        if (window.RT) clearTimeout(window.RT);
        window.RT = setTimeout(function(){
            this.location.reload(false);
        }, 100);
    });
}

$('.review-button').click(function(event){
    document.getElementById('reviews').scrollIntoView({behavior: "smooth"});
});

$('#vendor-button').click(function(event){
    document.getElementById('vendor-heading').scrollIntoView({behavior: "smooth"});
});

$('#radar-button').click(function(event){
    document.getElementById('radar-heading').scrollIntoView({behavior: "smooth"});
});

$('#add-button').click(function(){
    $('#my-modal').modal('toggle');
});


// This is the event listener for the accordian effect in the add to beanstack modal
$('#modal-add, #arrow-glyph').click(function(){
    $('.collapse').collapse('hide');
    $('#class-to-add').addClass('panel-default').removeClass('panel-primary');
    $('#class-to-add').css("margin-bottom", "5px");
    $('#modal-message').show();
    $('#spacer').hide();
});

// Make the arrow and the add button both react when one is hovered over
$('#arrow-glyph, #modal-add').hover(function(){
    $('#arrow-glyph').css('color', '#3174AE');
    $('#modal-add').addClass('btn-primary');
}, function(){
    $('#arrow-glyph').css('color', '#DDDDDD');
    $('#modal-add').removeClass('btn-primary');
});

$('#arrow-glyph, #modal-add').click(function(){
    //Ajax call to add the coffee to the user's saved coffees
    $.get('update-my-beanstack', {bean_slug: beanSlug }, function(){
        // do nothing on callback
    });

});

// This is called from the maps.js script
function activate_modal(marker){
    $('#vendor-detail-modal .modal-title').html(marker.name);
    $('#vendor-detail-modal .modal-body #description').html(marker.description);
    $('#vendor-detail-modal .modal-body #online-shop').html("<a target='_blank' href=" + marker.onlineshop + " >visit online shop</a>");
    $('#vendor-detail-modal .modal-body #address').html(marker.address);
    $('#vendor-detail-modal .modal-body #products').html("");
    for (i = 0; i < marker.products.length; i++){
        $('#vendor-detail-modal .modal-body #products').append("<li>"+ marker.products[i] + "</li>");
    }
    $('#vendor-detail-modal').modal('toggle');
}

// This function will listen to the tag buttons and update the hidden values for the form
// each time they are updated


$('.plus, .minus').click(function(){

    var item = $(this);
    var id = item.attr('data-tag')
    if ($('#' + id + '-label').attr('data-selected') == 'false'){
        // Get the name of tag that has been pushed
        var tag_id = $(this).attr('data-tag');

        //change the color of the label
        var label = $("#" + tag_id + "-label");
        label.css('color', 'white');
        label.css('border-color', 'white');
        label.attr('data-selected', 'true');

        // and the plus
        var item = $(this);
        item.css('color', 'white');
        item.css('border-color', 'white');

        // place the appropriate value in the form
        var itemType = $(this).attr('id');
        var value;
        if (itemType.includes('plus')){
            value = '+';
        } else if (itemType.includes('minus')){
            value = '-';
        }
        $("#" + tag_id).attr('value', value);
     }
});


$('.minus, .plus').hover(function(){
    var item = $(this);
    //Rollover disabled if tag is already selected
    var id = item.attr('data-tag')
    if ($('#' + id + '-label').attr('data-selected') == 'false'){
        item.css('color', 'white');
        item.css('border-color', 'white');
    }
}, function(){
    // only do the mouse leave if the button is not selected
    var tag_id = $(this).attr('data-tag');
    if ($('#' + tag_id + "-label").attr('data-selected') == 'false'){
        var item = $(this);
        item.css('color', '#209FAA');
        item.css('border-color', '#209FAA');
    }
});

// You can also click on the label to deselect your selection
$('.tag-label').click(function(){
    // is is selected?
    if ($(this).attr('data-selected') == 'true'){
      var tag = $(this);
      tag.css('color', '#209FAA');
      tag.css('border-color', '#209FAA');

      // reset the color of the plus and minus too
       var id = tag.attr('data-tag')

       var plus = $('#' + id + '-plus');
       plus.css('color', '#209FAA');
       plus.css('border-color', '#209FAA');

       console.log(plus.css('border-color'));

       var minus = $('#' + id + '-minus');
       minus.css('color', '#209FAA');
       minus.css('border-color', '#209FAA');


       $(this).attr('data-selected', 'false');

       // make sure that no value is recorded for the tag
       $("#" + id).attr('value', 'None');
    }
});
