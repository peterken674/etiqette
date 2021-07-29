$(document).ready(function(){
    $('#checkoutForm input').change(function(e){
        
        let newValue = $(this).val();
        let numSeats = parseInt(newValue);

        let cost = 300;

        let totalCost = numSeats*cost;

        $("#totalCost").text(totalCost)
        $("#totalSeats").text(numSeats)
        e.preventDefault()
    })

})