orderUrl = window.location.href;
// orderNumber = orderUrl.substr(42);
// 正式
orderNumber = attractionUrl.substr(41);

// let newURLForThankyou = `http://192.168.0.226:3000/api/order/${orderNumber}`
let newURLForThankyou = `http://52.63.14.114:3000/api/order/${orderNumber}`
function getorderInfo(newURLForThankyou) {
    fetch(newURLForThankyou)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            if (data["data"]["status"] === 1) {
                thankyousuccessIcon = document.getElementsByClassName("successIcon")[0]
                thankyousuccessIcon.style.display = "block";
                thankyoufailIncon = document.getElementsByClassName("failIncon")[0]
                thankyoufailIncon.style.display = "none";

                orderMsg = document.getElementsByClassName("orderMsg")[0]
                orderMsg.innerHTML = "行程預定成功"
                number1 = document.getElementsByClassName("number1")[0]
                number1.innerHTML = data["data"]["number"]
                number2 = document.getElementsByClassName("number2")[0]
                number2.innerHTML = data["data"]["price"]
                number3 = document.getElementsByClassName("number3")[0]
                number3.innerHTML = data["data"]["trip"]["attraction"]["name"]
                number4 = document.getElementsByClassName("number4")[0]
                number4.innerHTML = data["data"]["trip"]["attraction"]["address"]
                number5 = document.getElementsByClassName("number5")[0]
                number5.innerHTML = data["data"]["trip"]["date"]
                number6 = document.getElementsByClassName("number6")[0]
                number6.innerHTML = data["data"]["trip"]["time"]

                returnBtn = document.getElementsByClassName("returnBtn")[0]
                returnBtn.innerHTML = "返回首頁"
                returnBtn.onclick = function () {
                    returnToHP();
                };
            } else {
                thankyousuccessIcon = document.getElementsByClassName("successIcon")[0]
                thankyousuccessIcon.style.display = "none";
                thankyoufailIncon = document.getElementsByClassName("failIncon")[0]
                thankyoufailIncon.style.display = "block";

                orderMsg = document.getElementsByClassName("orderMsg")[0]
                orderMsg.innerHTML = "付款失敗"
                number1 = document.getElementsByClassName("number1")[0]
                number1.innerHTML = data["data"]["number"]
                number2 = document.getElementsByClassName("number2")[0]
                number2.innerHTML = data["data"]["price"]
                number3 = document.getElementsByClassName("number3")[0]
                number3.innerHTML = data["data"]["trip"]["attraction"]["name"]
                number4 = document.getElementsByClassName("number4")[0]
                number4.innerHTML = data["data"]["trip"]["attraction"]["address"]
                number5 = document.getElementsByClassName("number5")[0]
                number5.innerHTML = data["data"]["trip"]["date"]
                number6 = document.getElementsByClassName("number6")[0]
                number6.innerHTML = data["data"]["trip"]["time"]

                returnBtn = document.getElementsByClassName("returnBtn")[0]
                returnBtn.innerHTML = "返回預定行程頁"
                returnBtn.onclick = function () {
                    returnTobookingPage()
                };
            }
        });
}

function returnToHP() {
    location.replace("http://192.168.0.226:3000/")
}
function returnTobookingPage() {
    location.replace("http://192.168.0.226:3000/booking")
}

getorderInfo(newURLForThankyou)