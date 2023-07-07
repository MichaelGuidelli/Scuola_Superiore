<?php

    function somma($primoNumero, $secondoNumero) {
        return $primoNumero + $secondoNumero;
    }

    function differenza($primoNumero, $secondoNumero) {
        return $primoNumero - $secondoNumero;
    }

    function creaJsonFile() {
        $arrayRisultati = [
            "risultatoSomma" => somma(filter_var($_POST["primo-numero"], FILTER_SANITIZE_NUMBER_FLOAT), filter_var($_POST["secondo-numero"], FILTER_SANITIZE_NUMBER_FLOAT)),
            "risultatoDifferenza" => differenza(filter_var($_POST["primo-numero"], FILTER_SANITIZE_NUMBER_FLOAT), filter_var($_POST["secondo-numero"], FILTER_SANITIZE_NUMBER_FLOAT)),
        ];

        file_put_contents("risultati.json", json_encode($arrayRisultati));
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        creaJsonFile();    
    }

    echo '<script> window.setTimeout("window.close()", 0.5);</script>';
    
?>
