// DoC U MenT DoT ReaD Y
$(document).ready(function() {

    $('#twitch-channel-form').on('submit', function(event){
        event.preventDefault();
        if ($('#twitch-channel-btn').hasClass('disabled')) { return; }
        var formData = new FormData($(this)[0]);
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: formData,
            beforeSend: function( jqXHR ){
                $('#twitch-channel-btn').addClass('disabled');
                $('#twitch-channel').attr('disabled', true);
                $('#search-icon').addClass('fa-spin');
                $('#search-status').addClass('progress-bar-striped progress-bar-animated');
            },
            complete: function(){
                $('#twitch-channel-btn').removeClass('disabled');
                $('#twitch-channel').attr('disabled', false);
                $('#search-icon').removeClass('fa-spin');
                $('#search-status').removeClass('progress-bar-striped progress-bar-animated');
            },
            success: function(data, textStatus, jqXHR){
                console.log("Status: "+textStatus+", Data: "+data.toString());
                console.log(jqXHR.status);
                console.log(data.success);
                console.log(data.channel);
            },
            error: function(data, textStatus) {
                console.log("Status: "+textStatus+", Data: "+data.responseText);
                console.log(data.status);
                console.log(data.responseJSON.success);
                console.log(data.responseJSON.channel);
            },
            cache: false,
            contentType: false,
            processData: false
        });
        return false;
    });

});
