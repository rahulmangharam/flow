import numpy as np

from cistar_dev.core.scenario import Scenario
from cistar_dev.scenarios.figure8.gen import Figure8Generator


class Figure8Scenario(Scenario):
    def __init__(self, name, type_params, net_params, cfg_params=None,
                 initial_config=None, cfg=None):
        """
        Initializes a figure 8 scenario. Required net_params: radius_ring, lanes,
        speed_limit, resolution. Required initial_config: positions.

        See Scenario.py for description of params.
        """
        self.ring_edgelen = net_params["radius_ring"] * np.pi / 2.
        self.intersection_len = 2 * net_params["radius_ring"]
        self.junction_len = 2.9 + 3.3 * net_params["lanes"]
        self.inner_space_len = 0.28

        # instantiate "length" in net params
        net_params["length"] = 6 * self.ring_edgelen + 2 * self.intersection_len + 2 * self.junction_len + \
            10 * self.inner_space_len

        if "radius_ring" not in net_params:
            raise ValueError("radius of ring not supplied")
        self.radius_ring = net_params["radius_ring"]

        self.length = net_params["length"]

        if "lanes" not in net_params:
            raise ValueError("number of lanes not supplied")
        self.lanes = net_params["lanes"]

        if "speed_limit" not in net_params:
            raise ValueError("speed limit not supplied")
        self.speed_limit = net_params["speed_limit"]

        if "resolution" not in net_params:
            raise ValueError("resolution of circular sections not supplied")
        self.resolution = net_params["resolution"]

        super().__init__(name, type_params, net_params, cfg_params=cfg_params,
                         initial_config=initial_config, cfg=cfg,
                         generator_class=Figure8Generator)

    def specify_edge_starts(self):
        """
        See base class
        """
        edgestarts = \
            [("bottom_lower_ring", 0 + self.inner_space_len),
             ("right_lower_ring_in", self.ring_edgelen + 2 * self.inner_space_len),
             ("right_lower_ring_out",
              self.ring_edgelen + self.intersection_len / 2 + self.junction_len + 3 * self.inner_space_len),
             ("left_upper_ring",
              self.ring_edgelen + self.intersection_len + self.junction_len + 4 * self.inner_space_len),
             ("top_upper_ring",
              2 * self.ring_edgelen + self.intersection_len + self.junction_len + 5 * self.inner_space_len),
             ("right_upper_ring",
              3 * self.ring_edgelen + self.intersection_len + self.junction_len + 6 * self.inner_space_len),
             ("bottom_upper_ring_in",
              4 * self.ring_edgelen + self.intersection_len + self.junction_len + 7 * self.inner_space_len),
             ("bottom_upper_ring_out",
              4 * self.ring_edgelen + 3 / 2 * self.intersection_len + 2 * self.junction_len + 8 * self.inner_space_len),
             ("top_lower_ring",
              4 * self.ring_edgelen + 2 * self.intersection_len + 2 * self.junction_len + 9 * self.inner_space_len),
             ("left_lower_ring",
              5 * self.ring_edgelen + 2 * self.intersection_len + 2 * self.junction_len + 10 * self.inner_space_len)]

        return edgestarts

    def specify_intersection_edge_starts(self):
        """
        See base class
        """
        intersection_edgestarts = \
            [(":center_intersection_%s" % (1+self.lanes),
              self.ring_edgelen + self.intersection_len / 2 + 3 * self.inner_space_len),
             (":center_intersection_1",
              4 * self.ring_edgelen + 3 / 2 * self.intersection_len + self.junction_len + 8 * self.inner_space_len)]

        return intersection_edgestarts

    def specify_internal_edge_starts(self):
        """
        See base class
        """
        internal_edgestarts = \
            [(":bottom_lower_ring", 0),
             (":right_lower_ring_in", self.ring_edgelen + self.inner_space_len),
             (":right_lower_ring_out",
              self.ring_edgelen + self.intersection_len / 2 + self.junction_len + 2 * self.inner_space_len),
             (":left_upper_ring",
              self.ring_edgelen + self.intersection_len + self.junction_len + 3 * self.inner_space_len),
             (":top_upper_ring",
              2 * self.ring_edgelen + self.intersection_len + self.junction_len + 4 * self.inner_space_len),
             (":right_upper_ring",
              3 * self.ring_edgelen + self.intersection_len + self.junction_len + 5 * self.inner_space_len),
             (":bottom_upper_ring_in",
              4 * self.ring_edgelen + self.intersection_len + self.junction_len + 6 * self.inner_space_len),
             (":bottom_upper_ring_out",
              4 * self.ring_edgelen + 3 / 2 * self.intersection_len + 2 * self.junction_len + 7 * self.inner_space_len),
             (":top_lower_ring",
              4 * self.ring_edgelen + 2 * self.intersection_len + 2 * self.junction_len + 8 * self.inner_space_len),
             (":left_lower_ring",
              5 * self.ring_edgelen + 2 * self.intersection_len + 2 * self.junction_len + 9 * self.inner_space_len)]

        return internal_edgestarts