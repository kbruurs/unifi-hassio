// Call the dataTables jQuery plugin
$(document).ready(function() {
  var table = $('#dataTable').DataTable();
  
	  // Delete record
				  $('#dataTable tbody').on('click','.deleteTicket',function(){
					 var id = $(this).data('id');

					 var deleteConfirm = confirm("Are you sure?");
					 if (deleteConfirm == true) {
						// AJAX request
						$.ajax({
						  url: '/_delete_voucher',
						  type: 'post',
						  data: {id: id},
						  success: function(response){
							 if(response.status == "success"){
								alert("Record deleted.");

								// Reload DataTable
								table.row('#'+id).remove().draw();
							 }else{
								alert("Invalid ID."+response.status);
							 }
						  }
						});
					 } 

				  });
  
  

});

