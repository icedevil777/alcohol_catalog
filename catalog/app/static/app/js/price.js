$(document).ready(function(){
    $('#output').val($('#range').val());
    $('#range').mousemove(function() {
        $('#output').val($('#range').val());
    });

    $('#output').change(function() {
        $('#range').val($('#output').val());
    });
})
