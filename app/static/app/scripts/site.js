let theme = 'dark'

addEventListener('load', (event) => {
    theme = getCookie('theme')
    if (theme == null) {

        let darkMode = window.matchmedia("(prefers-color-scheme: dark)").matches;
        if (darkMode) {
            theme = 'dark'
        }
        else {
            theme = 'light'
        }
        setCookie('theme', theme, 30)
    }
    document.documentElement.setAttribute('data-bs-theme', theme)
})


function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}


function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function deleteCookie(name) {
    document.cookie = name + '=; Max-Age=-99999999;';
}

function SwitchTheme() {
    if (theme == 'light') {
        document.documentElement.setAttribute('data-bs-theme', 'dark')
        theme = 'dark'
    }
    else {
        document.documentElement.setAttribute('data-bs-theme', 'light')
        theme = 'light'
    }
    deleteCookie('theme')
    setCookie('theme', theme, 30)
}

document.getElementById('btnSwitch').addEventListener('click', SwitchTheme)
