$('input[name=checkbox]').change(function () {
      if($(this).is(':checked')){
        console.log("Checkbox is checked..") 
        let command = 'start';

        $.ajax({
          url: '/camera_cmd',
          type: 'POST',
          dataType: 'json',
          data: JSON.stringify({
            'command': command,
          }),
          contentType: 'application/json, charset=UTF-8',
          success: function(data) {
            // location.reload();
            console.log(command);
          },
          error: function(err){
            console.log(err);
          }
        });
      }
      else {        
        $('#attend-image').removeClass('hide'); 
        console.log("Checkbox is not checked..");
        let command = 'stop';

        $.ajax({
          url: '/camera_cmd',
          type: 'POST',
          dataType: 'json',
          data: JSON.stringify({
            'command': command,
          }),
          contentType: 'application/json, charset=UTF-8',
          success: function(data) {
            // location.reload();
            console.log(command);
          },
          error: function(err){
            console.log(err);
          }
        });
      }        
   });