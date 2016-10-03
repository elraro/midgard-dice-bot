<?php
    header("Content-type: image/jpeg");
    $frase = $_REQUEST["frase"];
    $imgPath = 'midgardpiz.jpg';
    $image = imagecreatefromjpeg($imgPath);
    $color = imagecolorallocate($image, 0, 0, 0);
    $palabras = explode(" ", $frase);
    $lineas[] = "";
	$lineas[] = "";
	$lineas[] = "";
	$lineas[] = "";
    $contador = 0;
    foreach ($palabras as $palabra) {
		if ($contador < 4) {
			if (strlen($lineas[$contador].$palabra)> 22) {
				$contador+=1;
				$lineas[$contador] = $lineas[$contador].$palabra." ";
			} else {
				$lineas[$contador] = $lineas[$contador].$palabra." ";
			}
		}
    }
    $fontSize = 30;
    $x = 15;
    $y = 185;
    // Add the text
    $font = "./comicsans.ttf";
    $c_linea = 0;
    foreach ($lineas as $linea) {
		imagettftext($image, $fontSize, 0, $x, $y+$c_linea*70, $color, $font, $linea);
		$c_linea+=1;
    }
    imagejpeg($image);
?>
