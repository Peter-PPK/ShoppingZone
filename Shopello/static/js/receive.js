$(document).ready(function() {
    var i=0;
    $(".addReceiveRow").click(function() {
        ++i;
        var productName=$("#productName").find("option:selected").text();
        var productValue=$("#productName").val();
        var qty=$('#qty').val();
        var markup="<tr><td><input type='hidden' name='rows["+i+"][productName]' value="+productValue+">"+productName+"</td>"+"<tr><td><input type='hidden' name='rows["+i+"][qty]' value="+qty+">"+qty+"</td>"+"</td><td><button type='button' class='btn btn-danger remove-tr'><i class='fa fa-minus'></i></button></tr>";
        $("table tbody").append(markup);
        var table=document.getElementById("tableID"),sumVal=0;
        for (var j=1; j<table.rows.length; j++) {
            sumVal=sumVal+parseInt(table.rows[j].cells[4].querySelector('input').value);
        }
        document.getElementById('totalValue').value=sumVal;
    });
    $(document).on('click','.remove-tr',function() {
        $(this).parents('tr').remove();
    });
});