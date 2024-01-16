from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = '1234'  # สามารถกำหนดให้เป็นค่าสุ่ม

queue_number = 1
image_path = "path_to_your_image.jpg"

@app.route('/')
def index():
    return render_template('index.html', queue_number=session.get('queue_number', queue_number), image_path=image_path)

@app.route('/increment/<int:num>', methods=['POST'])
def increment_queue(num):
    global queue_number
    queue_number += num
    session['queue_number'] = queue_number
    return str(queue_number)

if __name__ == '__main__':
    app.run(debug=True)
