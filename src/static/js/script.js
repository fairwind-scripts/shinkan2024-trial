const slideDown = (el) => {
    el.style.height = "auto";
    let h = el.offsetHeight;
    el.style.height = h + "px";
    el.animate([{ height: 0 }, { height: h + "px" }], {
        duration: 250,
    });
};

const slideUp = (el) => {
    el.style.height = 0;
};

let activeIndex = null;

const accordions = document.querySelectorAll(".include-accordion");
accordions.forEach((accordion) => {
    const accordionBtns = accordion.querySelectorAll(".accordionBtn");
    accordionBtns.forEach((accordionBtn, index) => {
        accordionBtn.addEventListener("click", (e) => {
            activeIndex = index;
            e.currentTarget.parentNode.classList.toggle("active");
            const content = accordionBtn.nextElementSibling;
            if (e.currentTarget.parentNode.classList.contains("active")) {
                slideDown(content);
            } else {
                slideUp(content);
            }
            accordionBtns.forEach((btn, i) => {
                if (activeIndex !== i) {
                    btn.parentNode.classList.remove("active");
                    const openedContent = btn.nextElementSibling;
                    slideUp(openedContent);
                }
            });
            let container = accordion.closest(".scroll-control");
            if (
                e.currentTarget.parentNode.classList.contains("active") ==
                    false &&
                container !== null
            ) {
                container.classList.remove("active");
            } else if (container !== null) {
                container.classList.add("active");
            }
        });
    });
});

const generateLink = () => {
    const path = document.getElementById("pathInput").value;
    const link = document.getElementById("goTo");
    if (link != null) {
        link.href = "/" + path;
    } else {
        alert("Error");
    }
};
