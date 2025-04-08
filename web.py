from http.server import HTTPServer, BaseHTTPRequestHandler
content= """
<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link rel="stylesheet"href="style.css">
     <title>Device specifications</title>

<style>
 body{
  height:100%;
  margin:20px;
  display:flex;
  text-align:center;
  justify-content: center;
  align-items: center;
}
.Logo{
  width:50%;
  height:100%;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
table{
   width:100%;
   height:100%;
   border-collapse:collapse;
   padding:20px;
  
  
}


th,td{
   border:1px solid #1b1a1afa;
   padding:10px;
   text-align:center;
  
}

th{
  background-color: rgb(200, 135, 49);

}

td{
   background-color:antiquewhite;
}

.Table th {
   background-color:rgb(49, 185, 200);
}
.Table td {
   background-color: aquamarine;
}   
</style>
</head>
<body>
<div class="Logo">
   <center>
   <h1>DEVICE SPECIFICATION</h1>
   </center>
  <table>
      <tbody>
      <center>
        <tr>
               <th>Device name</th>
              <td>DESKTOP-MOHHBTU</td>
           </tr>
           <tr>
               <th>Processor</th>
               <td>13th Gen Intel(R)Core(TM)i5-13335U 1.30GHz</td>
           </tr>
           <tr>
               <th>Installed RAM</th>
               <td>16.0 GB(15.7 GB usable)</td>
           </tr>
           <tr>
               <th>Device ID</th>
               <td>15EEEA3B2-7EF5-4DEC-903D-57782C3C005</td>
           </tr>
           <tr>
               <th>Product ID</th>
               <td>00342-42708-33510-AAOEM</td>
           </tr>
           <tr>
               <th>System type</th>
               <td>64-bit operation system,x64-based processor</td>
           </tr>
           <tr>
               <th>Pen and touch</th>
               <td>No pen or touch input is available for this display</td>
          </tr>
      <center>
       </tbody>
      </table>   
</body>
</html>
"""
class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
      print("Get request received...")
      self.send_response(200)
      self.send_header("content-type","text/html")
      self.end_headers()
      self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
httpd= HTTPServer(server_address,MyServer)
httpd.serve_forever()