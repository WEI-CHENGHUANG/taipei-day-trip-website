let nextPage = 0;
let isLoading = false;

function setNextPage(val) {
  nextPage = val;
}

// This function can be called flag. I use this funciton to detect if the queryAttractions function is fetching data or not.
// Check the comment inside of the queryAttractions function
function setLoading(signal) {
  isLoading = signal;
}

function showErrorMsg(userInput) {
  let p = document.createElement("p");
  p.className = "wrongMessage";
  p.innerHTML = userInput;
  
  let container = document.getElementById("container");
  container.appendChild(p);
  container.parentNode.replaceChild(p, container);
}

function onSearch() {
  let container = document.getElementById("container");
  if (container) {
    container.remove();
  }

  let wrongMessage = document.querySelector(".wrongMessage");
  if (wrongMessage) {
    wrongMessage.remove();
  }
  
  let div = document.createElement("div");
  div.className = "container";
  div.id = "container";

  let outerContainer = document.getElementById("outerContainer");
  outerContainer.appendChild(div);

  queryByPagination(0);
}

function queryByPagination(pageNumber) {
  // If isLoading is true, it means function is fetching the data via API. Even the scrolling function has been manipulated more than once.
  // This queryAttractions function cannot pass the if statement in scrolling function. (check window.addEventListener)
  setLoading(true);

  let url = `http://52.63.14.114:3000/api/attractions?page=${pageNumber}`;
  
  const keywordInput = document.getElementById("queryLocationName").value;
  if (keywordInput.trim() !== "") {
    url += `&keyword=${keywordInput}`;
  }

  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((response) => {
      setNextPage(response["nextPage"]);

      if (response.message) {
        showErrorMsg(
          `${response.message} or there are no results matching your query.`
        );
      } else {
        for (let i = 0; i < response["data"].length; i++) {
          let name = response["data"][i]["name"];
          let mrt = response["data"][i]["mrt"];
          let category = response["data"][i]["category"];
          let image = response["data"][i]["images"][0];
          createGrid(name, mrt, category, image);
        }
      }
      // This function is for testing purpose and also can know whether the data back or not.
      // setTimeout(function(){
      //     setLoading(false);
      // },5000)

      // If the data has been captured successfully by API, this means here should set up to false. Then, the system can excute the function again.
      setLoading(false);
    })
    .catch((error) => {
      console.log(error, "query failed");
    });
}

window.addEventListener("scroll", () => {
  const scrollable = document.documentElement.scrollHeight - window.innerHeight;
  const scrlled = window.scrollY;

  if (Math.ceil(scrlled) === scrollable && nextPage && !isLoading) {
    queryByPagination(nextPage);
  }
});

// execute query after the DOM is ready
window.onload = function() {
  queryByPagination(nextPage);
}

// 這底下不用看  因為這是為了create block用的
// change the title to => name, mrt, category. url => image
function createGrid(name, mrt, category, image) {
  let container = document.getElementsByClassName("container")[0];

  // Reference(如何添加 New Node): https://ithelp.ithome.com.tw/articles/10191867    => check in the middle of the article
  // 增加節點
  // First Layer
  let firstLayerDiv = document.createElement("div");
  firstLayerDiv.className = "square";
  // Second and Third Layer Topbox
  let secondLayerDivTopBox = document.createElement("div");
  secondLayerDivTopBox.className = "topBox";

  let thirdLayerImg = document.createElement("div");
  thirdLayerImg.className = "image";
  // Reference: https://www.w3schools.com/html/html_images_background.asp
  // Url 字符格式：https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Template_literals
  thirdLayerImg.style.backgroundImage = `url(${image})`;

  let thirdLayerPForName = document.createElement("p");
  textNodeForName = document.createTextNode(name);
  thirdLayerPForName.appendChild(textNodeForName);
  // Second and Third Layer bottomBox
  let secondLayerDivbottomBox = document.createElement("div");
  secondLayerDivbottomBox.className = "bottomBox";

  let thirdLayerPForMrt = document.createElement("p");
  textNodeForMrt = document.createTextNode(mrt);
  thirdLayerPForMrt.appendChild(textNodeForMrt);

  let thirdLayerPForCategory = document.createElement("p");
  textNodeForCategory = document.createTextNode(category);
  thirdLayerPForCategory.appendChild(textNodeForCategory);

  secondLayerDivTopBox.appendChild(thirdLayerImg);
  secondLayerDivTopBox.appendChild(thirdLayerPForName);
  secondLayerDivbottomBox.append(thirdLayerPForMrt);
  secondLayerDivbottomBox.append(thirdLayerPForCategory);
  firstLayerDiv.appendChild(secondLayerDivTopBox);
  firstLayerDiv.appendChild(secondLayerDivbottomBox);
  container.appendChild(firstLayerDiv);
}
