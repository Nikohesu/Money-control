function open_close_burger () {
    let menu = document.getElementById("menu-h");
    let hamburguesa = document.getElementById("hamburguesa");
    menu.classList.toggle("active-menu-h");
    hamburguesa.classList.toggle("active-h");

}
function transform_loader() {
    let element = document.getElementById("boton");
    let text = document.getElementById("boton-text");

    element.classList.add("loader");
    element.disabled = true;
    text.classList.add("boton-text-a");

    console.log("cambie");
}