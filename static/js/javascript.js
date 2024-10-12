//    if(this.value=='flexSwitchCheckChecked'){
//        document.getElementById("form_exp").style.display='none';
//    }
//    else
//        document.getElementById("form_inc").style.display='none';

function form_choice_inc (){
    document.getElementById('form_exp').style.display = "none";
    document.getElementById('form_inc').style.display = "block";
    console.log(event);
}
function form_choice_exp (){
    document.getElementById('form_inc').style.display = "none";
    document.getElementById('form_exp').style.display = "block";
    console.log(event);
}
function dropdown(){
const dropdownElementList = document.querySelectorAll('.dropdown-toggle')
const dropdownList = [...dropdownElementList].map(dropdownToggleEl => new bootstrap.Dropdown(dropdownToggleEl))
}
