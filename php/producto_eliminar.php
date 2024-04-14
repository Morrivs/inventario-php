<?php
$product_id_del = limpiar_cadena($_GET['product_id_del']);

//verificar producto
$check_producto = conexion();
$check_producto = $check_producto -> query("SELECT * FROM producto WHERE producto_id='$product_id_del'");
if ($check_producto->rowCount()==1) {
    $datos = $check_producto->fetch();

    $eliminar_producto = conexion();
    $eliminar_producto = $eliminar_producto -> prepare("DELETE FROM producto WHERE producto_id=:id");

    //prepare statement
    $eliminar_producto->execute([":id" => $product_id_del]);

    if($eliminar_producto->rowCount()==1){
        if(is_file("./img/producto/".$datos['producto_foto'])){
            chmod("./img/producto/".$datos['producto_foto'],0777);
            unlink("./img/producto/".$datos['producto_foto'],0777);
        }
        echo '
            <div class="notification is-info is-light">
                <strong>¡Producto Eliminado!</strong><br>
                Los datos de el producto se eliminaron con exito
            </div>
        ';
    }else{
        echo '
            <div class="notification is-danger is-light">
                <strong>¡Ocurrio un error inesperado!</strong><br>
                No se pudo eliminar el producto, intentelo nuevamente
            </div>
        ';
    }
    $eliminar_producto = null;
} else {
    echo '
    <div class="notification is-danger is-light">
        <strong>¡Ocurrio un error inesperado!</strong><br>
        El PRODUCTO que intenta eliminar no existe
    </div>
    ';
}
$check_producto = null;

