function showPassword() {
    let el = document.getElementById("input-password");
    if (el.type === "text")
        el.type = "password";
    else if (el.type === "password")
        el.type = "text";
}