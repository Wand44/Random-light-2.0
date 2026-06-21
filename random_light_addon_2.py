bl_info = {
    "name": "Random_Light",
    "author": "wand",
    "version": (2, 0, 0),
    "blender": (5, 1, 0),
    "location": "View3D > N",
    "description": "Adds a light",
    "warning": "",
    "doc_url": "",
    "category": "Lighting",
}


import bpy
import random
from bpy.types import Panel, Operator


class MyProperties(bpy.types.PropertyGroup):

    my_n: bpy.props.IntProperty(name="Number of lights", soft_min=0, soft_max=10, default=3)
    my_e: bpy.props.IntProperty(name="Energy", soft_min=0, soft_max=100, default=10)
    my_s: bpy.props.FloatProperty(name="Size", soft_min=0, soft_max=10, default=0.5)
    my_c: bpy.props.IntProperty(name="Spread", soft_min=0, soft_max=10, default=5)
    my_v: bpy.props.IntProperty(name="Type", soft_min=1, soft_max=2, default=1)
    my_z: bpy.props.IntProperty(name="Height", soft_min=0, soft_max=10, default=0)
    my_color: bpy.props.IntProperty(name="Enable color", soft_min=0, soft_max=1, default=1)


class ButtonOperator(bpy.types.Operator):
    """Generate random lights around the selected object"""
    bl_idname = "random_light.generate"
    bl_label = "Generate Lights"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        # Remove existing random lights
        for obj in list(bpy.context.scene.objects):
            if obj.name.startswith("Random_light"):
                bpy.context.collection.objects.unlink(obj)
                bpy.data.objects.remove(obj)

        selected_object = bpy.context.active_object

        if selected_object is None:
            self.report({'WARNING'}, "No active object selected")
            return {'CANCELLED'}

        if mytool.my_v == 1:
            for i in range(mytool.my_n):
                # Colors in Blender are 0.0-1.0 linear floats
                c1 = random.random()
                c2 = random.random()
                c3 = random.random()
                x1 = random.randint(-mytool.my_c, mytool.my_c)
                y1 = random.randint(-mytool.my_c, mytool.my_c)
                z1 = random.uniform(0.0, 5.0)

                rim_light = bpy.data.lights.new(name="Light", type='POINT')
                rim_light.energy = mytool.my_e
                rim_light.shadow_soft_size = mytool.my_s

                if mytool.my_color == 1:
                    rim_light.color = (c1, c2, c3)
                else:
                    rim_light.color = (1.0, 1.0, 1.0)

                rim_light_obj = bpy.data.objects.new(name="Random_light", object_data=rim_light)
                bpy.context.collection.objects.link(rim_light_obj)
                rim_light_obj.location = (
                    selected_object.location.x + x1,
                    selected_object.location.y + y1,
                    selected_object.location.z + z1,
                )

        if mytool.my_v == 2:
            for i in range(mytool.my_n):
                c1 = random.random()
                c2 = random.random()
                c3 = random.random()
                x1 = random.randint(-mytool.my_c, mytool.my_c)
                y1 = random.randint(-mytool.my_c, mytool.my_c)
                z1 = random.uniform(0.0, 5.0)

                rim_light = bpy.data.lights.new(name="Light", type='AREA')
                rim_light.energy = mytool.my_e
                rim_light.size = mytool.my_s

                if mytool.my_color == 1:
                    rim_light.color = (c1, c2, c3)
                else:
                    rim_light.color = (1.0, 1.0, 1.0)

                rim_light_obj = bpy.data.objects.new(name="Random_light", object_data=rim_light)
                bpy.context.collection.objects.link(rim_light_obj)

                rim_light_obj.constraints.new(type="TRACK_TO")
                rim_light_obj.constraints["Track To"].target = selected_object
                rim_light_obj.location = (
                    selected_object.location.x + x1,
                    selected_object.location.y + y1,
                    selected_object.location.z + z1 + mytool.my_z,
                )

        return {'FINISHED'}


class ButtonOperator_1(bpy.types.Operator):
    """Delete all generated random lights"""
    bl_idname = "random_light.delete"
    bl_label = "Delete Lights"

    def execute(self, context):
        for obj in list(bpy.context.scene.objects):
            if obj.name.startswith("Random_light"):
                bpy.context.collection.objects.unlink(obj)
                bpy.data.objects.remove(obj)
        return {'FINISHED'}


class CustomPanel(bpy.types.Panel):
    bl_label = "Random Light"
    bl_idname = "VIEW3D_PT_random_light"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Random Light"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='OUTLINER_OB_LIGHT')

        row = layout.row()
        row.prop(mytool, "my_n")

        row = layout.row()
        row.prop(mytool, "my_v")

        row = layout.row()
        row.operator(ButtonOperator_1.bl_idname, text="Delete", icon='CANCEL')


class PanelA(bpy.types.Panel):
    bl_label = "Config"
    bl_idname = "VIEW3D_PT_random_light_config"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Random Light"
    bl_parent_id = "VIEW3D_PT_random_light"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "my_z")
        layout.prop(mytool, "my_color")
        layout.prop(mytool, "my_e")
        layout.prop(mytool, "my_s")
        layout.prop(mytool, "my_c")


from bpy.utils import register_class, unregister_class

_classes = [
    MyProperties,
    ButtonOperator,
    ButtonOperator_1,
    CustomPanel,
    PanelA,
]


def register():
    for cls in _classes:
        register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperties)


def unregister():
    del bpy.types.Scene.my_tool
    for cls in reversed(_classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()
