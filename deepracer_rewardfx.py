from math import dist


def reward_function(params):
    '''
    simple reward function to keep agent on track and get through in a few steps
    '''

    if params['all_wheels_on_track'] and params['steps'] > 0:
        reward = ((params['progress']/params['steps'])*100 + params['speed']**2)
    else:
        reward = 0.01

    '''
    more rewards the closer the gent gets to the finish line based Basic model:
    Stay inside two borders of the track
    '''
    #Read input patameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    #Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.01*track_width
    marker_2 = 0.125*track_width
    marker_3 = 0.25*track_width

    #Give a very low reward by default
    reward = 1e-3

    #Give a high reward if wheels go of track and the car is somewhere in 
    #between the trach borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0
    elif not params['all_wheels_on_track']:
        reward = -1
    else:
        reward = params['progress']

    #Read input parameters 
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = -1 #likely crashed/ closed to offtrack


    return float(reward)
