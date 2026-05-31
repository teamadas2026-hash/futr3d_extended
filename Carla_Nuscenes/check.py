from nuscenes.nuscenes import NuScenes
from nuscenes.utils.data_classes import Box
from nuscenes.utils.geometry_utils import view_points
import numpy as np

nusc = NuScenes(version='v1.14', dataroot="E:\dataset_7_15_rgb_withCamouflagedCar_50_scene_time_wrong_fixed_1600_900_position_proper_trafficmanegerLessCollide_with_lidarseg", verbose=True)
my_sample = nusc.sample[0]
nusc.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='LIDAR_TOP', out_path='E:\check_point\\pointcloud_rendered.png')