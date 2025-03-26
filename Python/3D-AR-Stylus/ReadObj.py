import pywavefront

# Load the OBJ file
scene = pywavefront.Wavefront('3D_Model/Test.obj')

# Access vertices
for name, material in scene.materials.items():
    vertices = material.vertices
    print(f"Vertices for material {name}:")
    print(vertices)
