/**
 * Created by arturo on 1/06/17.
 */
"use strict";


function validar() {
    var username = $('#id_username')[0].value;

    if (username === undefined || username === ""){

        var error = $('#message_error');
        console.log(error);

        error[0].innerText = "Choose a username";

        return false;

    }

    var password = $('#id_password')[0].value;
    console.log(password);
    if (password === undefined || password === ""){

        console.log("Password vacia");

        var error = $('#message_error');
        console.log(error);

        error[0].innerText = "Empty password";

        return false;
    }

    if (password !== $('#repeat_password')[0].value){

        console.log("Passwords no coinciden");

        var error = $('#message_error');
        console.log(error);

        error[0].innerText = "The passwords don't match";

        return false;
    }

    return true;
}

$(document).ready(function () {

    //$('input').bind('enterKey', validar());

    $('#submit_register').on('click', validar);

});