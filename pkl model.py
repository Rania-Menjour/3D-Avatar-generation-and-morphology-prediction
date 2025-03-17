import os
import pickle
import shutil
import open3d as o3d
import tkinter as tk
from tkinter import simpledialog

# Load the pickle file
pkl_file_path = 'C:\\Users\\rania\\Desktop\\Avatar project\\trained_models.pkl'
with open(pkl_file_path, 'rb') as file:
    loaded_objects = pickle.load(file)

# Extract objects from the loaded pickle file
loaded_best_rf = loaded_objects['best_rf_model']
loaded_scaler = loaded_objects['scaler']
loaded_knn_model = loaded_objects['knn_model']
loaded_data = loaded_objects['data']

print("Pickle file loaded successfully!")

# Initialize tkinter
root = tk.Tk()
root.title("Avatar Generation")

# Prompt the user to input measurements using tkinter
bust = float(simpledialog.askstring("Input", "Bust (cm):", parent=root))
under_bust = float(simpledialog.askstring("Input", "Under Bust (cm):", parent=root))
waist = float(simpledialog.askstring("Input", "Waist (cm):", parent=root))
hip = float(simpledialog.askstring("Input", "Hip (cm):", parent=root))
neck_girth = float(simpledialog.askstring("Input", "Neck Girth (cm):", parent=root))
inside_leg = float(simpledialog.askstring("Input", "Inside Leg (cm):", parent=root))
shoulder = float(simpledialog.askstring("Input", "Shoulder (cm):", parent=root))
body_height = float(simpledialog.askstring("Input", "Body Height (cm):", parent=root))
gender = simpledialog.askstring("Input", "Gender (Male/Female):", parent=root).strip().lower()

# Convert gender to 1 for Male, 0 for Female
if gender == "male":
    gender_male = 1
elif gender == "female":
    gender_male = 0
else:
    print("Invalid gender input. Please enter 'Male' or 'Female'.")
    exit()

# Create the measurements list
measurements = [bust, under_bust, waist, hip, neck_girth, inside_leg, shoulder, body_height, gender_male]

# Scale the measurements using the loaded scaler
scaled_measurements = loaded_scaler.transform([measurements])

# Predict the morphology using the Random Forest model
predicted_morphology = loaded_best_rf.predict(scaled_measurements)[0]
print(f"Predicted Morphology: {predicted_morphology}")

# Use KNN to find the closest avatar
closest_avatar = loaded_knn_model.predict(scaled_measurements)
closest_avatar_id = int(closest_avatar[0])  # Convert to integer
print(f"Closest Avatar ID: {closest_avatar_id}")

# Find the corresponding avatar file (assuming avatar ID corresponds to filename)
avatar_filename = f"{closest_avatar_id}.obj"  # Assuming filenames are like '1878.obj'
model_folder = 'C:\\Users\\rania\\Desktop\\Avatar project\\models'
output_folder = 'C:\\Users\\rania\\Desktop\\Avatar project\\classified_avatars'

# Define the destination folder based on predicted morphology
morphology_folder = os.path.join(output_folder, predicted_morphology)

# Check if the morphology folder exists and create it if it doesn't
if not os.path.exists(morphology_folder):
    os.makedirs(morphology_folder)
    print(f"Morphology folder created: {morphology_folder}")
else:
    print(f"Morphology folder already exists: {morphology_folder}")

# Define the source and destination paths for the avatar file
source_path = os.path.join(model_folder, avatar_filename)
destination_path = os.path.join(morphology_folder, avatar_filename)

# Check if the avatar file exists at the source location
if os.path.exists(source_path):
    shutil.copy(source_path, destination_path)
    print(f"Copied avatar {avatar_filename} to {morphology_folder}")

    # Create a label to display the predicted morphology in the Tkinter window
    morphology_label = tk.Label(root, text=f"Predicted Morphology: {predicted_morphology}", font=("Arial", 14))
    morphology_label.pack(pady=20)
    
    # Render the avatar in a separate Open3D window
    def render_avatar(avatar_file_path):
        if not os.path.exists(avatar_file_path):
            print(f"File not found: {avatar_file_path}")
            return
        
        # Load and render the avatar using Open3D
        mesh = o3d.io.read_triangle_mesh(avatar_file_path)
        if not mesh.has_triangles():
            print(f"Failed to load mesh from: {avatar_file_path}")
            return
        
        mesh.compute_vertex_normals()
        mesh.paint_uniform_color([0.7, 0.7, 0.7])  # Light gray color
        
        # Open3D visualization in a new window
        o3d.visualization.draw_geometries([mesh], mesh_show_wireframe=True, mesh_show_back_face=True)
    
    # Call the function to render the avatar
    render_avatar(destination_path)
else:
    print(f"Avatar file {avatar_filename} not found in {model_folder}")

# Start the Tkinter event loop
root.mainloop()