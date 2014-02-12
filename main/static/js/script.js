/**
 * Created by Alex on 14/01/14.
 */

$("#publicar_nav").on("click",mostrarForm);

var $form = $("form").first();
	/*$form.on("submit",publicar);
var $item = $(".item").first();*/


function mostrarForm(event){
	$form.slideToggle();
	return false;
}

/*function publicar(event){
	var $contenido = $("#contenido");
	var $clon = $item.clone();
	var titulo = $("#titulo").val();
	var url = $("#url").val();
	$clon.hide();
	$clon.find(".titulo_item a").first()
			.text(titulo)
			.attr("href",url);

	$contenido.prepend($clon);
	$clon.fadeIn();
	return false;
}*/