/**
 * Created by arturo on 1/06/17.
 */

function validar() {

    var password = $('#id_password');
    console.log(password);
    if (password === ""){

        console.log("Password vacia");

        return false;
    }

    if (password !== $('#repeat_password')){

        console.log("Passwords no coinciden");

        return false;
    }


}

$(document).ready(function () {

    $('input').bind('enterKey', validar());

    $('#submit_register').on('click', validar());

});