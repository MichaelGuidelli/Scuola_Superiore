function letturaJsonRisultatiPhp(form) {

    setInterval(() => {
        fetch('risultati.json')
        .then((response) => response.json())
        .then((json) => phpInjection(json, form.name));
    }, 1000);   
}

function phpInjection(datiPhp, nomeForm) {
    
    if (nomeForm == "formSommaEDifferenza" && typeof(datiPhp["risultatoSomma"]) != "undefined" && typeof(datiPhp['risultatoDifferenza']) != "undefined") {
        
        document.getElementById("risultato-somma").innerHTML = datiPhp["risultatoSomma"];
        document.getElementById("risultato-differenza").innerHTML = datiPhp['risultatoDifferenza'];
    } 

    if (nomeForm == "formConcatenatoreStringhe" && (typeof(datiPhp["risultatoConcatenatoreStringhe"]) != "undefined")) {
        
        document.getElementById("risultato-concatenazione").innerHTML = datiPhp["risultatoConcatenatoreStringhe"];
    }

    if (nomeForm == "formLunghezzaStringa" && (typeof(datiPhp["lunghezzaStringa"]) != "undefined")) {

        document.getElementById("risultato-stringa").innerHTML = datiPhp["lunghezzaStringa"];
    }
}
