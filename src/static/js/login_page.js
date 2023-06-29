function RefreshCaptcha() {
     var gR = function (o) {
         var res = JSON.parse(o.responseText);
         if (res.success == "true") {
             document.getElementById('secimg').src = res.url;
             document.getElementById('rand2').value = res.tet;
         } else {
         }
     };
     var callback = {success: gR, failure: false};
     var param = 'action=RefreshCaptcha&CapUserID=' + Math.random();
     fum.util.Connect.asyncRequest('POST', '/gateway/PuyaAuthenticate.php?', callback, param);
 }

 function OpenKeyboard(obj) {
     refobj1 = obj;
     window.status = '';
     kbwin = window.open("../shares/keyboard.php", "kbwin", "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=yes, copyhistory=no, width=430, height=200, addressbar=no, top=200, left=200")
 }

 function ChkEmptiness(Object) {
     if (Object.value.length == 0) {
         alert("این فیلد نباید خالی باشد");
         Object.focus();
         return false;
     }
     return true;
 }

 function ChkForm(FormObj) {
     var t = FormObj.DummyVar.value;
     if (!ChkEmptiness(FormObj.UserID) || !ChkEmptiness(FormObj.DummyVar))
         return false;
     if (t.length < 6) {
         alert('Password must be at least 6 characters long!');
         FormObj.DummyVar.focus();
         return false;
     }
     fum.util.password.checkPass();
     FormObj.pswdStatus.value = fum.util.password.result;
     FormObj.UserPassword.value = FormObj.DummyVar.value;
     FormObj.DummyVar.value = '';
     return true;
 }


 $(function () {
     $("input[required]").attr("oninvalid", "this.setCustomValidity('این فیلد الزامی است.')");
     $("input[required]").attr("oninput", "setCustomValidity('')");
 });

 $(document).ready(function () {
     $("#UserID").focus();
 });

 var d = new Date();
 document.cookie = "rand=" + d.getTime() + '_' + d.getTimezoneOffset() + "; expires=Thu, 18 Jun 2019 12:00:00 UTC; path=/";
