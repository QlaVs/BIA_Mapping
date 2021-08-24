$(document).ready(function () {
    $("#data_table").DataTable({
        stateSave: true,
        "columnDefs": [
        { "width": "20%", "targets": 0 }
        ]
    });
});