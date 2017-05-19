

function scroll() {
    window.scrollTo(0, document.body.scrollHeight);
}

setInterval(scroll, 2000);

var items = document.querySelectorAll(".identity >a");

items.forEach(function(item) {
    console.log(item.href);
})

