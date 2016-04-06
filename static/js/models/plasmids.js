(function($){ $(document).ready(function(){

	ShowHideIf( 'plasmid_gateway', 'TRUE;', ['plasmid_vector'], true );
	ShowHideIf( 'vectortype', '7;8', ['plasmid_system', 'plasmid_flippases', 'plasmid_attb', 'plasmid_marker'], true );
	ShowHideIf( 'plasmid_mcs', 'on;', ['plasmid_sc_enzymes'], true );


 }); }(Suit.$));