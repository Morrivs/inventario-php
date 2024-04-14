<?php
    $user_id_del = limpiar_cadena($_GET['user_id_del']);

    //verificar usuario
    $check_usuario = conexion();
    $check_usuario = $check_usuario -> query("SELECT usuario_id FROM usuario WHERE usuario_id='$user_id_del'");
    //cuantos registros ha seleccionado rowCount()
    if($check_usuario->rowCount()==1){

        //verificar productos asosiados al usuario
        $check_productos = conexion();
        $check_productos = $check_productos -> query("SELECT usuario_id FROM producto WHERE usuario_id='$user_id_del' LIMIT 1");

        if ($check_productos->rowCount()<=0) {
            $eliminar_usuario = conexion();
            $eliminar_usuario = $eliminar_usuario -> prepare("DELETE FROM usuario WHERE usuario_id=:id");

            //prepare statement
            $eliminar_usuario->execute([":id" => $user_id_del]);

            if($eliminar_usuario->rowCount()==1){
                echo '
                    <div class="notification is-info is-light">
                        <strong>¡Usuario Eliminado!</strong><br>
                        Los datos del usuario se eliminaron con exito
                    </div>
                ';
            }else{
                echo '
                    <div class="notification is-danger is-light">
                        <strong>¡Ocurrio un error inesperado!</strong><br>
                        No se pudo eliminar el usuario, intentelo nuevamente
                    </div>
                ';
            }
            $eliminar_usuario=null;
        } else {
            echo '
                    <div class="notification is-danger is-light">
                        <strong>¡Ocurrio un error inesperado!</strong><br>
                        No podemos eliminar el usuario ya que tiene productos registrados
                    </div>
            ';
        }
        $check_productos = null;
    }else{
        echo '
            <div class="notification is-danger is-light">
                <strong>¡Ocurrio un error inesperado!</strong><br>
                El usuario que intenta eliminar no existe
            </div>
        ';
    }
    $check_usuario = null;