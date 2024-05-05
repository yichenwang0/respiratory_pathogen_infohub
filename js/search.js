// This function enables autocomplete functionality for the search box
function doAutocomplete() {
    $('#search_item').autocomplete({
        source: function(request, response) {
            // Hide and clear previous results
            $('#results').hide();
            $('tbody').empty();

            $.ajax({
                // Send the user input to the server side script 'search_suggestion.cgi' as the parameter
                url: './search_suggestion.cgi',
                dataType: 'json',
                data: { search_term: request.term },
                success: function(data, textStatus, jqXHR) {
                    // Populate the autocomplete suggestions
                    response(data.suggestions);
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    alert("Failed to perform autocompletion! textStatus: (" + textStatus + 
                          ") and errorThrown: (" + errorThrown + ")");
                }
            });
        },
        // Two characters are required before a search is performed
        minLength: 2,
    });
}


// this function executes our search via an AJAX call
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#gene_search').serialize();
    
    $.ajax({
        url: './search_product.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}


// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count );
    
    // this will be used to keep track of row identifiers
    var next_row_num = 1;
    
    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
    
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');
        
        // add the locus column
        $('<td/>', { "text" : item.locus_id } ).appendTo('#' + this_row_id);
        
        // add the product column
        $('<td/>', { "text" : item.product } ).appendTo('#' + this_row_id);

    });
    
    // now show the result section that was previously hidden
    $('#results').show();
}



// run our javascript once the page is ready
$(document).ready( function() {

    // Enable autocomplete functionality for the search box
    $('#search_item').on('input', function() {
        doAutocomplete();
    });

    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;  // prevents 'normal' form submission
    });
});

