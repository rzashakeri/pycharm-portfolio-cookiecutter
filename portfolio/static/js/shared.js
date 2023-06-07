function resize(e) {
    const size = `${e.x}px`;
    sidebar.style.flexBasis = size;
}

function showContent() {
    let element = document.querySelector(".sidebar-content");
    let sideBar = document.querySelector("#sidebar")
    if (element.style.display === "none") {
        element.setAttribute(
            "style",
            "display: flex; flex-direction: column; width: 210px;"
        );
    } else {
        element.setAttribute("style", "display: none;");
        sideBar.removeAttribute("style");

    }
}

const resizer = document.querySelector("#resizer");
const sidebar = document.querySelector("#sidebar");

resizer.addEventListener("mousedown", (event) => {
    document.addEventListener("mousemove", resize, false);
    document.addEventListener(
        "mouseup",
        () => {
            document.removeEventListener("mousemove", resize, false);
        },
        false
    );
});

setInterval(() => $("#dateTime").text(new Date().toLocaleString()), 1000);

function changeFirstHeaderIcon() {
    let element = document.querySelector(".sidebar-first-header-icon");
    let sidebarItems = document.querySelector(".sidebar-items");
    if (element.className === "sidebar-first-header-icon") {
        element.setAttribute(
            "src",
            "./assets/images/icons/findAndShowNextMatches.svg"
        );
        element.className += " open";
        sidebarItems.removeAttribute("style");
    } else {
        element.setAttribute("src", "./assets/images/icons/play_forward.svg");
        element.className = "sidebar-first-header-icon";
        sidebarItems.setAttribute("style", "display: none;");
    }
}

function changeProjectsIcon() {
    let element = document.querySelector(".sidebar-projects-icon");
    let sidebarItems = document.querySelector(".sidebar-projects-content");
    if (element.className === "sidebar-projects-icon") {
        element.setAttribute(
            "src",
            "./assets/images/icons/findAndShowNextMatches.svg"
        );
        element.className += " open";
        sidebarItems.removeAttribute("style");
    } else {
        element.setAttribute("src", "./assets/images/icons/play_forward.svg");
        element.className = "sidebar-projects-icon";
        sidebarItems.setAttribute("style", "display: none;");
    }
}

function showSocialMediaIcons() {
    let element = document.querySelector(".social-media");
    if (element.style.display === "none") {
        element.setAttribute("style", "display: flex;");
    } else {
        element.setAttribute("style", "display: none;");
    }
    if (window.matchMedia("(max-width: 600px)").matches && element.style.display === "none") {
        element.setAttribute("style", "display: flex;");
    }
}

let docTitle = document.title;
window.addEventListener("blur", () => {
    document.title = "Come Back :(";
});

window.addEventListener("focus", () => {
    document.title = docTitle;
});
