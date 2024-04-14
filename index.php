<?php require("./inc/session_start.php"); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <?php include("./inc/head.php"); ?>
</head>
<body> 
    <!-- inclusion de navbar -->
    
    <?php 
    if(!isset($_GET['vista']) || $_GET['vista']==""){
        $_GET['vista']="login";
    }

    if(is_file("./vistas/".$_GET['vista'].".php") && $_GET['vista']!="login" && $_GET['vista']!="404" ){

        //cerrar sesion forzadamente (solo se accede si se inicia sesion)
        if((!isset($_SESSION['id']) || $_SESSION['id']=="") || (!isset($_SESSION['usuario']) || $_SESSION['usuario']=="")){
            include "./vistas/logout.php";
            exit();
        }

        include("./inc/navbar.php"); 
        include("./vistas/".$_GET['vista'].".php"); 
    }else{
        if($_GET['vista']=="login"){
            include("./vistas/login.php"); 
        }else{
            include("./vistas/404.php"); 
        }
    }
    include("./inc/script.php");
    ?>
</body>
</html>