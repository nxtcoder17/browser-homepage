
/* Configuring Button Clicks on the Items Row */
/* ++++++++++++++++++++++++++++++++++++++++++ */

$(document).ready (function () {
    $('.items').click (function () {
        var id = this.id;
        console.log (id);
        /* Removing any already being displayed box */
        $('.items').each (function () {
            if (this.id != id)
                $("#_" + this.id).hide();
        });

        $("#_" + this.id).fadeToggle("fast");
        /* console.log ("Inside it"); */
    });
});

var dict = {
    'google': 'https://www.google.com/search?q=QUERY',
    'duckduckgo': 'https://www.duckduckgo.com/q=QUERY',
    'google_images': 'https://www.google.com/search?tbm=isch&q=QUERY'
};

function search_query () 
{
    var engine = document.getElementById ('search_engine').value;
    var query = document.getElementById ('query').value;
    if ( ! (query.startsWith ('\"') || query.startsWith ("'"))) {
        query = query.trim();
        query = query.replace(/\s+/g, '+')
    }
    console.log  ("Your Query: " + query);
    var search_url = dict[engine].replace ("QUERY", query);
    console.log ("Search URL: " + search_url);

    window.open (search_url, "_self");
}
