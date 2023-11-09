<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Generar código QR</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">

        <?php
            $cod_maq = 'prueba1'; 
            $apiToken = 'sWCkATuQlzT2solMGTM8BumHnr5CcKtrl70r3kVAK6wuVHPq2nAq1O2M0D4w'; 
            $numeroautorizacion = '2269'; 
            $url = "http://149.202.12.81/rapidprest_i2/public/api/maq1/generarqr/$cod_maq";

            // Datos del formulario 
            $nombre =$_POST['nombre']; 
            $cantidad = (int)$_POST['cantidad'];
            $telefono = $_POST['telefono'];

            // Datos de la solicitud POST
            $postData = array(
                'nombre' =>$nombre,
                'cantidad' =>$cantidad,
                'telefono' =>$telefono,
                'numeroautorizacion' => $numeroautorizacion
            );

            $header = array(
                'Content-Type: application/x-www-form-urlencoded',
                'authorization: Bearer ' . $apiToken
            );

            //Inicializacion de la API 
            $ch = curl_init($url);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
            curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            $response = curl_exec($ch);

            if ($response === false) {
                die('Error al conectarse a la API');
            }


            $responseData = json_decode($response, true);

            // Verificar si la respuesta es correcta
            if (isset($responseData['state']) && $responseData['state'] == 200) {

                // Obtener el código QR generado
                $codigoQR = $responseData['data']['codigo'];
                // Generar el HTML del código QR
                $qrHtml = '<img src="https://api.qrserver.com/v1/create-qr-code/?data=' . urlencode($codigoQR) . '">';
                // Mostrar el código QR en pantalla
                echo "<h3>{$responseData['message']}</h3>"; 
                echo $qrHtml;
                
            } else {
                // error de la API
                $errorMessage = isset($responseData['message']) ? $responseData['message'] : 'Error en la respuesta';
                echo 'Error en la API: ' . $errorMessage;
            }
        ?>

    </div>
</body>
</html>





