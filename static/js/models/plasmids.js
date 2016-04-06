(function($){ $(document).ready(function(){

	ShowHideIf( 'plasmid_gateway', 'TRUE;', ['plasmid_vector'], true );
	ShowHideIf( 'plasmid_mcs', 'on;', ['plasmid_sc_enzymes'], true );
	ShowHideIf( 'vectortype', '6;8', ['plasmid_system', 'plasmid_flippases', 'plasmid_attb', 'plasmid_marker'], true );


 }); }(Suit.$));