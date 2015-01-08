$(function() {
 
  console.log("start"); 



  //Clone reference section when button is clicked
  $("#add-reference").click(function(){
  		console.log("add-reference clicked");
  		$( ".reference-form").first().clone().appendTo("#references");
   });
  


  $('#myform').submit(function(e) {
  	e.preventDefault();
    console.log("Submit started");

    //Set the action and type for the form
    $('#myform').attr('action','/application_form_submit/');
    $('#myform').attr('method','post');
    

    //Collect form element with info class save as info
    info = {}
    $(".info").each(function(index,value) {
    	info[$(this).attr('name')] = $(this).val();
    })

    //Get all references and append to array
    references = [];

    //Go though each reference form div element
    $(".reference-form").each(function(index,value) {
	    reference = {};
	    
	    //For every input in the dive element save the form data
		$(this).find("input").each(function(index,value) {
			reference[$(this).attr('name')] = $(this).val();
		});    	
		references.push(reference);

    });
 

    data = JSON.stringify({
    	"info":info,
    	"references":references
    	
    });

    

    console.log(data);
   



    $('<input type="hidden" name="json"/>').val(data).appendTo('#myform');
    //Comment this to not submit and debug 
    this.submit();

});  


//Apply submit funciton to form.submit button





});
