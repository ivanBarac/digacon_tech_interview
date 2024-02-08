# Digacon Tech Interview

Python script `script.py` takes two STL meshes, a nut and a screw, and combines them in three different ways:

1. **nut_and_screw_1.stl**: Places the nut below the screw head.
2. **nut_and_screw_2.stl**: Places the nut below the screw head and cuts of the excess screw "tail".
3. **nut_and_screw_3.stl**: Makes the nut cover the screw, under the head.

## Usage
Using command prompt, position yourself in the directory containing _script.py_, _nut.stl_ and _screw.stl_. Run this command:
```
python script.py -o output_folder
```
#### Arguments

- `-o`, `--output`: Specifies the directory path for saving generated STL files. (Required)

## Dependencies

- Trimesh: <https://github.com/mikedh/trimesh>
- manifold3d: <https://github.com/elalish/manifold>
- NumPy: <https://numpy.org/>

## Code
The complete Python code and logic reside with the `script.py` file. Trimesh library functionalities are used for loading, manipulating and exporting STL meshes.
Jupyter notebook `notebook.ipynb` contains similar code with few extra cells that consider a more general task.

## Output
Three STL files will be generated and saved in the designated output directory:
- `nut_and_screw_1.stl`
- `nut_and_screw_2.stl`
- `nut_and_screw_3.stl`
