from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/hello')
def hello():
    # Extract the requester's IP address
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        user_ip = request.environ['REMOTE_ADDR']
    else:
        user_ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    # Log the IP address to the console
    print(f"Request received from IP: {user_ip}")
    # Return the IP address in the HTML response
    return render_template_string('<h1>Hello! Your IP address is {{user_ip}}</h1>', user_ip=user_ip)

if __name__ == '__main__':
    app.run(debug=True)
