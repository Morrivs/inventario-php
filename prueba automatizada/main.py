import unittest
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class InventarioTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path=r'chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)


    def test_login(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        #foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        #inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

    def test_registrar_producto(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        #foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        #inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Productos')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=product_new']"))
        )
        self.driver.save_screenshot('imagenes/menu_producto.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=product_new']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/producto_nuevo.png')

        #llenar campos
        #codigo
        codigo = self.driver.find_element(By.XPATH, "//input[contains(@name,'producto_codigo')]")
        codigo.send_keys("9790")
        self.driver.save_screenshot('imagenes/RP_codigo.png')

        #Nombre
        nombre = self.driver.find_element(By.XPATH,"//input[contains(@name,'producto_nombre')]")
        nombre.send_keys("leche")
        self.driver.save_screenshot('imagenes/RP_nombre.png')

        #precio
        precio = self.driver.find_element(By.XPATH,"//input[contains(@name,'producto_precio')]")
        precio.send_keys("90")
        self.driver.save_screenshot('imagenes/RP_precio.png')

        #stock
        stock = self.driver.find_element(By.XPATH,"//input[contains(@name,'producto_stock')]")
        stock.send_keys("10")
        self.driver.save_screenshot('imagenes/RP_stock.png')

        #categoria
        categoria = self.driver.find_element(By.XPATH, "//select[contains(@name,'producto_categoria')]")

        item_seleccionado = Select(categoria)
        item_seleccionado.select_by_value("4")
        self.driver.save_screenshot('imagenes/RP_categoria.png')

        #Guardar cambios
        guardar_producto = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Guardar')]")
        guardar_producto.click()

        wait = WebDriverWait(self.driver, 10)  # 10 segundos de espera
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(2)
        self.driver.save_screenshot('imagenes/RP_guardar.png')

    def test_editar_producto(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Productos')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=product_new']"))
        )
        self.driver.save_screenshot('imagenes/menu_producto.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=product_list']")
        elemento_menu.click()


        #click en actualizar
        actualizar = self.driver.find_element(By.XPATH, "//a[@href='index.php?vista=product_update&product_id_up=4'][contains(.,'Actualizar')]")
        actualizar.click()
        self.driver.save_screenshot('imagenes/producto_editar.png')

        #editar stock
        editar_stock = self.driver.find_element(By.XPATH, "//input[contains(@name,'producto_stock')]")
        editar_stock.clear()
        editar_stock.send_keys("15")
        self.driver.save_screenshot('imagenes/editar_stock.png')

        # actualizar cambios
        actualizar_producto = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Actualizar')]")
        actualizar_producto.click()

        wait = WebDriverWait(self.driver, 10)  # 10 segundos de espera
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(2)
        self.driver.save_screenshot('imagenes/editar_producto.png')


    def test_eliminar_producto(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Productos')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=product_new']"))
        )
        self.driver.save_screenshot('imagenes/menu_producto.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=product_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/producto_eliminar_form.png')

        #click eliminar
        eliminar_boton = self.driver.find_element(By.XPATH, "//a[@href='index.php?vista=product_list&page=1&product_id_del=11'][contains(.,'Eliminar')]")
        eliminar_boton.click()
        self.driver.save_screenshot('imagenes/eliminar_producto_menu.png')

    def test_lista_producto(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Productos')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=product_new']"))
        )
        self.driver.save_screenshot('imagenes/menu_producto.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=product_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/Lista_producto.png')


    def test_agregar_categoria(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        # navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Categoria')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=category_new']"))
        )
        self.driver.save_screenshot('imagenes/menu_categoria.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=category_new']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/nueva_Categoria.png')

        #nueva categoria
        nombre_categoria = self.driver.find_element(By.XPATH, "//input[contains(@name,'categoria_nombre')]")
        nombre_categoria.send_keys("Electrodomesticos")
        self.driver.save_screenshot('imagenes/nombre_categoria.png')

        ubicacion_categoria = self.driver.find_element(By.XPATH, "//input[contains(@name,'categoria_ubicacion')]")
        ubicacion_categoria.send_keys("pasillo 2")
        self.driver.save_screenshot('imagenes/ubicacion_categoria.png')

        boton_guardar = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Guardar')]")
        boton_guardar.click()

        wait = WebDriverWait(self.driver, 10)  # 10 segundos de espera
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(1)
        self.driver.save_screenshot('imagenes/categoria_guardada.png')

    def test_editar_categoria(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Categoria')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=category_list']"))
        )
        self.driver.save_screenshot('imagenes/menu_categoria.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=category_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/categoria_editar_menu.png')

        #click en actualizar
        actualizar = self.driver.find_element(By.XPATH, "//a[@href='index.php?vista=category_update&category_id_up=3'][contains(.,'Actualizar')]")
        actualizar.click()
        self.driver.save_screenshot('imagenes/categoria_editar.png')

        #editar ubicacion
        editar_stock = self.driver.find_element(By.XPATH, "//input[contains(@name,'categoria_ubicacion')]")
        editar_stock.clear()
        editar_stock.send_keys("pasillo 1")
        self.driver.save_screenshot('imagenes/editar_ubicacion.png')


    def test_Lista_categoria(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Categoria')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=category_list']"))
        )
        self.driver.save_screenshot('imagenes/menu_categoria.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=category_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/Lista_categorias.png')

    def test_eliminar_categoria(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        # navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Categoria')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=category_list']"))
        )
        self.driver.save_screenshot('imagenes/menu_categoria.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=category_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/categoria_editar_menu.png')

        #click eliminar
        eliminar_boton = self.driver.find_element(By.XPATH, "//a[@href='index.php?vista=category_list&page=1&category_id_del=15'][contains(.,'Eliminar')]")
        eliminar_boton.click()
        self.driver.save_screenshot('imagenes/eliminar_categoria_menu.png')

    def test_Lista_usuarios(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Usuarios')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=user_list']"))
        )
        self.driver.save_screenshot('imagenes/menu_usuarios.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=user_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/Lista_usuarios.png')


    def test_buscar_producto(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Productos')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=product_search']"))
        )
        self.driver.save_screenshot('imagenes/menu_producto.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=product_search']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/producto_buscar.png')

        #click buscar
        buscar = self.driver.find_element(By.XPATH, "//input[contains(@class,'input is-rounded')]")
        buscar.send_keys("maquillaje")
        self.driver.save_screenshot('imagenes/buscar_producto_texto.png')

        boton_buscar = self.driver.find_element(By.XPATH, "//button[@class='button is-info'][contains(.,'Buscar')]")
        boton_buscar.click()
        self.driver.save_screenshot('imagenes/buscar_acabado.png')


    def test_buscar_usuario(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Usuarios')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=user_search']"))
        )
        self.driver.save_screenshot('imagenes/menu_usuarios.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=user_search']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/usuario_buscar.png')

        # click buscar
        buscar = self.driver.find_element(By.XPATH, "//input[contains(@class,'input is-rounded')]")
        buscar.send_keys("caso")
        self.driver.save_screenshot('imagenes/buscar_usuario_texto.png')

        boton_buscar = self.driver.find_element(By.XPATH, "//button[@class='button is-info'][contains(.,'Buscar')]")
        boton_buscar.click()
        self.driver.save_screenshot('imagenes/buscar_usuario_acabado.png')

    def test_buscar_categoria(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Categoria')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=category_search']"))
        )
        self.driver.save_screenshot('imagenes/menu_categoria.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=category_search']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/categoria_buscar.png')

        # click buscar
        buscar = self.driver.find_element(By.XPATH, "//input[contains(@class,'input is-rounded')]")
        buscar.send_keys("globos")
        self.driver.save_screenshot('imagenes/buscar_categoria_texto.png')

        boton_buscar = self.driver.find_element(By.XPATH, "//button[@class='button is-info'][contains(.,'Buscar')]")
        boton_buscar.click()
        self.driver.save_screenshot('imagenes/buscar_categoria_acabado.png')

    def test_registrar_usuario(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        #foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        #inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Usuarios')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=user_new']"))
        )
        self.driver.save_screenshot('imagenes/menu_usuario.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=user_new']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/usuario_nuevo.png')

        #llenar campos
        #Nombres
        nombre = self.driver.find_element(By.XPATH,"//input[contains(@name,'usuario_nombre')]")
        nombre.send_keys("juan michael")
        self.driver.save_screenshot('imagenes/RU_nombre.png')

        #apellidos
        apellidos = self.driver.find_element(By.XPATH,"//input[contains(@name,'usuario_apellido')]")
        apellidos.send_keys("mireles sosa")
        self.driver.save_screenshot('imagenes/RU_apellidos.png')

        #usuario
        usuario = self.driver.find_element(By.XPATH,"//input[contains(@name,'usuario_usuario')]")
        usuario.send_keys("JMMS")
        self.driver.save_screenshot('imagenes/RU_usuario.png')

        #email
        email = self.driver.find_element(By.XPATH, "//input[contains(@type,'email')]")
        email.send_keys("JuanM@gmail.com")
        self.driver.save_screenshot('imagenes/RU_email.png')

        #clave 1
        clave1 = self.driver.find_element(By.XPATH, "//input[contains(@name,'usuario_clave_1')]")
        clave1.send_keys("1234567")
        self.driver.save_screenshot('imagenes/RU_clave1.png')

        #clave 2
        clave1 = self.driver.find_element(By.XPATH, "//input[contains(@name,'usuario_clave_2')]")
        clave1.send_keys("1234567")
        self.driver.save_screenshot('imagenes/RU_clave2.png')

        #Guardar cambios
        guardar_usuario = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Guardar')]")
        guardar_usuario.click()

        wait = WebDriverWait(self.driver, 10)  # 10 segundos de espera
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(2)
        self.driver.save_screenshot('imagenes/RU_guardar_usuario.png')

    def test_editar_usuario(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        #navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Usuarios')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=user_list']"))
        )
        self.driver.save_screenshot('imagenes/menu_usuario.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=user_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/editar_usuario_menu.png')

        #click en actualizar
        actualizar = self.driver.find_element(By.XPATH, "//a[@href='index.php?vista=user_update&user_id_up=2'][contains(.,'Actualizar')]")
        actualizar.click()
        self.driver.save_screenshot('imagenes/usuario_editar_form.png')

        #editar apellido
        editar_stock = self.driver.find_element(By.XPATH, "//input[contains(@name,'usuario_apellido')]")
        editar_stock.clear()
        editar_stock.send_keys("testapellido")
        self.driver.save_screenshot('imagenes/editar_apellido.png')

        #validar
        usuarioVal = self.driver.find_element(By.XPATH, "//input[contains(@name,'administrador_usuario')]")
        usuarioVal.send_keys("morrivs")

        claveVal = self.driver.find_element(By.XPATH, "//input[contains(@name,'administrador_clave')]")
        claveVal.send_keys("1234567")
        self.driver.save_screenshot('imagenes/editar_validar_usuario.png')

        # actualizar cambios
        actualizar_usuario = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Actualizar')]")
        actualizar_usuario.click()

        wait = WebDriverWait(self.driver, 10)  # 10 segundos de espera
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(1)
        self.driver.save_screenshot('imagenes/editar_usuario.png')

    def test_eliminar_usuario(self):
        # Acceder a la página de inicio de sesión de GitHub
        self.driver.get("http://localhost/inventario/index.php?vista=home")

        # foto de entrar a la pagina
        self.driver.save_screenshot('imagenes/entrar_pagina.png')

        # Ingresar nombre de usuario y contraseña
        usuario = self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]")
        usuario.send_keys("morrivs")
        self.driver.save_screenshot('imagenes/usuario.png')

        clave = self.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        clave.send_keys("1234567")
        self.driver.save_screenshot('imagenes/password.png')

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Iniciar sesion')]")
        login_button.click()

        # inicio de sesion
        self.driver.save_screenshot('imagenes/inicio_sesion.png')

        # Esperar a que la página de inicio se cargue
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='index.php?vista=logout'][contains(.,'Salir')]"))
        )

        self.driver.save_screenshot('imagenes/pagina_inicio.png')

        # navbar
        element = self.driver.find_element(By.XPATH, "//a[@class='navbar-link'][contains(.,'Usuarios')]")

        # Posicionar el cursor sobre el elemento
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

        # Espera a que aparezca el menú desplegable
        menu_desplegable = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?vista=user_list']"))
        )
        self.driver.save_screenshot('imagenes/menu_usuario.png')

        # Localiza y selecciona un elemento dentro del menú desplegable
        elemento_menu = menu_desplegable.find_element(By.XPATH, "//a[@href='index.php?vista=user_list']")
        elemento_menu.click()
        self.driver.save_screenshot('imagenes/eliminar_usuario_menu.png')

        #click eliminar
        boton_eliminar = self.driver.find_element(By.XPATH, "//a[@href='index.php?vista=user_list&page=1&user_id_del=15'][contains(.,'Eliminar')]")
        boton_eliminar.click()
        time.sleep(1)

        self.driver.save_screenshot('imagenes/usuario_eliminado.png')


    def cerrar(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
