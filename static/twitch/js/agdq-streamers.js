// DoC U MenT DoT ReaD Y
$(document).ready(function() {

    $('#agdq-streamers-form').on('submit', function(event){
        event.preventDefault();
        if ($('#agdq-streamers-btn').hasClass('disabled')) { return; }
        var formData = new FormData($(this)[0]);
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: formData,
            beforeSend: function( jqXHR ){
                $('#agdq-streamers-btn').addClass('disabled');
                $('#search-icon').addClass('fa-spin');
                $('#search-status').addClass('progress-bar-striped progress-bar-animated');
                $('#search-results').empty();
            },
            complete: function(){
                $('#agdq-streamers-btn').removeClass('disabled');
                $('#search-icon').removeClass('fa-spin');
                $('#search-status').removeClass('progress-bar-striped progress-bar-animated');
            },
            success: function(data, textStatus, jqXHR){
                console.log('Status: '+jqXHR.status+', Success: '+data.success);
                $('#search-results').append('<pre><code>'+data.results+'</code></pre>');
            },
            error: function(data, textStatus) {
                if (data.responseJSON) {
                    console.log(data.responseJSON.success);
                    console.log(data.responseJSON.results);
                    $('#search-results').append('<div class="alert alert-danger">' + data.responseJSON.results + '</div>' +
                        '<pre><code>' + data.responseText + '</code></pre>');
                }else{
                    $('#search-results').append('<div class="alert alert-danger">Unknown Error Occurred.</div>' +
                        '<pre><code>' + data.responseText + '</code></pre>');
                }
            },
            cache: false,
            contentType: false,
            processData: false
        });
        return false;
    });

});
