/**
 * Created by arturo on 13/06/17.
 */


$(document).ready(function () {

    $('.note').on('click', function () {

        console.log(this.id);
        $('#' + this.id + " .note_longer").toggle();

    });

});