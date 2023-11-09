<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 1</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <form method="post" action="generadorqr.php">
        <h2>Generador QR</h2>
        <p>Ingresa los siguientes datos</p>
        <div class="input-wrapper">
            <input type="text" name="nombre" placeholder="Nombre" id="nombre" required>
            <img class="input-icon" src="imagenes/nombre.png" alt="">
        </div>
        <div class="input-wrapper">
            <input type="text" name="cantidad" placeholder="Cantidad" id="cantidad" required>
            <img class="input-icon" src="imagenes/cantidad.png" alt="">
        </div>
        <div class="input-wrapper">
            <input type="text" name="telefono" placeholder="Telefono" id="telefono" required>
            <img class="input-icon" src="imagenes/telefono.png" alt="">
        </div>
        <input class="btn" type="submit" value="Enviar">
    </form>
</body>
</html>