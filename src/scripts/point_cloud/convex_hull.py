import open3d as o3d
import numpy as np

# The convex hull of a point cloud is the smallest convex set that contains all points.
# Open3D contains the method compute_convex_hull
# that computes the convex hull of a point cloud. The implementation is based on Qhull.

bunny = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh(bunny.path)
mesh.compute_vertex_normals()

pcl = mesh.sample_points_poisson_disk(number_of_points=2000)
hull, _ = pcl.compute_convex_hull()
hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
hull_ls.paint_uniform_color((1, 0, 0))
o3d.visualization.draw_geometries([pcl, hull_ls])