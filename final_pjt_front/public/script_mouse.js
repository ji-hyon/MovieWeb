// @AbubakerSaeed96
// abubakersaeed.netlify.app

// Thanks for viewing
// =========================

let c = document.querySelector(".c");

window.addEventListener("mousemove", (e) => {

  requestAnimationFrame(() => {
    c.style.top = e.pageY + "px";
    c.style.left = e.pageX + "px";

    let d = document.createElement("div");
    d.classList.add('co');
    d.style.top = e.pageY + "px";
    d.style.left = e.pageX + "px";
    d.style.setProperty(`--hue`, Math.floor(Math.random() * 360));

    setTimeout(() => {
      d.style.opacity = 0;
      d.style.transform = 'scale(12)';
      setTimeout(() => c.removeChild(d), 1100);
    }, 500)

    c.appendChild(d);
  })

});