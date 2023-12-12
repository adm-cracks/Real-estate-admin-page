$(document).ready(function(){
    $("#probtn").click(function(){
  
      $("#div1").fadeToggle("slow");
      $("#div2").fadeOut("slow");
    
    });
  });
  
  $(document).ready(function(){
    $("#probtn2").click(function(){
      $("#div1").fadeOut("slow");
      $("#div2").fadeToggle("slow");
    
    });
  });



  $(function(){ 
    $("#arch").autocomplete({
        source:
        "{% url 'ser' %}"

    });
});