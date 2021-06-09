from flask import Flask, request
import cv2, numpy as np
import tensorflow as tf

app = Flask(__name__)

def predict_image(image_up, model):
    im = image_up
    im_array = np.asarray(im)
    im_array = im_array * (1 / 255)
    predict_label = np.argmax(model.predict(im_array))

    return ['Boat', 'Bus', 'Car', 'Cat', 'Flower', 'Horse'][predict_label]


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Test Flask"

@app.route('/predict', methods=['POST'])
def predict():
    # Load Model
    model = tf.keras.models.load_model('model.h5')

    file = request.files['image'].read()
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))

    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img = np.vstack([x])

    print('test')
    return predict_image(img, model)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port='5000')