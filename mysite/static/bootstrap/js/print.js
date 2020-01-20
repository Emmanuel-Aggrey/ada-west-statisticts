function createPDF() {
// var edit = document.querySelector('.edit')
   
    // document.getElementById('rem').innerHTML=''

     var sTable = document.querySelector('.print_table').innerHTML;
   

     var style = "<style>";
     style = style + "table {width: 100%;font: 17px Calibri;}";
     style = style + "table, th, td {border: solid 1px #DDD; border-collapse: collapse;";
     style = style + "padding: 2px 3px;text-align: center;}";
     style = style + "</style>";

     // CREATE A WINDOW OBJECT.
     var win = window.open('', '', 'height=800,width=800');

     win.document.write('<html><head>');
     win.document.write('<title>QUARTALLY REPORT</title>');   // <title> FOR PDF HEADER.
     win.document.write(style);          // ADD STYLE INSIDE THE HEAD TAG.
     win.document.write('</head>');
     win.document.write('<body>');
     win.document.write(sTable);         // THE TABLE CONTENTS INSIDE THE BODY TAG.
     win.document.write('</body></html>');

     win.document.close(); 	// CLOSE THE CURRENT WINDOW.

     win.print();    // PRINT THE CONTENTS.
 
     
 }
