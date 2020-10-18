import bpy
 
# make mesh
vertices = [(0,0,0), (1,0,0), (1,1,0),(0,1,0)]
edges = [(0,1),(1,2), (2,0), (2,3), (3,0)]
faces = [(0,1,2),(0,2,3)]
new_mesh = bpy.data.meshes.new('petal')
new_mesh.from_pydata(vertices, edges, faces)
new_mesh.update()
# make object from mesh
petal = bpy.data.objects.new('petal_0', new_mesh)
# make collection
daisy_collection = bpy.data.collections.new('daisy')
bpy.context.scene.collection.children.link(daisy_collection)
# add object to scene collection
daisy_collection.objects.link(petal)
