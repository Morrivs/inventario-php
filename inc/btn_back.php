<p class="has-text-right pt-4 pb-4">
		<a href="#" class="button is-link is-rounded btn-back"><- Regresar atrás</a>
	</p>
	<script type="text/javascript">
	    let btn_back = document.querySelector(".btn-back");

	    btn_back.addEventListener('click', function(e){
	        e.preventDefault(); //no redirecciona a alguna parte
	        window.history.back();//vuelve a la ultima pagina que se ha visitado
	    });
	</script>