$(function () {
     $("input[required]").attr("oninvalid", "this.setCustomValidity('این فیلد الزامی است.')");
     $("input[required]").attr("oninput", "setCustomValidity('')");
 });