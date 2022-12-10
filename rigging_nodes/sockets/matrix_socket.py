from bpy.types import NodeSocket

class MatrixSocket(NodeSocket):
    '''Matrix socket type'''
    bl_idname = 'MatrixSocketType'
    bl_label = "Matrix Socket"

    def draw(self, context, layout, node, text):
        layout.label(text="Matrix")

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 1.0)