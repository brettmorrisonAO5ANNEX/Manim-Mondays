# Manim-Mondays
This is a repository of Manim projects I create! I don't have a particular theme I want to follow, I just want to learn more about Manim and share my creations with anyone interested! I am using ManimCE because it has great documentation available (check out https://docs.manim.community/en/stable/index.html for more info!).

# For General Use
Feel free to clone any of these animations and build off of them! You will need to have Manim installed for them to work, however. I use a Conda environment because I found it to be a little easier to set up... if you would like to do the same you can follow the steps below (these are for Mac, but I'm sure the process is quite similar for windows or Linux). Happy animating!

1. Install Conda: https://www.anaconda.com/download

Run the following commands in your terminal:

3. Create an environment to download Manim

```conda create --name name_of_your_environment python=<insert_version_num>```

3. Activate the new environment

```conda activate name_of_your_environment```

4. Install Manim in the environment

```pip3 install manim```

5. Run an animations

```manim -pql file_name.py ClassName```
