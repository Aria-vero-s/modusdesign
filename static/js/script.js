// Wait for the DOM to finish loading before running the game
// Get the button elements and add event listeners to them

document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.getElementsByTagName("button");
    let branding2 = document.getElementById('branding2');
    let website2 = document.getElementById('website2');
    let illustration2 = document.getElementById('illustration2');
    let fullpackage2 = document.getElementById('fullpackage2');

    for (let button of buttons) {
        button.addEventListener("click", function() {
            if (this.getAttribute("service") === "branding") {
                branding2.style.display = "inline";
                website2.style.display = "none";
                illustration2.style.display = "none";
                fullpackage2.style.display = "none";
            }
            if (this.getAttribute("service") === "website") {
                branding2.style.display = "none";
                website2.style.display = "inline";
                illustration2.style.display = "none";
                fullpackage2.style.display = "none";
            }
            if (this.getAttribute("service") === "illustration") {
                branding2.style.display = "none";
                website2.style.display = "none";
                illustration2.style.display = "inline";
                fullpackage2.style.display = "none";
            }
            if (this.getAttribute("service") === "fullpackage") {
                branding2.style.display = "none";
                website2.style.display = "none";
                illustration2.style.display = "none";
                fullpackage2.style.display = "inline";
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.getElementsByTagName("button");
    let plan = document.getElementById('plan');
    let bronze = document.getElementById('bronze');
    let silver = document.getElementById('silver');
    let gold = document.getElementById('gold');

    for (let button of buttons) {
        button.addEventListener("click", function() {
            if (this.getAttribute("package") === "branding2") {
                plan.style.display = "inline";
                bronze.style.display = "inline";
                silver.style.display = "inline";
                gold.style.display = "inline";
            }
            if (this.getAttribute("package") === "website2") {
                plan.style.display = "inline";
                bronze.style.display = "inline";
                silver.style.display = "inline";
                gold.style.display = "inline";
            }
            if (this.getAttribute("package") === "illustration2") {
                plan.style.display = "inline";
                bronze.style.display = "inline";
                silver.style.display = "inline";
                gold.style.display = "inline";
            }
            if (this.getAttribute("package") === "fullpackage2") {
                plan.style.display = "inline";
                bronze.style.display = "inline";
                silver.style.display = "inline";
                gold.style.display = "inline";
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", function() {
    let inputs = document.getElementsByTagName("input");
    let quote = document.getElementById('quote');

    for (let input of inputs) {
        inputs.addEventListener("click", function() {
            if (this.getAttribute("plan") === "bronze") {
                quote.style.display = "inline";
            }
            if (this.getAttribute("plan") === "silver") {
                quote.style.display = "inline";
            }
            if (this.getAttribute("plan") === "gold") {
                quote.style.display = "inline";
            }
        });
    }
});

// Extract user's checked checkboxes 


function brandingCheckbox(event) {
    var logo = document.getElementById("logo");
    var promo = document.getElementById("promo");
    var stationary = document.getElementById("stationary");
    var packaging = document.getElementById("packaging");

    if (document.getElementById('logo').checked){
        alert("logo checked") ;
    } else {
        alert("logo unchecked")
    }
    if (document.getElementById('promo').checked){
        alert("promo checked") ;
    } else {
        alert("promo unchecked")
    }
    if (document.getElementById('stationary').checked){
        alert("stationary checked") ;
    } else {
        alert("stationary unchecked")
    }
    if (document.getElementById('packaging').checked){
        alert("packaging checked") ;
    } else {
        alert("packaging unchecked")
    }

};

/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});