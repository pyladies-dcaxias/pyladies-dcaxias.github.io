$().ready(function() {
    scrollToObj();
});

function scrollToObj() {
    $(".scroller").click(function() {
        var id = $(this).attr("href");
        $("html, body").animate({
            scrollTop: $(id).offset().top - 10
        }, 1000);
        return false;
    });
}
