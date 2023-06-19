# from flask import Flask, render_template, request, jsonify
# import numpy as np
# import tensorflow as tf
# import cv2
#
# app = Flask(__name__)
#
# with open('static/network.json', 'r') as json_file:
#     model = json_file.read()
#
# inceV3_model = tf.keras.models.model_from_json(model)
# inceV3_model.load_weights('static/cp-38.hdf5')
# inceV3_model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
#
#
# @app.route('/', methods=['GET', 'POST'])
# def demo():
#     if request.method == "POST":
#         upload_file = request.files['photo']
#         if upload_file.filename.endswith('.png'):
#             image_path = "static/images/" + upload_file.filename
#             upload_file.save(image_path)
#             isPost = True
#             image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#             resized_image = cv2.resize(image, (299, 299))
#             rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
#             normalized_image = rgb_image / 255.0
#             input_image = np.expand_dims(normalized_image, axis=0)
#
#             predicted = inceV3_model.predict(input_image)
#             predicted_class_index = int(np.argmax(predicted[0], axis=1))
#             predicted_confidence = predicted[0].tolist()
#             class_names = ['adenocarcinoma', 'large cell carcinoma', 'normal', 'squamous cell carcinoma']
#             predicted_class_name = class_names[predicted_class_index]
#             return jsonify({"prediction": predicted_class_name, "confidence": predicted_confidence}), 200
#         else:
#             error_message = "Invalid file format. Please upload a PNG image."
#             return jsonify({"error": error_message}), 400
#     return render_template("index.html", **locals())

# -------------------------------------------------------------------------------
#
# from flask import Flask, render_template, request, jsonify
# import numpy as np
# import tensorflow as tf
# import cv2
#
# app = Flask(__name__)
#
# with open('static/network.json', 'r') as json_file:
#     model = json_file.read()
#
# inceV3_model = tf.keras.models.model_from_json(model)
# inceV3_model.load_weights('static/cp-38.hdf5')
# inceV3_model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
#
#
# @app.route('/', methods=['GET', 'POST'])
# def demo():
#     if request.method == "POST":
#         if 'photo' not in request.files:
#             return jsonify({"error": "No photo sent"}), 400
#
#         upload_file = request.files['photo']
#         if not upload_file.filename.lower().endswith('.png'):
#             image_path = "static/images/temp.png"
#             image = cv2.imdecode(np.frombuffer(upload_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
#             cv2.imwrite(image_path, image)
#         else:
#             image_path = "static/images/" + upload_file.filename
#             upload_file.save(image_path)
#
#         isPost = True
#
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         image = cv2.medianBlur(image, 3)
#         image = cv2.equalizeHist(image)
#
#         resized_image = cv2.resize(image, (299, 299))
#         rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
#         normalized_image = rgb_image / 255.0
#         input_image = np.expand_dims(normalized_image, axis=0)
#
#         predicted = inceV3_model.predict(input_image)
#         predicted_class_index = int(np.argmax(predicted[0], axis=1))
#         predicted_confidence = predicted[0].tolist()
#         class_names = ['adenocarcinoma', 'large cell carcinoma', 'normal', 'squamous cell carcinoma']
#         predicted_class_name = class_names[predicted_class_index]
#
#         return jsonify({"prediction": predicted_class_name, "confidence": predicted_confidence}), 200
#
#     return render_template("index.html", **locals())
#
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify
import werkzeug

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save('./uploadimages/' + filename)
        return jsonify({'message': 'done'})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
