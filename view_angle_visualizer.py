"""
I was having some troubles understanding camera orientation in Manim, so I decided to
develope an interactive tool to help figure out values for phi, theta, and gamma to 
achieve the desired view angle
"""
from manim import *

class ThreeDAngleVisTool(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        axes_labels = axes.get_axis_labels(Text("X", color=BLUE), 
                                           Text("Y", color=RED), 
                                           Text("Z", color=GREEN))
        axes_group = VGroup(axes, axes_labels)

        self.add(axes_group)