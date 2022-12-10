# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Rigging Nodes",
    "author" : "PiloeGAO",
    "description" : "",
    "blender" : (3, 4, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "This is a protoype for the Constraint Nodes Project.",
    "category" : "Animation"
}

from . import auto_load

auto_load.init()

import nodeitems_utils
from nodeitems_utils import NodeItem

from rigging_nodes.nodes.abstract import RiggingNodesCategory

node_categories = [
    RiggingNodesCategory("Color", "Color", items=[
        NodeItem("FunctionNodeCombineColor"),
        NodeItem("FunctionNodeSeparateColor"),
    ]),
    RiggingNodesCategory("Input", "Input", items=[
        NodeItem("FunctionNodeInputBool"),
        NodeItem("FunctionNodeInputColor"),
        NodeItem("FunctionNodeInputInt"),
        NodeItem("FunctionNodeInputString"),
        NodeItem("FunctionNodeInputVector"),
    ]),
    RiggingNodesCategory("Text", "Text", items=[
        NodeItem("FunctionNodeReplaceString"),
        NodeItem("FunctionNodeSliceString"),
        NodeItem("FunctionNodeStringLength"),
        NodeItem("FunctionNodeValueToString"),
        NodeItem("FunctionNodeInputSpecialCharacters"),
    ]),
    RiggingNodesCategory("Utilities", "Utilities", items=[
        NodeItem("FunctionNodeAlignEulerToVector"),
        NodeItem("FunctionNodeBooleanMath"),
        NodeItem("FunctionNodeCompare"),
        NodeItem("FunctionNodeFloatToInt"),
        NodeItem("FunctionNodeRandomValue"),
        NodeItem("FunctionNodeRotateEuler"),
    ]),
    RiggingNodesCategory('Matrix', "Matrix related nodes", items=[
        NodeItem("MatrixInputType"),
    ]),
]

def register():
    auto_load.register()

    nodeitems_utils.register_node_categories('RIGGING_NODES', node_categories)

def unregister():
    nodeitems_utils.unregister_node_categories('RIGGING_NODES')

    auto_load.unregister()
