// alert("Hello, world!")







document.querySelector("#twi").addEventListener("click", () => {
    document.getElementById("twi_form").style.display = "block"
    document.getElementById("english_form").style.display = "none"
})


document.querySelector("#english").addEventListener("click", () => {
    document.getElementById("english_form").style.display = "block"
    document.getElementById("twi_form").style.display = "none"
})





