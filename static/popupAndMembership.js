// Check more insturction and explaination from this site: https://www.w3schools.com/howto/howto_css_modals.asp
let signInPopup = document.getElementById("signInPopup"); /*in index.html */
let registerPopup = document.getElementById("registerPopup"); /*in index.html */

// The variables below are to clear the text inside of the input field after the window colsed.
let clearNameBoxInput = document.getElementsByClassName("nameBox")[0];
let clearEmailBoxInputForSignIN =
  document.getElementsByClassName("emailBox")[0];
let clearEmailBoxInputForRegister =
  document.getElementsByClassName("emailBox")[1];
let clearPasswordBoxInputForSignIN =
  document.getElementsByClassName("passwordBox")[0];
let clearPasswordBoxInputForRegister =
  document.getElementsByClassName("passwordBox")[1];

// in index.html
function btnPushItems_2() {
  signInPopup.style.display = "block";
}
function clearValue() {
  clearEmailBoxInputForSignIN.value = "";
  clearEmailBoxInputForRegister.value = "";
  clearPasswordBoxInputForSignIN.value = "";
  clearPasswordBoxInputForRegister.value = "";
  clearNameBoxInput.value = "";
}

window.onclick = function (event) {
  if (event.target == signInPopup || event.target == registerPopup) {
    event.target.style.display = "none";
    clearValue();
    let existErrorMsgTag = document.getElementsByClassName("errorMsg")[0];
    if (existErrorMsgTag) {
      existErrorMsgTag.remove();
    }
  }
};

/*in signIn.html */
function register() {
  registerPopup.style.display = "block";
  signInPopup.style.display = "none";
  clearValue();
  let existErrorMsgTag = document.getElementsByClassName("errorMsg")[0];
  if (existErrorMsgTag) {
    existErrorMsgTag.remove();
  }
}
function closeIconSignIn() {
  signInPopup.style.display = "none";
  clearValue();
  let existErrorMsgTag = document.getElementsByClassName("errorMsg")[0];
  if (existErrorMsgTag) {
    existErrorMsgTag.remove();
  }
}

/*in register.html */
function signIn() {
  registerPopup.style.display = "none";
  signInPopup.style.display = "block";
  clearValue();
  let existErrorMsgTag = document.getElementsByClassName("errorMsg")[0];
  if (existErrorMsgTag) {
    existErrorMsgTag.remove();
  }
  let existInformMsgTag = document.getElementsByClassName("successMsg")[0];
  if (existInformMsgTag) {
    existInformMsgTag.remove();
  }
}
function closeIconRegister() {
  registerPopup.style.display = "none";
  clearValue();
  let existInformMsgTag = document.getElementsByClassName("successMsg")[0];
  if (existInformMsgTag) {
    existInformMsgTag.remove();
  }
}

function validateEmail(email) {
  if (/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/.test(email)) {
    return true;
  } else {
    return false;
  }
}

function createInformMsgTag(tagName, tagClassName, messages) {
  let bottomPopupBoxParentNode = document.getElementById(tagName).parentNode;
  let bottomPopupBox = document.getElementById(tagName);
  let existErrorMsgTag = document.getElementsByClassName("errorMsg")[0];
  let existInformMsgTag = document.getElementsByClassName("successMsg")[0];
  if (existErrorMsgTag) {
    existErrorMsgTag.remove();
  }
  if (existInformMsgTag) {
    existInformMsgTag.remove();
  }
  let errorMsg = document.createElement("div");
  errorMsg.className = tagClassName;

  let errorMsgTag = document.createElement("p");
  errorMsg.appendChild(errorMsgTag);

  bottomPopupBoxParentNode.insertBefore(errorMsg, bottomPopupBox);
  errorMsgTag.innerHTML = messages.join("<br>");
}

function createNavLogInTag() {
  let navBtnHeader = document.getElementsByClassName("push")[0];
  let logInAndRegisterButton = document.getElementById("pushItems_2");
  logInAndRegisterButton.remove();

  let logOutButton = document.createElement("button");
  logOutButton.id = "pushItemsLogOut";
  logOutButton.className = "pushItemsLogOut";
  logOutButton.onclick = function () {
    deleteUserStatus();
  };
  let logOutTag = document.createElement("p");
  logOutTag.id = "logOut";

  logOutButton.appendChild(logOutTag);
  navBtnHeader.appendChild(logOutButton);
  logOutTag.innerHTML = "登出系統";
}

signInToSystem = document.getElementById("signInToSystem");
signInToSystem.addEventListener("click", (outcome) => {
  let messages = [];
  sigInEmailBox = document.getElementById("sigInEmailBox").value;

  sigInPasswordBox = document.getElementById("sigInPasswordBox").value;

  if (validateEmail(sigInEmailBox) === false) {
    messages.push("信箱格式不正確");
  }
  if (sigInPasswordBox === "" || sigInPasswordBox == null) {
    messages.push("密碼不得為空");
  }
  if (messages.length > 0) {
    outcome.preventDefault();
    tagClassName = "errorMsg";
    createInformMsgTag("bottomPopupBoxForSingIn", tagClassName, messages);
  } else {
    logInToSystem();
  }
});

function logInToSystem() {
  url = "http://192.168.0.223:3000/api/user";
  // url = "http://52.63.14.114:3000/api/user";
  singInInput = document.getElementById("sigInEmailBox").value;
  sigInPasswordBox = document.getElementById("sigInPasswordBox").value;

  fetch(url, {
    method: "PATCH",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: singInInput,
      password: sigInPasswordBox,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if (String(Object.keys(data)) === "ok") {
        createNavLogInTag();
        // checkUserStatus(); //This method is to send a request again instead of refreah page.
        location.reload();

        signInPopup.style.display = "none";
        clearValue();
      } else {
        messages = [data["message"]];
        tagClassName = "errorMsg";
        createInformMsgTag("bottomPopupBoxForSingIn", tagClassName, messages);
      }
    })
    .catch((error) => {
      console.log(
        error,
        "Something went wrong when fetching data via API, Check JS function : give the function name here"
      );
    });
}

// =============================
registerNewMeber = document.getElementById("registerNewMeber");
registerNewMeber.addEventListener("click", (outcome) => {
  let messages = [];
  registerName = document.getElementById("registerNameBox").value;
  registerEmail = document.getElementById("registerEmailBox").value;
  registerPassword = document.getElementById("registerPasswordBox").value;

  if (registerName === "" || registerName == null) {
    messages.push("姓名不得為空");
  }
  if (validateEmail(registerEmail) === false) {
    messages.push("信箱格式不正確");
  }
  if (registerPassword.length <= 6) {
    messages.push("密碼至少需 6 個字元");
  }
  if (messages.length > 0) {
    outcome.preventDefault();
    tagClassName = "errorMsg";
    createInformMsgTag("bottomPopupBoxForRegister", tagClassName, messages);
  } else {
    registerToSystem();
  }
});
// =============================
function registerToSystem() {
  url = "http://192.168.0.223:3000/api/user";
  // url = "http://52.63.14.114:3000/api/user";

  fetch(url, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: registerName,
      email: registerEmail,
      password: registerPassword,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if (String(Object.keys(data)) === "ok") {
        console.log("成功");
        messages = ["註冊成功"];
        tagClassName = "successMsg";
        createInformMsgTag("bottomPopupBoxForRegister", tagClassName, messages);
      } else {
        messages = [data["message"]];
        tagClassName = "errorMsg";
        createInformMsgTag("bottomPopupBoxForRegister", tagClassName, messages);
        console.log(data["message"]);
      }
    });
}

function checkUserStatus() {
  url = "http://192.168.0.223:3000/api/user";
  // url = "http://52.63.14.114:3000/api/user";
  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if (String(data) !== "null") {
        createNavLogInTag();
      }
    })
    .catch((error) => {
      console.log(
        error,
        "Something went wrong when fetching data via API, Check JS function : give the function name here"
      );
    });
}

function deleteUserStatus(singInInput, sigInPasswordBox) {
  url = "http://192.168.0.223:3000/api/user";
  // url = "http://52.63.14.114:3000/api/user";
  fetch(url, {
    method: "DELETE",
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if (String(Object.keys(data)) === "ok") {
        let navBtnHeader = document.getElementsByClassName("push")[0];
        let btnPushItemsLogOut = document.getElementById("pushItemsLogOut");
        btnPushItemsLogOut.remove();

        let logInAndRegisterButton = document.createElement("button");
        logInAndRegisterButton.id = "pushItems_2";
        logInAndRegisterButton.className = "pushItems_2";
        logInAndRegisterButton.onclick = function () {
          btnPushItems_2();
        };

        let logInTag = document.createElement("p");
        logInTag.id = "logInAndRegister";

        logInAndRegisterButton.appendChild(logInTag);
        navBtnHeader.appendChild(logInAndRegisterButton);
        logInTag.innerHTML = "登入/註冊";

        // checkUserStatus(); //This method is to send a request again instead of refreah page.
        location.reload();
        signInPopup.style.display = "none";
        clearEmailBoxInputForSignIN.value = "";
        clearEmailBoxInputForRegister.value = "";
        clearPasswordBoxInputForSignIN.value = "";
        clearPasswordBoxInputForRegister.value = "";
        clearNameBoxInput.value = "";
      }
    })
    .catch((error) => {
      console.log(
        error,
        "Something went wrong when fetching data via API, Check JS function : give the function name here"
      );
    });
}

checkUserStatus();
