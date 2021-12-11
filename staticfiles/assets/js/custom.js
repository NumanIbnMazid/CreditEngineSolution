// Custom Scripts
// Author: Numan Ibn Mazid [numanibnmazid@gmail.com]

// dynamic navbar active
$(function ($) {
    let url = window.location.href
    $('nav ul li a').each(function () {
        if (this.href === url) {
            $(this).addClass('active')
            // $(this).parent().parent().parent().addClass('menu-open')
        }
    })

    // console.log(url)
})

// Digital Clock Script

$(document).ready(function () {
    clockUpdate();
    setInterval(clockUpdate, 1000)
});

function clockUpdate() {
    var date = new Date()
    $(".digital-clock").css({
        color: "#fff",
        "text-shadow": "0 0 6px #ff0"
    })

    function addZero(x) {
        if (x < 10) {
            return (x = "0" + x)
        } else {
            return x
        }
    }

    function twelveHour(x) {
        if (x > 12) {
            return (x = x - 12)
        } else if (x == 0) {
            return (x = 12)
        } else {
            return x
        }
    }

    var h = addZero(twelveHour(date.getHours()))
    var m = addZero(date.getMinutes())
    var s = addZero(date.getSeconds())

    $(".digital-clock").text(h + ":" + m + ":" + s)
}