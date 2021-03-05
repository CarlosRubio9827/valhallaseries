function cargar_div(url_send,method_send,data_send,div_target,asincronico,modal){
  inicio_carga()
  $.ajax({
    method: method_send,
    url: url_send,
    async:asincronico,
    data: data_send
  })
    .done(function(response) {
      try{
      $("#container_"+div_target).html(response);
      if(modal){
        $("#modal_"+div_target).modal("show");
      }  
    }
    catch(err) {
        console.log(err.message);
    }
    })
    .fail(function(response) {
      console.log(response.responseJSON);
      swal({
        title: 'Error '+response.status,
        text: response.statusText,
        type: 'error',
        confirmButtonText: '<i class="fa fa-check"></i> Continuar',
        showCloseButton: true,
        confirmButtonClass: 'btn btn-danger',
        buttonsStyling: false,
        animation: false,
        customClass: 'animated zoomIn',
      });
    })
    .always(function() {
      fin_carga()
    });
}
function inicio_carga(){
  $(".se-pre-con").fadeIn("slow");
}
function fin_carga(){
  $(".se-pre-con").fadeOut("slow");
}
function mostrar_modal(url_send,div_target) {
  cargar_div(url_send,"GET",{},div_target,true,true);
}

function mostrar_div(url_send,div_target) {
  cargar_div(url_send,"GET",{},div_target,true,false);
}
