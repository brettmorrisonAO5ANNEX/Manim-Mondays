from manim import *
import numpy as np

control_points_x = np.array([[-1, 0, 1], 
                    [-1, 0, 1], 
                    [-1, 0, 1]])
control_points_y = np.array([[1, 1, 1], 
                    [0, 0, 0],
                    [-1, -1, -1]])
control_points_z = np.array([[0, 0, 0],
                    [1, 1, 1],
                    [0, 0, 0]])

#determines the nimber of control points along the u and v axis (essnetially size of the grid)
u_points = np.size(control_points_x, 0)
v_points = np.size(control_points_x, 1)

#the number of control lines is 1 less than the number of control points
n = u_points - 1
m = v_points - 1

#used for defining the 'fineness' of the surface
u_cells = 10
v_cells = 10

#create the actual 'grid in the (u, v) plane
u = np.linspace(0, 1, u_cells)
v = np.linspace(0, 1, v_cells)

class BezierSurface(ThreeDScene):
    def n_i(self, n, i):
        return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

    def B(self, i, n, u):
        return self.n_i(n, i) * (u ** i) * (1 - u) ** (n - i)
    
    def bezier_surface(self, u, v):
        #start the returned point at origin
        point_x = 0;
        point_y = 0;
        point_z = 0;

        #compute the point on the surface given grid coord (u, v)
        for i in range(0, u_points):
            for j in range(0, v_points):
                B_i = self.B(i, n, u)
                B_j = self.B(j, m, v)

                point_x += B_i * B_j * control_points_x[i, j]
                point_y += B_i * B_j * control_points_y[i, j]
                point_z += B_i * B_j * control_points_z[i, j]
    
        #return the calculated point on the surface
        return [point_x, point_y, point_z]

    def construct(self):
        axes = ThreeDAxes()

        #add bazier surface and control points
        bezier_surface_plot = Surface(
            lambda u, v: np.array(self.bezier_surface(u, v)),
            u_range=(0, 1),
            v_range=(0, 1),
            resolution=(u_cells, v_cells),
            fill_color=BLUE,
            fill_opacity=0.5,
        )

        #add control points
        control_points = [Sphere(radius=0.05, stroke_color=RED).move_to(axes.c2p(control_points_x[i, j], 
                                                                                control_points_y[i, j], 
                                                                                control_points_z[i, j]))
                          for i in range(u_points) for j in range(v_points)]
        
        self.add(*control_points)
        self.add(axes, bezier_surface_plot)
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
