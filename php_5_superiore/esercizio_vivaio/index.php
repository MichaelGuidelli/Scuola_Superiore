<?php

    function connessioneDatabaseEQuery () {
        $conn = new mysqli("localhost", "root", "", "Vivaio");

        if ($conn->connect_error) {
            die("Connessione Fallita: " . $conn->connect_error);
        }
          
        $query = "SELECT NomeSpecie
                  FROM SpeciePiante
                  WHERE Fioritura = 'Inverno';";
        
        $risultato = $conn->query($query);

        if ($risultato -> num_rows != 0) {
            echo "<table border>";
            echo "<tr>";
            echo "<th>Nome Specie</th>";
            echo "<tr>";

            while ($row = $risultato->fetch_array()) {
                echo "<tr>";
                echo "<td>$row[NomeSpecie]";
                echo "<tr>";
            } 
            
            echo "</table>";

        } else {
            echo "Non ci sono fiori che sbocciano in questa stagione";
        }

        $conn->close();
    }

    connessioneDatabaseEquery()
    
?>