url = "http://192.168.0.226:3000/api/orders"
// url = "http://52.63.14.114:3000/api/booking"
let price = document.getElementsByClassName("bookingExpenses")[0].getElementsByClassName("two")[0].textContent.substring(4)
let subtitleName = document.getElementsByClassName("bookingDetailDescription")[0].textContent
let attractionId = document.getElementsByTagName("img")[0].alt;
let attractionImg = document.getElementsByTagName("img")[0].src;
let attractionAddress = document.getElementsByClassName("bookingLocation")[0].getElementsByClassName("two")[0].textContent;
let travelDate = document.getElementsByClassName("bookingDate")[0].getElementsByClassName("two")[0].textContent.substring(5);
let travelTime = document.getElementsByClassName("bookingTime")[0].getElementsByClassName("two")[0].textContent;
let contactName = document.getElementsByClassName('contactNameBox')[0].value;
let contactEmail = document.getElementsByClassName('bookingEmailBox')[0].value;
let contactPhone = document.getElementsByClassName('mobileBox')[0].value;

fetch(url, {
    method: "POST",
    headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        "prime": result.card.prime,
        "order": {
            "price": price,
            "trip": {
                "attraction": {
                    "id": attractionId,
                    "name": subtitleName,
                    "address": attractionAddress,
                    "image": attractionImg
                },
                "date": travelDate,
                "time": travelTime
            },
            "contact": {
                "name": contactName,
                "email": contactEmail,
                "phone": contactPhone
            }
        }
    }),
})
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('here')
        console.log(data)
    });



