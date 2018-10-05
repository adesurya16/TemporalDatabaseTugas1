var $resulttable = $('.resulttable');

$("#resultbutton").click(function(){    
    // var $link = "/temporalaps/answer/" + document.getElementById('id').getAttribute('value');
    var $link = document.getElementById('link').getAttribute('value');
    $(".resulttable").show("slow", function(){
        console.log($link);
        $.ajax({
            type : 'GET',
            url : $link,
            success : function(results){
                toResultTable(results['data']);
                // var $key = Object.keys(results['data'][0])
                // console.log($key)
                // console.log(results['data']);
                //     $.each(results['data'], function(i, result){
                //       if (i == 0){
                //         $resulttable.apppend("<tbody>")  
                //       }

                //       $resulttable.apppend("<td>" + result +"</td>");
                //       if (i == results['data'].length - 1){
                //         $resulttable.apppend("</tbody>")
                //       }
                //     });
            }
        });
    });
});

function toResultTable(results){
    var key = Object.keys(results[0])
    // class table
    $resulttable.append("<table class='table table-striped'>")
    // header
    $resulttable.append("<thead><tr>");
    for (x in key){
        $resulttable.append("<th>" + key[x] + "</th>");
    }
    $resulttable.append("</tr></thead>");
    //body
    $resulttable.append("<tbody>");
    for (obji in results){
        $resulttable.append("<tr>");
        for (x in results[obji]){
            $resulttable.append("<td>" + results[obji][x] + "</td>");
        }   
        $resulttable.append("</tr>");
    }
    $resulttable.append("</tbody>");

    $resulttable.append("</table>");
    console.log($resulttable);
}