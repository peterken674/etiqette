$(document).ready(function(){
    $('#checkoutForm input').change(function(e){
        
        let newValue = $(this).val();
        let numSeats = parseInt(newValue);

        const cost = 500;

        let totalCost = numSeats*cost;

        $("#totalCost").text(totalCost)
        $("#totalSeats").text(numSeats)
        e.preventDefault()
    })

})