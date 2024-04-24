import pdfkit

def getCertificate(name, competition):
    imagePath= "certificateDesign.jpg"
    fontSize= "0.37in"   
    if len(competition)> 19:
        fontSize= "0.33in"

    htmlcontent = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <link href='https://fonts.googleapis.com/css?family=Dancing Script' rel='stylesheet'>
            <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
            <title>Certificate Design</title>
            <style>
                body{{
                    padding: 0;
                    margin: 0;
                    color: rgba(0, 0, 0, 0.863);
                    /*font-family: 'Dancing Script'; */        
                    /*font-family: "Parisienne", cursive;*/
                    /*font-family: "Montserrat", sans-serif;*/
                    /*font-family: "Ubuntu", sans-serif;*/
                    
                    font-family: "Playfair Display", serif;
                    font-style: italic;
                }}
                .container {{
                    position: absolute;
                    overflow: hidden;
                    text-align: center;
                    display: block;
                    background-color: purple;
                }}
                .name{{
                    padding: 0px;
                    margin: 0px;
                }}
                .name-div{{
                    /*background-color: blue;*/
                    position: absolute;
                    text-align: center;
                    height: 0.45in;
                    width:4.4in;
                    top: 3.33in;
                    left: 4.42in;
                    padding: 0px;
                    margin: 0px;
                    font-size:0.37in;
                }}
                .competition{{
                    padding: 0px;
                    margin: 0px;
                }}
                .competition-div{{
                    /*background-color: red*/;
                    position: absolute;
                    text-align: center;
                    height: 0.45in;
                    width:3.81in;
                    top: 4.09in;
                    left: 5.7in;
                    padding: 0px;
                    margin: 0px;
                    font-size:{fontSize};
                }}
                img{{
                    width: 100%;
                    z-index: -1;
                }}
            </style>
        </head>
        <body>
            <img src={imagePath} alt="">
            <div class="name-div">
                <p class="name">{name}</p>
            </div>
            <div class="competition-div">
                <p class="competition">{competition}</p>
            </div>
        </body>
        </html>
    '''

    htmlFile = open("temp.html","w")     
    htmlFile.write(htmlcontent)  
    htmlFile.close()
    options = {
            'dpi': 365,
            'margin-top': '0in',
            'margin-right': '0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'page-height': '6.3in',
            'page-width': '8in',
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None,
        }

    certificateFile= "certificate.pdf"
    pdfkit.from_file("temp.html", certificateFile , options=options)
    return certificateFile