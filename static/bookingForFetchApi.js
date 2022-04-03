// 1. check the user log-in status.
// 這個是為了當使用者直接type URL to booking page
// 或是當使用者以登入 並再點選 預定行程按鈕準備前往booking page時 會在頁面再次做檢查
function checkunconfirmOrder() {
  // url = "http://127.0.0.1:3000//api/booking";
  url = "http://52.63.14.114:3000/api/booking";

  fetch(url)
    .then((response) => {
      if (response.status === 403) {
        return response.status;
      } else { return response.json(); }

    })
    .then((data) => {
      if (data === 403) {
        console.log("I am in step one")
        // 尚未登入

        // // get the exist tag first
        mainBodyFromBookingPage = document.getElementById("forInsertingPurpose")
        newFooter = document.getElementById("forNewFooter")

        // // Now, creating a new page to reminder user they haven't logged in yet.
        let askLoginInfo = document.createElement("div");
        askLoginInfo.className = "newWholeMainBody";
        let askLoginInfoTag = document.createElement("p");
        askLoginInfoTag.className = "askLoginContent";
        askLoginInfo.appendChild(askLoginInfoTag)
        mainBodyFromBookingPage.appendChild(askLoginInfo)
        askLoginInfoTag.innerHTML = "Hi there, You have not logged in. " + "<br />" + "<br />" + "Please, click on the top right log-in button.";
        // The default CSS display has been setting as none, so I have to change it after creating this tag.
        askLoginInfo.style.display = "flex"
        // Old Footer
        footerBox = document.getElementsByClassName("footerBox")[0]
        footerBox.style.display = "none"
        // New Footer
        newFooterForAskLoginInfo = document.getElementsByClassName("newFooterForAskLoginInfo")[0]
        newFooterForAskLoginInfo.style.display = "flex"

      } else if (data === null) {
        console.log("I am in step two")
        // // 以登入 沒有預定資訊
        wholeMainBodyFromBookingPage = document.getElementsByClassName("wholeMainBody")[0]
        wholeMainBodyFromBookingPage.style.display = "flex"

        bookingWholeTopInfo = document.getElementsByClassName("bookingWholeTopInfo")[0]
        bookingWholeTopInfo.style.display = "none"
        bookingWholeMidInfo = document.getElementsByClassName("bookingWholeMidInfo")[0]
        bookingWholeMidInfo.style.display = "none"
        bookingWholeBottomInfo = document.getElementsByClassName("bookingWholeBottomInfo")[0]
        bookingWholeBottomInfo.style.display = "none"
        submitButtonForPayment = document.getElementsByClassName("submitButtonForPayment")[0]
        submitButtonForPayment.style.display = "none"

        firstSubTitle = document.getElementsByClassName("firstSubTitle")[0]
        let newFooterForBookingPage = document.createElement("p");
        newFooterForBookingPage.className = "remiderInfo"
        firstSubTitle.appendChild(newFooterForBookingPage)
        newFooterForBookingPage.innerHTML = "<br />" + "目前沒有任何待預訂的行程"

        // Old Footer
        footerBox = document.getElementsByClassName("footerBox")[0]
        footerBox.style.display = "none"
        // New Footer
        newFooterForAskLoginInfo = document.getElementsByClassName("newFooterForAskLoginInfo")[0]
        newFooterForAskLoginInfo.style.display = "flex"

      } else {
        // 有預定資訊 並顯示出來
        wholeMainBodyFromBookingPage = document.getElementsByClassName("wholeMainBody")[0]
        wholeMainBodyFromBookingPage.style.display = "flex"
        // the code below is to fill in the attraction info.
        // 台北一日遊content
        bookingDetailsTitle = document.getElementsByClassName("bookingDetailsTitle")[0]
        let bookingDetailDescription = document.createElement("label");
        bookingDetailDescription.className = "bookingDetailDescription";
        bookingDetailsTitle.appendChild(bookingDetailDescription)
        bookingDetailDescription.innerHTML = data["data"]["attraction"]["name"]
        // Picture bookingAttractionPic
        bookingAttractionPic = document.getElementsByClassName("bookingAttractionPic")[0]
        let bookingPicture = document.createElement("img");
        bookingPicture.src = data["data"]["attraction"]["image"][0]
        bookingAttractionPic.appendChild(bookingPicture)
        // Date
        bookingDate = document.getElementsByClassName("bookingDate")[0]
        let bookingDateTag = document.createElement("label");
        bookingDateTag.className = "two";
        bookingDate.appendChild(bookingDateTag)
        bookingDateTag.innerHTML = data["data"]["date"].substr(0, 17)
        // Time
        bookingTime = document.getElementsByClassName("bookingTime")[0]
        let bookingTimeTag = document.createElement("label");
        bookingTimeTag.className = "two";
        bookingTime.appendChild(bookingTimeTag)
        bookingTimeTag.innerHTML = data["data"]["time"]
        // Expense
        bookingExpenses = document.getElementsByClassName("bookingExpenses")[0]
        let bookingExpensesTag = document.createElement("label");
        bookingExpensesTag.className = "two";
        bookingExpenses.appendChild(bookingExpensesTag)
        let dollarUSLocale = Intl.NumberFormat('en-US');

        bookingExpensesTag.innerHTML = "新台幣 " + dollarUSLocale.format(data["data"]["price"])
        // Location
        bookingLocation = document.getElementsByClassName("bookingLocation")[0]
        let bookingLocationTag = document.createElement("label");
        bookingLocationTag.className = "two";
        bookingLocation.appendChild(bookingLocationTag)
        bookingLocationTag.innerHTML = data["data"]["attraction"]["address"]

        // The default of old Footer style is flex.
        // New Footer
        newFooterForAskLoginInfo = document.getElementsByClassName("newFooterForAskLoginInfo")[0]
        newFooterForAskLoginInfo.style.display = "none"
      }
    })
    .catch((error) => {
      console.log(
        error,
        "Something went wrong when fetching data via API, Check JS function :checkunconfirmOrder"
      );
    });
}
checkunconfirmOrder()


function deleteBookedAttraction() {
  // url = "http://127.0.0.1:3000//api/booking";
  url = "http://52.63.14.114:3000/api/booking";

  fetch(url, {
    method: "DELETE",
  })
    .then((response) => {
      return response.json();

    }).then((data) => {
      console.log(data)
      checkunconfirmOrder()
    })
}





