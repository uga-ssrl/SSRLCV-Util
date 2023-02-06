import pyproj
from sympy.vector import CoordSys3D, BodyOrienter, AxisOrienter, Vector, SpaceOrienter
from sympy import Matrix, Symbol
import numpy as np
from sympy.matrices.dense import matrix2numpy

def lla2ecef(lat, lon, alt):
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    x, y, z = pyproj.transform(lla, ecef, lon, lat, alt, radians=False)

    return x, y, z

def convert(rows, lat, lon, alt):
    new_matrix = None

    start_x, start_y, start_z = lla2ecef(lat, lon, alt)

    subtr_x, subtr_y, subtr_z = rows[0][1:4]

    print(start_x, start_y, start_z)

    for row in rows:
        
        pos = np.array([0,0,0], dtype=float)
        pos[0] = float(row[1]) - float(subtr_x)
        pos[1] = float(row[2]) - float(subtr_y)
        pos[2] = float(row[3]) - float(subtr_z)

        pos[1] *= -1
        pos[2] *= -1

        r, p, y = float(row[4]), float(row[5]), float(row[6])

        orienter = BodyOrienter(-r, p, y, '123')

        BASE = CoordSys3D('BASE')
        ORIG = BASE.orient_new('ORIG', (orienter, ))

        orig_matrix = matrix2numpy(ORIG.rotation_matrix(BASE))

        ## Generate New Matrix

        e3_map = np.array([-start_x, -start_y, -start_z]) # points down towards earth's center
        e3_map /= np.linalg.norm(e3_map)

        e1_map = np.array([1, 0, 0], dtype='float64') if not np.array_equal(e3_map, np.array([1, 0, 0], dtype='float64')) else np.array([0, 1, 0], dtype='float64')
        e1_map -= e1_map.dot(e3_map) * e3_map
        e1_map /= np.linalg.norm(e1_map)

        e2_map = np.cross(e3_map, e1_map)

        new_matrix = np.column_stack((e1_map, e2_map, e3_map))

        R = np.matmul(new_matrix, orig_matrix)

        # Convert back to Euler
        row[4] = np.arctan2(float(R[2][1]), float(R[2][2]))
        row[5] = np.arctan2(float(-R[2][0]), np.sqrt(1-float(R[2][0])**2))
        row[6] = np.arctan2(float(R[1][0]),float(R[0][0]))
        
        pos = np.matmul(new_matrix, np.transpose(pos))
        row[1] = float(pos[0]) + start_x / 1000
        row[2] = float(pos[1]) + start_y / 1000
        row[3] = float(pos[2]) + start_z / 1000

