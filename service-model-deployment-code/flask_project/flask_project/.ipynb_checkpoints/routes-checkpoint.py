from flask import Blueprint, render_template

# Define a Blueprint for the routes
main = Blueprint('main', __name__)


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

@app.route('/about')
def about():
    return render_template('about.html')