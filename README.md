# solidpython2 and OpenSCAD

### Intro:

I set up this repository to act as a working environment for creating personal 3D prints. Everything here is free to use for any purpose. This is all here because I like the idea of using `git` to hold and track all my 3D models.

Reach out if you have any questions or suggestions!

---

### Why?

I bought my first 3D printer in the Spring of 2024 and I initially used Blender (without any plugins) to generate my first 3D models. Blender was free and had tons of resources and so I thought it was the best tool for the job.

Then I discovered parametric vs direct modeling and how one could be better than the other. Coming from the software development world, I thought that parametric modeling would suit me _much_ better as my style of modeling is based more on math and measurements than sculpting and artistic expression.

Then I wondered if all this could be done in a programming language; this led me to OpenSCAD which _then_ led me to the python-`solidpython2` combo.

And now here we are: a system where I can use the VSCode environment and python (both of which I am exceedingly familiar with) to generate 3D models.

And this is all free! And open source!

---

### Usage:

1. Make sure you have OpenSCAD installed: [Install here](https://openscad.org/downloads.html)

2. Download _Antyos's_ Extension _"OpenScad"_ (Antyos.openscad)

3. Make sure you have `nodemon` installed:

```bash
npm install -g nodemon
# or
yarn global add nodemon
```

4. Set up a python virtual environment:

```bash
python3 -m venv venv
pip install -r requirements.txt
```

5. Start the script

```bash
# use nodemon to run the python script with hot reload
nodemon --exec python3 path/to/your/python/script.py
```

6. Make sure your python script is set up to generate a `.scad` file:

```
from solid2 import *
model = cube(10, 10, 10)
model.save_as_scad()
```

7. Right click and choose "Preview in OpenSCAD". This should open OpenSCAD and allow you to preview your model.

8. Edit your python script to see your model refresh in realtime! (nodemon > update `.scad` file > OpenSCAD preview hot reload)

---
