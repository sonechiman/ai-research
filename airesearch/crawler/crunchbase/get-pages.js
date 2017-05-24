

function scroll() {
    window.scrollTo(0, document.body.scrollHeight);
}

setInterval(scroll, 2000);

var links = document.querySelectorAll(".identity >a");

links.forEach(function(item) {
    console.log(item.href);
})

var names = document.querySelectorAll(".identity .name");

names.forEach(function(item) {
    console.log(item.textContent);
})