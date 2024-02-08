import trimesh
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Path to the output folder", required=True)
    args = parser.parse_args()
    output = args.output

    #check if output folder already exists
    if not os.path.exists(output):
        os.mkdir(output) #if it does not exist, create output folder

    #load models
    input_path = "input"
    mesh_screw = trimesh.load_mesh(input_path + "/screw.stl")
    mesh_nut = trimesh.load_mesh(input_path + "/nut.stl")

    #calculate height of screw head
    mask_box = trimesh.creation.box(bounds=[[14, -2, -10], [20, 2, 20]])
    mask_mesh = mesh_screw.intersection(mask_box)
    off_z = mask_mesh.bounds[1, 2] - mask_mesh.bounds[0, 2]

    #Task 1
    screw_centroid = mesh_screw.centroid
    nut_centroid = mesh_nut.centroid
    #position screw in the origin
    #position nut in the origin and translate it along the z-axis by the height of screw head
    screw_translation_vector = [screw_centroid[0]*(-1), screw_centroid[1]*(-1), 0]
    nut_translation_vector = [nut_centroid[0]*(-1), nut_centroid[1]*(-1), off_z]
    mesh_nut.apply_translation(nut_translation_vector)
    mesh_screw.apply_translation(screw_translation_vector)
    #combine nut mesh and screw mesh
    combined_mesh = trimesh.util.concatenate([mesh_screw, mesh_nut])
    #export result
    combined_mesh.export(output + "/nut_and_screw_1.stl")

    #Task 2
    screw_box = mesh_screw.bounds
    nut_box = mesh_nut.bounds
    box = combined_mesh.bounds
    #define mask
    mask_box = trimesh.creation.box(bounds=[box[0, :], [box[1, 0], box[1, 1], off_z + nut_box[1, 2] - nut_box[0, 2]]])
    #using interestion to cut off the excess part of the screw tail
    combined_mesh_2 = combined_mesh.intersection(mask_box)
    #export resutl
    combined_mesh_2.export(output + "/nut_and_screw_2.stl")

    #Task 3
    #calculate sclae factor to elongate the nut
    scale_factor = (screw_box[1, 2]-off_z)/(nut_box[1, 2] - nut_box[0, 2])
    #Place screw and the nut in the origin, elongate the nut and translate it under the screw head
    nut_translation_vector = [nut_centroid[0]*(-1), nut_centroid[1]*(-1), -off_z]
    mesh_nut.apply_translation(nut_translation_vector)
    mesh_nut.apply_scale([1,1,scale_factor])
    nut_translation_vector = [nut_centroid[0]*(-1), nut_centroid[1]*(-1), off_z]
    mesh_nut.apply_translation(nut_translation_vector)
    #combine nut mesh and screw mesh
    combined_mesh_3 = trimesh.util.concatenate([mesh_screw, mesh_nut])
    #export result
    combined_mesh_3.export(output + "/nut_and_screw_3.stl")

    print("Done!\nNew .stl files are created and saved in {} directory".format(output))

if __name__ == "__main__":
    main()