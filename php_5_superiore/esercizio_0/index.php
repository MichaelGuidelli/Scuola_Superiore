<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Esercizio 0</title>
    <link rel='stylesheet' href='main.css'>
</head>
<body>

    <div class="card">
        <h1 class="titolo">Somma e Differenza</h1>
        <form action="logica_somma_differenza.php" method="post" name="formSommaEDifferenza" onsubmit="letturaJsonRisultatiPhp(this)" enctype="multipart/form-data" target="_blank"> 
            <input required type="number" class="input" name="primo-numero" placeholder="Inserisci un numero">
            <input required type="number" class="input" name="secondo-numero" placeholder="Inserisci un numero">
            <button type="submit" name="submit-button" class="buttons">Calcola</button>
                
            <p>Somma <p class="risultato" id="risultato-somma"></p></p>
            <p>Differenza <p class="risultato" id="risultato-differenza"></p></p>
        </form>
    </div>

    <div class="card">
        <h1 class="titolo">Concatenatore Stringhe</h1>
        <form action="logica_concatenatore.php" method="post" name="formConcatenatoreStringhe" onsubmit="letturaJsonRisultatiPhp(this)" enctype="multipart/form-data" target="_blank"> 
            <input required type="text" class="input" name="prima-stringa" placeholder="Inserisci una Stringa">
            <input required type="text" class="input" name="seconda-stringa" placeholder="Inserisci una Stringa">
            <button type="submit" name="submit-button" class="buttons">Concatena</button>

            <p>Stringa Concatenata <p class="risultato" id="risultato-concatenazione"></p></p>
        </form>
    </div>

    <div class="card">
        <h1 class="titolo">Contatore Lunghezza Stringa</h1>
        <form action="logica_lunghezza_stringa.php" method="post" name="formLunghezzaStringa" onsubmit="letturaJsonRisultatiPhp(this)" enctype="multipart/form-data" target="_blank">
            <input required type="text" class="input" name="stringa-da-contare" placeholder="Inserisci una Stringa">
            <button type="submit" name="submit-button" class="buttons">Conta</button>

            <p>Lunghezza <p class="risultato" id="risultato-stringa"></p></p>
        </form>
    </div>
    
    <script src="app.js"></script>

</body>
</html>
