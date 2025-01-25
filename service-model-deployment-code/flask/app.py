from flask import Flask, request, render_template, jsonify
import numpy as np
from PIL import Image, UnidentifiedImageError
import io
import logging
import tensorflow as tf

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create the Flask application
app = Flask(__name__)

# Security and size limits
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # Limit file uploads to 16 MB

# Load the TensorFlow/Keras model directly
# MODEL_PATH = "/srv/models/efficient_net_b0_v1.h5"  # Path to your saved model
MODEL_PATH = "/srv/models/my_cnn_model_v1.h5"  # Path to your saved model
model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = ['dog', 'horse', 'elephant', 'butterfly', 'chicken', 'cat', 'cow', 'sheep', 'spider', 'squirrel']

# Preprocess image for the model
def preprocess_image(image):
    """
    Preprocesses the image to match the input size and format expected by the model.
    """
    target_size = (128, 128)  # Adjust this to your model's expected size
    if image.mode != "RGB":
        image = image.convert("RGB")  # Convert grayscale or other modes to RGB
    image = image.resize(target_size)
    image = np.array(image) / 255.0  # Normalize pixel values to range [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.before_request
def log_request_info():
    """
    Logs incoming requests for debugging and monitoring purposes.
    """
    logging.info(f"Request Path: {request.path}")
    logging.info(f"Request Method: {request.method}")

# Main route for image upload and form rendering
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", error="No file found in the request.")

        images = request.files.getlist("image")
        if len(images) == 0:
            return render_template("index.html", error="No image was uploaded.")

        # Preprocess and validate all images
        processed_images = []
        filenames = []
        predictions = []
        for image_file in images:
            try:
                # Attempt to open the file as an image
                image = Image.open(io.BytesIO(image_file.read()))
                # Preprocess the image
                processed_image = preprocess_image(image)
                processed_images.append(processed_image)
                filenames.append(image_file.filename)
            except UnidentifiedImageError:
                return render_template("index.html", error=f"The file '{image_file.filename}' is not a valid image.")
            except Exception as e:
                return render_template("index.html", error=f"Error processing '{image_file.filename}': {str(e)}")

        # Combine all preprocessed images into a single batch
        processed_images_batch = np.vstack(processed_images)

        try:
            # Predict using the loaded model
            raw_predictions = model.predict(processed_images_batch)

            # Map predictions to class names
            for filename, prediction in zip(filenames, raw_predictions):
                class_index = np.argmax(prediction)  # Get the index of the highest probability
                class_name = CLASS_NAMES[class_index]
                predictions.append({"filename": filename, "class": class_name, "confidence": prediction[class_index]})

            return render_template("index.html", results=predictions)

        except Exception as e:
            return render_template("index.html", error=f"An error occurred during prediction: {str(e)}")

    return render_template("index.html")

# Custom error handler for file size limits
@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template("index.html", error="File size exceeds the maximum allowed size of 16 MB.")


@app.route('/about')
def about():
    return render_template('about.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
