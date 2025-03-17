# 3D-Avatar-generation-and-morphology-prediction

The project focuses on generating personalized 3D avatars using simple body measurements.

Here's a demo of how the ML model works: https://www.youtube.com/watch?v=fgC85pL9hFg

#This is the link to download the zip files so the PKL model can generate the avatars properly: https://drive.google.com/drive/folders/1UrIIXkE6oavJqyQqhmyK7ku8m38JrqAS?usp=drive_link

#Please make sure to change the paths of the files in the Python file accordingly after downloading

# Overview


The process begins with the user entering key body measurements, including:

Bust

Under Bust

Waist

Hip

Neck Girth

Inside Leg

Shoulder Width

Height


These inputs are processed by our model, which then generates a 3D avatar tailored to the given dimensions.

**Data Processing**


Before generating the avatar, we preprocess the data by normalizing measurements to ensure consistency and accuracy. The processed data is fed into the model, which outputs a 3D mesh with proportions closely matching the user's real body.

Once the measurements are processed, the model generates a fully customizable 3D avatar.

**Technologies Used**

Python for model development.

Scikit-learn for data preprocessing and building the model pipeline.

Pickle to serialize and save the model for fast loading during demonstrations.

Open3D for creating and visualizing 3D avatar meshes.


**Conclusion**

In summary, this project bridges the gap between real-world measurements and digital avatar creation. With potential applications in fashion, animation, and other creative fields, it demonstrates my ability to develop practical, innovative solutions. I am continually learning new technologies to improve and refine my projects and working on new ideas that blend art with technology.


