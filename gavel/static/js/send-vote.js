function sendForm(action) {
  const XHR = new XMLHttpRequest(),
        FD  = new FormData();

  const route = document.getElementById("route-getter").textContent;
  const next_id = document.getElementById("next_id-getter").textContent;
  const prev_id = document.getElementById("prev_id-getter").textContent;
  const _csrf_token = document.getElementById("_csrf_token-getter").textContent;

  FD.append( "action", action );
  FD.append( "next_id", next_id );
  FD.append( "prev_id", prev_id );
  FD.append( "_csrf_token", _csrf_token );

  XHR.addEventListener( 'load', function( event ) {
    location.reload(true);
  } );

  XHR.open( 'POST', route)
  XHR.send( FD );
}
