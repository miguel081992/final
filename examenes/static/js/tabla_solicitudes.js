
$(document).ready(function(){
    // DataTable
    var table = $('#tbl-solicitudes').DataTable({
        "ordering": true,
        "bFilter": true,
        
        columnDefs: [
            { orderable: true, className: 'reorder', targets: 0 },
            { orderable: true, className: 'reorder', targets: 1 },
            { orderable: true, className: 'reorder', targets: 2 },
            { orderable: true, className: 'reorder', targets: 3 },
            { orderable: true, className: 'reorder', targets: 4 },
            { orderable: false, targets: '_all' },
        ],
        "language": {               
            "search":               "Búsqueda General:",
            "searchPlaceholder":    "Valor para buscar",
            "zeroRecords":          "No se han encontrado coincidencias.",
            "lengthMenu":           "Mostrar _MENU_ registros por página",
            "info":                 "Mostrando página _PAGE_ de _PAGES_",
            "infoFiltered":         "(Filtrado de un total de _MAX_ filas.)",
            "paginate": {
                "first":            "Primera",
                "last":             "Última",
                "next":             "Siguiente",
                "previous":         "Anterior"              
            },
        }
    });

    // Setup - add a text input to each footer cell    
    $('#tbl-solicitudes #busq td').each( function (i) {
        if(i != 0 && i != 5){
            var title = $(this).text();
            $(this).html( //'<label>' + title + '</label>' +
                '<input type="text" class="form-control" placeholder="buscar..." />'
            );
        }
    } );
    
    // Apply the search
    table.columns().every( function () {
        var column = this;
        $( 'input', this.header() ).on( 'keyup change', function () {        
            if ( column.search() !== this.value ) {
                column.search( this.value ).draw();
            }
        } );
    } );
});



/*
if(opcion == "0"){
        $('#tbl-solicitudes #busq td').each( function (i) {
            if(i != 0 && i != 1 && i != 5){
                var title = $(this).text();
                $(this).html( //'<label>' + title + '</label>' +
                    '<input type="text" class="form-control" placeholder="'+title+'" />'
                );
            }
        } );
    }else{
        $('#tbl-solicitudes #busq td').each( function (i) {
            if(i != 0 && i != 5){
                var title = $(this).text();
                $(this).html( //'<label>' + title + '</label>' +
                    '<input type="text" class="form-control" placeholder="'+title+'" />'
                );
            }
        } );
    }
*/

/*
$(document).ready(function() {
    // DataTable
    var table = $('#tbl-solicitudes').DataTable({
        "ordering": false,
        "bFilter": true,
        "language": {               
            "search":               "Búsqueda General:",
            "searchPlaceholder":    "Valor para buscar",
            "zeroRecords":          "No se han encontrado coincidencias.",
            "lengthMenu":           "Mostrar _MENU_ registros por página",
            "info":                 "Mostrando página _PAGE_ de _PAGES_",
            "infoFiltered":         "(Filtrado de un total de _MAX_ filas.)",
            "paginate": {
                "first":            "Primera",
                "last":             "Última",
                "next":             "Siguiente",
                "previous":         "Anterior"              
            },
        }
    });

    // Setup - add a text input to each footer cell    
    $('#tbl-solicitudes #busq td').each( function () {
        var title = $(this).text();
        $(this).html( //'<label>' + title + '</label>' +
            '<input type="text" class="form-control" placeholder="'+title+'" />'
        );
    } );

    // Apply the search
    table.columns().every( function () {
        var column = this;
        $( 'input', this.header() ).on( 'keyup change', function () {        
            if ( column.search() !== this.value ) {
                column.search( this.value ).draw();
            }
        } );
    } );
} );*/



/*
$(document).ready(function() {
    // DataTable
    var table = $('#tbl-solicitudes').DataTable({
        //"ordering": false,
        "bFilter": false,
        "language": {               
            "search":               "Búsqueda General:",
            "searchPlaceholder":    "Valor para buscar",
            "zeroRecords":          "No se han encontrado coincidencias.",
            "lengthMenu":           "Mostrar _MENU_ registros por página",
            "info":                 "Mostrando página _PAGE_ de _PAGES_",
            "paginate": {
                "first":            "Primera",
                "last":             "Última",
                "next":             "Siguiente",
                "previous":         "Anterior"              
            },
        }
    });

    // Setup - add a text input to each footer cell
    $('#tbl-solicitudes tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( //'<label>' + title + '</label>' +
            '<input type="text" class="form-control" placeholder="'+title+'" />'
        );
    } );

    // Apply the search
    table.columns().every( function () {
        var column = this;
 
        $( 'input', this.footer() ).on( 'keyup change', function () {
            if ( column.search() !== this.value ) {
                column.search( this.value ).draw();
            }
        } );
    } );
} );*/