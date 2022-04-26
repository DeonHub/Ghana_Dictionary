// alert("Hello, world!")


document.querySelector("#twi").addEventListener("click", () => {
    document.getElementById("twi_form").style.display = "block"
    document.getElementById("english_form").style.display = "none"
})


document.querySelector("#english").addEventListener("click", () => {
    document.getElementById("english_form").style.display = "block"
    document.getElementById("twi_form").style.display = "none"
})



var btnContainer = document.getElementById("buttons");
var btns = btnContainer.getElementsByClassName("btn");

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", () => {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}





