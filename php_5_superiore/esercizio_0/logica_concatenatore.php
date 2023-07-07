<?php

    function concatenatoreStringhe($primaStringa, $secondaStringa) {
        return $primaStringa . " " . $secondaStringa;
    }

    function creaJsonFile() {
        $arrayRisultati = [
            "risultatoConcatenatoreStringhe" => concatenatoreStringhe(filter_var($_POST["prima-stringa"], FILTER_SANITIZE_STRING), filter_var($_POST["seconda-stringa"], FILTER_SANITIZE_STRING)),
        ];

        file_put_contents("risultati.json", json_encode($arrayRisultati));
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        creaJsonFile();    
    }

    echo '<script> window.setTimeout("window.close()", 0.5);</script>';
    
?>
