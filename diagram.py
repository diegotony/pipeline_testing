# -*- coding: utf-8 -*-
# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


# graph_attr = {
#     "fontsize": "45",
#     "bgcolor": "transparent"
# }



with Diagram("Test",filename="diagram", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
    ELB("lb") >> EC2("web") >> RDS("userdb")
