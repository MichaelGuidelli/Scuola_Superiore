<?php

    function contatoreStringhe($Stringa) {
        return strlen($Stringa);
    }

    function creaJsonFile() {
        $arrayRisultati = [
            "lunghezzaStringa" => contatoreStringhe(filter_var($_POST["stringa-da-contare"], FILTER_SANITIZE_STRING)),
        ];

        file_put_contents("risultati.json", json_encode($arrayRisultati));
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        creaJsonFile();    
    }

    echo '<script> window.setTimeout("window.close()", 0.5);</script>';
    
?>
