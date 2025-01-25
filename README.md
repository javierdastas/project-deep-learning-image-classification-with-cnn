# Project | Deep Learning: Image Classification with CNN
#### Collaborators: Javier Dastas, Paola Rivera

## Description
Build a Convolutional Neural Network (CNN) model to classify images from a given dataset into predefined categories/classes.

## Dataset Chosen for Project
Kaggle - Animals10: The second dataset contains about 28,000 medium quality animal images belonging to 10 categories: dog, cat, horse, spyder, butterfly, chicken, sheep, cow, squirrel, elephant. The link is [here](https://www.kaggle.com/datasets/alessiocorrado99/animals10/data).

## Presentation
- [Deep Learning: Image Classification with CNN](DL_Image_Classification_CNN.pdf)

## Assessment Components

### **Part 1: Data Preprocessing**
- Data loading and preprocessing (e.g., normalization, resizing, augmentation).
- Create visualizations of some images, and labels.

### **Part 2: Model Architecture**
- Design a CNN architecture suitable for image classification.
   - [18-layer CNN Model Architecture](https://github.com/javierdastas/project-deep-learning-image-classification-with-cnn/blob/main/my-cnn-model.png)
- Include convolutional layers, pooling layers, and fully connected layers.

### **Part 3: Model Training**

- Train the CNN model using appropriate optimization techniques (e.g., stochastic gradient descent, Adam). Utilize techniques such as early stopping to prevent overfitting.

### **Part 4: Model Evaluation**
- Evaluate the trained model on a separate validation set.
- Compute and report metrics such as accuracy, precision, recall, and F1-score.
- Visualize the confusion matrix to understand model performance across different classes.

### **Part 5: Transfer Learning**
- Evaluate the accuracy of your model on a pre-trained models like ImagNet, VGG16, Inception... (pick one an justify your choice)
You may find this link helpful.
This is the Pytorch version.
- Perform transfer learning with your chosen pre-trained models i.e., you will probably try a few and choose the best one.

#### **Define the Model & Freeze the Model Base**

## EfficientNetB0 - TensorFlow Keras implementation

#### **Define the Model: DataSet Preparation (validation and classes balance)**

#### **Model Pre-Trainning**

#### **Model Fine-Tunning (unfreeze model base and train again)**
- Unfreeze top layers to ajust using our dataset
- Use a lower learning rate to reduce hard changes on the weights

#### ***Analyze the results and select de best model for Deployment

### **Part 6: Model Deployment**
- Our 18-layer CNN model metrics are better ([see the notebook]()).
- The model selected for deployment was out 18-layer CNN model.
- Configure and set the Web Service Model Image Classification based on Flask and TensorFlow implementation.
    - [Image Classification Using 18-layer Convolutional Neural Networks](http://dl-image-cnn.org)
