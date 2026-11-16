$(document).ready(function() {
    var i=0;
    $(".add-row").click(function() {
        ++i;
        var productName=$("#productName").find("option:selected").text();
        var productValue=$("#productName").val();
        var saleTypeName=$("#saleType").find("option:selected").text();
        var saleTypeValue=$("#saleType").val();
        var qty=$("#qty").val();
        var price=$("#price").val();
        var amount=$("#amount").val();
        var markup="<tr><td><input type='hidden' name='rows["+i+"][productName]' value="+productValue+">"+productName+"</td>"+"<td><input type='hidden' name='rows["+i+"][saleTypeName]' value="+saleTypeValue+">"+saleTypeName+"</td>"+"<tr><td><input type='hidden' name='rows["+i+"][qty]' value="+qty+">"+qty+"</td>"+"<tr><td><input type='hidden' name='rows["+i+"][price]' value="+price+">"+price+"</td>"+"<tr><td><input type='hidden' name='rows["+i+"][amount]' value="+amount+">"+amount+"</td><td><button type='button' class='btn btn-danger remove-tr'><i class='fa fa-minus'></i></button></tr>";
        $("table tbody").append(markup);
        var table=document.getElementById("tableID"),sumVal=0;
        for (var j=1;j<table.rows.length;j++){
            sumVal=sumVal+parseInt(table.rows[j].cells[4].querySelector('input').value);
        }
        document.getElementById('totalValue').value=sumVal;
    });
    $(document).on('click','.remove-tr',function() {
        $(this).parents('tr').remove();
    });
});
function calc1(obj) {
    var qty=document.getElementById('qty').value;
    var price=document.getElementById('price').value;
    document.getElementById('amount').value=qty*price;
}
function calc2(obj) {
    var totalValue=document.getElementById('totalValue').value;
    var discount=document.getElementById('discount').value;
    var balance1=parseInt(totalValue)-parseInt(discount);
    document.getElementById('balance').value=balance1;
    var tax=document.getElementById('tax').value;
    var balance2=parseInt(balance1)-parseInt(tax);
    document.getElementById('balance').value=balance2;
    var paid=document.getElementById('paid').value;
    document.getElementById('credit').value=balance2-paid;
}