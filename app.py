from flask import *

app = Flask("IP TRACKER")

@app.route("/")
def home():
    return """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Cool CSS Tricks</title>
        </head>

        <body>

        <style>
            * {color: black;}
            body {font-family:consolas; background-color:white;}
            h1 {text-align:center;margin-top:11em;}
            h6 {display:inline; margin-top:12em;}
            button {margin-top:1em;padding:1em;background-color:aqua; color:black;}
            
            #blob {
                z-index: -2;
                position: fixed;
                background: #30D5C8;
                border-radius: 100%;
                height:20em;
                aspect-ratio: 1;
                pointer-events: none;
                left:50%;
                top:50%;
                translate: -50% -50%;
                animation: rotate 20s infinite;
                filter: blur(200px);
            }
            
            @keyframes rotate {
                from {
                rotate: 0deg;
                }
                
                50% {
                scale: 1 1.15;
                }
                
                to {
                rotate: 360deg;
                }
            }


        </style>

        <div id="blob"></div>

        <script>const blob = document.getElementById("blob");

            window.onpointermove = event => { 
            const { clientX, clientY } = event;
            
            blob.animate({
                left: `${clientX}px`,
                top: `${clientY}px`
            }, { duration: 800, fill: "forwards" });
            }
        </script>


        <h1>Cool CSS!</h1>
        <center><h5>Check out the cool CSS tricks in this page</h5>
        <dialog modal>A</dialog>
        <button onclick="alert('Ok, here is a trick that has already happened. By some tRICkY methods we have your ip. fullstop.');alert('And we have it stored so even if you leave the site we still have it.');alert('Nope no running away; your ip is ...');alert('......');alert('""" + request.remote_addr + """')">See More CSS Tricks</button></center>


        </body>
        </html>
        """

app.run("0.0.0.0", 80)
