/*Add the JavaScript here for the function billingFunction().  It is responsible for setting and clearing the fields in Billing Information */

function billingFunction() {

    checkbox = document.getElementById('same');
    billingName = document.getElementById('billingName');
    billingZip = document.getElementById('billingZip');
    shippingName = document.getElementById('shippingName');
    shippingZip = document.getElementById('shippingZip');
  
    if (checkbox.checked == true) {
      billingName.value = shippingName.value;
      billingZip.value = shippingZip.value;
      
    } else {
      billingName.value = '';
      billingZip.value = '';
      
    }
}
