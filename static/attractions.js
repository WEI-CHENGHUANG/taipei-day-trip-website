// Reference: https://www.youtube.com/watch?v=J254pngGt6E
let radioBtns = document.querySelectorAll("input[name='daySelect']");
let result = document.getElementById("result");

let findSelected = () => {
  const selected = document.querySelector(
    "input[name='daySelect']:checked"
  ).value;
  result.textContent = selected;
};

radioBtns.forEach((radioBtn) => {
  radioBtn.addEventListener("change", findSelected);
});
// ==============================================================
// Reference: https://www.youtube.com/watch?v=55pgyMWPVeI&t=569s
let imageNum = 1;
// displayImg(imageNum);

function nextImg(n) {
  displayImg((imageNum += n));
}

function currentSlide(n) {
  console.log(`n${n}`);
  displayImg((imageNum = n));
  console.log(4);
}

function displayImg(n) {
  let i;
  let image = document.getElementsByClassName("slideImage");
  let dots = document.getElementsByClassName("dot");

  if (n > image.length) {
    imageNum = 1;
  }
  if (n < 1) {
    imageNum = image.length;
  }
  //   This is to make sure that every pic cannot display and
  for (i = 0; i < image.length; i++) {
    image[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  //   Due to the for loop below,
  // this line is to show the pic as a block mode then user can see their current optional pic.
  image[imageNum - 1].style.display = "block";
  dots[imageNum - 1].className += " active";
}

// ==============================================================
// This is to extract the ID from current URL page.
attractionUrl = window.location.href;
attractionId = attractionUrl.substr(36);
// testing purpose
// attractionId = attractionUrl.substr(33);

url = `http://52.63.14.114:3000/api/attraction/${attractionId}`;
function queryAttractionsById(url) {

  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((response) => {
      let name = response["data"]["name"];
      let mrt = response["data"]["mrt"];
      let category = response["data"]["category"];
      document.getElementById("attractionsName").innerHTML = name;
      document.getElementById("catAndMrt").innerHTML = `${category} at ${mrt}`;

      let description = response["data"]["description"];
      let address = response["data"]["address"];
      let transport = response["data"]["transport"];
      document.getElementById("attractionDescriptionFromAPI").innerHTML =
        description;
      document.getElementById("attractionAddressFromAPI").innerHTML = address;
      document.getElementById("attractionTransportationFromAPI").innerHTML =
        transport;

      // This FOR LOOP is to extract the image from a list.
      for (let i = 0; i < response["data"]["images"].length; i++) {
        let image = response["data"]["images"][i];
        createTagsForAttractionImg(image);
        createTagsForAttractionInfo(i + 1);
      }
      // This is
      displayImg(imageNum);
    });
}

function createTagsForAttractionImg(image) {
  // The reason giving [0] is because the "getElementsByClassName" will return a list back.
  let attractionPic = document.getElementsByClassName("attractionPic")[0];
  let arrorButton = document.getElementById("arrorButton");

  let slideImage = document.createElement("div");
  slideImage.className = "slideImage";
  let img = document.createElement("IMG");
  img.src = image;
  slideImage.appendChild(img);
  // The reason I used inserBeofore is I forgot to use one more div to contain all the children div
  // So, I have to use this method to resolve my issue.
  // Reference: https://www.youtube.com/watch?v=FGS6j8MtT6U
  attractionPic.insertBefore(slideImage, arrorButton);
}
queryAttractionsById(url);

function createTagsForAttractionInfo(n) {
  let dotsContainer = document.getElementsByClassName("dotsContainer")[0];

  let dot = document.createElement("span");
  dot.className = "dot";
  dot.onclick = function () {
    currentSlide(n);
  };

  // This is another way to write the same function as above.
  // dot.addEventListener("click", function () {
  //   currentSlide(n);
  // });
  dotsContainer.appendChild(dot);
}
