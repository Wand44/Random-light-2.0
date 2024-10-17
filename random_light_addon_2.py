bl_info = {
    "name": "Random_Light",
    "author": "wand",
    "version": (1, 6, 0),
    "blender": (3, 6, 0),
    "location": "View3D > N",
    "description": "Adds a light",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from bpy.props import IntProperty
import random 
from bpy.types import (Panel, Operator)

class MyProperties(bpy.types.PropertyGroup):
    
    my_n : bpy.props.IntProperty(name= "Number of lights", soft_min=0, soft_max=10, default = 3)
    my_e : bpy.props.IntProperty(name= "Energy", soft_min=0, soft_max=100, default = 10)
    my_s : bpy.props.FloatProperty(name= "Size", soft_min=0, soft_max=10, default = 0.5)
    my_c : bpy.props.IntProperty(name= "Spread", soft_min=0, soft_max=10, default = 5)
    my_v : bpy.props.IntProperty(name= "Type", soft_min=1, soft_max=2, default = 1)  
    my_z : bpy.props.IntProperty(name= "Hight", soft_min=0, soft_max=10, default = 0)  
    my_color : bpy.props.IntProperty(name= "Enable color", soft_min=0, soft_max=1, default = 1)  
    

    
    
class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "random.1"
    bl_label = "Simple Random Operator"
    
    

    def execute(self, context):
        
        scene = context.scene
        mytool = scene.my_tool
        for obj in bpy.context.scene.objects:
            if obj.name.startswith("Random_light"):
                bpy.context.collection.objects.unlink(obj)
                bpy.data.objects.remove(obj)    
        # Get the selected object
        selected_object = bpy.context.active_object        
                
        if mytool.my_v == 1 :        

            for i in range(0,mytool.my_n):

                с1 = (random.randint(1, 255))
                с2 = (random.randint(1, 255))
                с3 = (random.randint(1, 255))
                x1 = (random.randint(-(mytool.my_c),mytool.my_c))
                y1 = (random.randint(-(mytool.my_c),mytool.my_c))
                z1 = (random.randint(0.0,5.0))

                # Create a new lamp for rim light
                rim_light = bpy.data.lights.new(name="Light", type='POINT')
                rim_light.energy = mytool.my_e
                rim_light.shadow_soft_size = mytool.my_s
                
                if mytool.my_color == 1:
                    rim_light.color = (с1, с2, с3) 
                if mytool.my_color == 0:
                    rim_light.color = (1, 1, 1)
                    
                rim_light_obj = bpy.data.objects.new(name="Random_light", object_data=rim_light)
                bpy.context.collection.objects.link(rim_light_obj)

                # Set the position of rim light
                rim_light_obj.location = (selected_object.location.x + x1, selected_object.location.y + y1, selected_object.location.z + z1)




        if mytool.my_v == 2 :
            
            for i in range(0,mytool.my_n):
            
                с1 = (random.randint(1, 255))
                с2 = (random.randint(1, 255))
                с3 = (random.randint(1, 255))
                x1 = (random.randint(-(mytool.my_c),mytool.my_c))
                y1 = (random.randint(-(mytool.my_c),mytool.my_c))
                z1 = (random.randint(0.0,5.0))
                
            
                # Create a new lamp for rim light                
                rim_light = bpy.data.lights.new(name="Lgight", type='AREA')
                rim_light_obj = bpy.data.objects.new(name="Random_light", object_data=rim_light)
                bpy.context.collection.objects.link(rim_light_obj)
                rim_light.energy = mytool.my_e
                rim_light.size = mytool.my_s
                
                
                if mytool.my_color == 1:
                    rim_light.color = (с1, с2, с3) 
                if mytool.my_color == 0:
                    rim_light.color = (1, 1, 1)
                
                
                rim_light_obj.constraints.new(type="TRACK_TO")
                rim_light_obj.constraints["Track To"].target = selected_object
                rim_light_obj.location = (selected_object.location.x + x1, selected_object.location.y + y1, selected_object.location.z + z1 + mytool.my_z)
                    
        
           
        return {'FINISHED'}
    
class ButtonOperator_1(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "random.2"
    bl_label = "Simple Random Operator"


    def execute(self, context):
        
        for obj in bpy.context.scene.objects:
            if obj.name.startswith("Random_light"):
                bpy.context.collection.objects.unlink(obj)
                bpy.data.objects.remove(obj)    
       
        return {'FINISHED'}
    


class CustomPanel(bpy.types.Panel):
    bl_label = "Random Light" 
    bl_idname = "random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Random Light"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        obj = context.object
        
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
    bl_idname = "config"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Random Light"
    bl_parent_id = "random"
    bl_options = {'DEFAULT_CLOSED'}
    bl_icon = {'MODIFIER'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        obj = context.object
        
        row = layout.row()

        
        row.prop(mytool, "my_z")
        row = layout.row()
        
        row.prop(mytool, "my_color")
        row = layout.row()
        
        row.prop(mytool, "my_e")
        row = layout.row()
        row.prop(mytool, "my_s")
        row = layout.row()
        row.prop(mytool, "my_c")


        

from bpy.utils import register_class, unregister_class

_classes = [
    MyProperties,
    ButtonOperator,
    ButtonOperator_1,   
    CustomPanel,
    PanelA
    
]


def register():
    
    for cls in _classes:
        
        register_class(cls)
        
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type = MyProperties)


def unregister():
    
    for cls in _classes:
        
        unregister_class(cls)
        
        del bpy.types.Scene.my_tool
        

if __name__ == "__main__":
    register()
