var login_modal = document.getElementById('id01');
var register_modal = document.getElementById('id02');

window.onclick = function(event) {
    if (event.target == login_modal) {
        login_modal.style.display = "none";
    }
    if (event.target == register_modal) {
        register_modal.style.display = "none";
    }
}
