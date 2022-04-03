// ==UserScript==
// @name         Croatia template
// @namespace    http://tampermonkey.net/
// @version      1.0
// @downloadURL  https://github.com/Eutrix/croplace/raw/main/userscript.user.js
// @updateURL    https://github.com/Eutrix/croplace/raw/main/userscript.user.js
// @description  NaM!
// @author       hotbear1110
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener('load', () => {
            document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
        (function () {
            const i = document.createElement("img");
            i.src = "https://raw.githubusercontent.com/Eutrix/croplace/main/canvas.png";
            i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 1000px;";
            console.log(i);
            return i;
        })())

    }, false);
document.onkeydown = function(e) {
const art = document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].getElementsByTagName("img")[0];
if (e.key == "h" && art.style.display) {
    art.style.removeProperty('display');
} else art.style.display = "none";
}
}