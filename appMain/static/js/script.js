
$(document).ready(function() {
   
     $( ".card" ).hover(
     function() {
       $(this).addClass('shadow').css('cursor', 'pointer'); 
     }, function() {
       $(this).removeClass('shadow');
     }
   );

   $( ".cardusers" ).hover(
    function() {
      $(this).addClass('border-success').css('cursor', 'pointer'); 
    }, function() {
      $(this).removeClass('border-success');
    }
  );
   
   });


    
   