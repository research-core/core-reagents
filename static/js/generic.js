function ShowHideIf(checkingfield, values, elements, allrow){
    allrow = true;
    values = values.split(";");

	var selector;
	if(allrow){
		selector = ".field-"+elements.join( ", .field-" );
	}else{
		selector = ".form-cell."+elements.join( " * ,.form-cell." )+" *";
	}

	$(selector).hide();

    $('#id_'+checkingfield).parent().css('background', 'white');
    
	$("input:radio[name="+checkingfield+"]").click(function() {
		var value = $(this).val(); 		
	    if( $.inArray(value, values)>=0 ){
	    	$(selector).show();
	    }else{
	    	$(selector).hide();
	    }
	});	

	$("input:checkbox[name="+checkingfield+"]").on("click", function() {
		$("input:checkbox[name="+checkingfield+"]").each(function(){
			var value = $(this).val();
			if( $.inArray(value, values)>=0 && this.checked ){
				$(selector).show();
				return false;
			}else{
				$(selector).hide();
			}
	    });
	});

	var should_show = false;
	$("input:radio[name="+checkingfield+"]:checked, input:checkbox[name="+checkingfield+"]:checked").each(function() {
	    var value = $(this).val();
        if( $.inArray(value, values)>=0 ) should_show = true;
	});

	if( should_show ) 
		$(selector).show();
	else
		$(selector).hide();

}

function clear(elem){
	$("#"+elem).parent().children('input').attr('checked', true);
	$("#"+elem).parent().children('input').click();
}

function setUnknownDate(elem){
    $("#"+elem).val("0001-01-01");
}



$(document).ready(function() {

	$("input:radio[value='']").each(function(){
		var id = $(this).attr('id');
		//var link="<a href='javascript:clear(\""+id+"\");' >clear</a>";
		//$(this).parent().parent().parent().parent().parent().children('.control-label').append(link);
        var link="<li><label><a href='javascript:clear(\""+id+"\");' >Reset</a></label></li>";
        $(this).parent().parent().parent().append(link);
        //var link="<label><a href='javascript:clear(\""+id+"\");' >clean</a></label>";
        //$('label[for="'+id+'"]').parent().append(link);
	});
	$("input:radio[value='']").parent().parent().hide();

	$('footer header').html("<ul></ul>")
	$('footer header').show()
	$('h2').each(function(){
		var h2text = $(this).text().replace(" (only if there is a wait and see policy)", '');
		if(h2text.length>27) h2text = h2text.substr(0,27)+" ...";
		$('footer header ul').append("<li class='headerSelector' >"+h2text+"</li>")
	});

	$('.headerSelector').click(function(){
		var text = $(this).text();
		var e = $('h2:contains("'+text.replace(" ...",'')+'")');
		$('html, body').animate({
	         scrollTop: (e.offset().top-70)
	    }, 2000);
	});

	$('.headerSelector').mouseenter(function(){
		$(this).addClass("mouseover");
	});

	$('.headerSelector').mouseleave(function(){
		$(this).removeClass("mouseover");
	});


    $(".vDateField").each(function(){
        var id = $(this).attr('id');
        var link="<br/><a href='javascript:setUnknownDate(\""+id+"\");' >Unknown</a>";
        $(this).parent().parent().children('.c-1').append(link);
    });


});