function display_ct1() {
    var x = new Date().toLocaleString("en-US", {timeZone: "America/Sao_Paulo"});
    var y = x.split(", ");
    document.getElementById('ct').innerHTML = y[1] + " " + y[0];
    tt = display_c();
}

function display_ct2() {
    var x = new Date().toLocaleString("en-US", {timeZone: "America/Sao_Paulo"});
    var y = x.split(", ");
    document.getElementById('ct').innerHTML = y[1] + ", " + y[0];
    tt=display_c();
}

function display_ct3() {
    var x = new Date().toLocaleString("en-US", {timeZone: "America/New_York"});
    var y = x.split(", ");
    document.getElementById('ct').innerHTML = y[1] + ", " +y[0];
    tt=display_c();
    }

function display_ct4() {
    var x=new Date().toLocaleString("en-US", {timeZone:"Europe/Budapest"});
    var d=x.split(",");
    document.getElementById('ct').innerHTML=d[1]+","+d[0];
    tt=display_c();
    }