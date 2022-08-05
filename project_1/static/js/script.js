function show_active_link(menu){
    try{
        let elem = document.getElementById(menu).querySelectorAll("a")
        let url = document.location.href
        for(link in elem){
            if(elem[link].href == url){
                elem[link].classList.add("active")
            }
        }
    } catch{}
}
show_active_link("menu")

function print_full_text(body){
    try{
        let elem = document.getElementById(body).querySelectorAll("a")
        let url = document.location.href
//        console.log(url)

        for(link in elem){
            if(elem[link].href == url){
                document.createElement(element)
            }
        }
    } catch{}
}
print_full_text("menu")