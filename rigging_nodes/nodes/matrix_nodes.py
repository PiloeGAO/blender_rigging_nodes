from bpy.props import FloatVectorProperty
from bpy.types import Node

from rigging_nodes.nodes.abstract import RiggingNodeTreeNode

class MatrixInputNode(RiggingNodeTreeNode, Node):
    '''An input for the matrix type'''
    bl_idname = 'MatrixInputType'
    bl_label = "Matrix Input"

    matrix_prop: FloatVectorProperty(
        name="Matrix",
        description="Matrix to create",
        subtype="NONE", # Must be "Matrix" but not implemented rightnow in Blender.
        size=16
    )

    def init(self, context):
        self.outputs.new('MatrixSocketType', "Matrix")

    def copy(self, node):
        pass

    def free(self):
        pass

    def draw_buttons(self, context, layout):
        layout.prop(self, "matrix_prop")

    def draw_buttons_ext(self, context, layout):
        layout.prop(self, "matrix_prop")

    def draw_label(self):
        return "Matrix Input"