from flask import Flask, request
from zoom_libary import *

app = Flask(__name__)

@app.route('/')
def index():
    return """
<!Doctype html>
<html>
<style>
    h1 {
        text-align: center;
        text-decoration: none;
        font-size: 50px;
    }

    div {
        display: inline-block;
        width: 100%;
        height:100%;
    }

    button {
        background-color: #008CBA;
        border: none;
        color: white;
        padding: 190px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 50px;
        width:48.5%;
        margin: 3px;
    }

    input[type=submit] {
        background-color: #008CBA;
        border: none;
        color: white;
        padding: 100px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 50px;
        width:25%;
        margin: 3px;
    }

    input[type=text] {
        background-color: white;
        border: none;
        color: black;
        padding: 100px 30px;
        text-decoration: none;
        display: inline-block;
        font-size: 50px;
        width:65%;
        margin: 3px;
        border: 2px solid black; 
    }

</style>

<body>
    <h1>Zoom Control</h1>
    <form method="get" action="/join">
        <input type="text" id="link" name="link" placeholder="Enter a Zoom link.">
        <input type="submit" value="Submit">
    </form>
    <div>
        <button id="mute-btn">Mute/UnMute</button>
        <button id="video-btn">Turn on/off video</button>
        <button id="view-btn">Switch Views</button>
        <button id="full-btn">Fullscreen</button>
        <button id="chat-btn">Turn on/off chat</button>
        <button id="end-btn">End Zoom</button>
    </div>
    <script>
        const Mutebutton = document.getElementById('mute-btn');
        Mutebutton.addEventListener('click', async _ => {
            try {
                const response = await fetch('/mute', {
                    method: 'get'
                });
                console.log('Completed!', response);
            } catch (err) {
                console.error(`Error: ${err}`);
            }
        });
        const Videobutton = document.getElementById('video-btn');
        Videobutton.addEventListener('click', async _ => {
            try {
                const response = await fetch('/video', {
                    method: 'get'
                });
                console.log('Completed!', response);
            } catch (err) {
                console.error(`Error: ${err}`);
            }
        });
        const Viewbutton = document.getElementById('view-btn');
        Viewbutton.addEventListener('click', async _ => {
            try {
                const response = await fetch('/view', {
                    method: 'get'
                });
                console.log('Completed!', response);
            } catch (err) {
                console.error(`Error: ${err}`);
            }
        });
        const Fullbutton = document.getElementById('full-btn');
        Fullbutton.addEventListener('click', async _ => {
            try {
                const response = await fetch('/fullscreen', {
                    method: 'get'
                });
                console.log('Completed!', response);
            } catch (err) {
                console.error(`Error: ${err}`);
            }
        });
        const Chatbutton = document.getElementById('chat-btn');
        Chatbutton.addEventListener('click', async _ => {
            try {
                const response = await fetch('/meetingChat', {
                    method: 'get'
                });
                console.log('Completed!', response);
            } catch (err) {
                console.error(`Error: ${err}`);
            }
        });
        const Endbutton = document.getElementById('end-btn');
        Endbutton.addEventListener('click', async _ => {
            try {
                const response = await fetch('/end', {
                    method: 'get'
                });
                console.log('Completed!', response);
            } catch (err) {
                console.error(`Error: ${err}`);
            }
        });
    </script>
</body>

</html>
    """

@app.route('/join')
def join_web():
    link = request.args.get('link')
    linkjoin(link)
    return "Done"

@app.route('/mute')
def mute_web():
    mute()
    return "Done"

@app.route('/video')
def video_web():
    video()
    return "Done"

@app.route('/view')
def speaker_web():
    view()
    return "Done"

@app.route('/fullscreen')
def fullscreen_web():
    fullscreen()
    return "Done"

@app.route('/meetingChat')
def meetingChat_web():
    meetingChat()
    return "Done"

@app.route('/end')
def end_web():
    end()
    return "Done"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)