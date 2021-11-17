 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='immune_activation_time', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.immune_activation_time = FloatText(
          value=20160,
          step=1000,
          style=style, layout=widget_layout)

        param_name3 = Button(description='save_interval_after_therapy_start', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.save_interval_after_therapy_start = FloatText(
          value=120.0,
          step=10,
          style=style, layout=widget_layout)

        param_name4 = Button(description='SVG_interval_after_therapy_start', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.SVG_interval_after_therapy_start = FloatText(
          value=120.0,
          step=10,
          style=style, layout=widget_layout)

        param_name5 = Button(description='immune_o2_relative_uptake', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.immune_o2_relative_uptake = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name6 = Button(description='immune_relative_adhesion', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.immune_relative_adhesion = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name7 = Button(description='immune_relative_repulsion', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.immune_relative_repulsion = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='number_of_immune_cells', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.number_of_immune_cells = IntText(
          value=7500,
          step=100,
          style=style, layout=widget_layout)

        param_name9 = Button(description='initial_min_immune_distance_from_tumor', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.initial_min_immune_distance_from_tumor = FloatText(
          value=30,
          step=1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='thickness_of_immune_seeding_region', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.thickness_of_immune_seeding_region = FloatText(
          value=75,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.tumor_radius = FloatText(
          value=250,
          step=10,
          style=style, layout=widget_layout)

        param_name12 = Button(description='tumor_mean_immunogenicity', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.tumor_mean_immunogenicity = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='tumor_immunogenicity_standard_deviation', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.tumor_immunogenicity_standard_deviation = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.immune_activation_time, units_button2, desc_button2] 
        row3 = [param_name3, self.save_interval_after_therapy_start, units_button3, desc_button3] 
        row4 = [param_name4, self.SVG_interval_after_therapy_start, units_button4, desc_button4] 
        row5 = [param_name5, self.immune_o2_relative_uptake, units_button5, desc_button5] 
        row6 = [param_name6, self.immune_relative_adhesion, units_button6, desc_button6] 
        row7 = [param_name7, self.immune_relative_repulsion, units_button7, desc_button7] 
        row8 = [param_name8, self.number_of_immune_cells, units_button8, desc_button8] 
        row9 = [param_name9, self.initial_min_immune_distance_from_tumor, units_button9, desc_button9] 
        row10 = [param_name10, self.thickness_of_immune_seeding_region, units_button10, desc_button10] 
        row11 = [param_name11, self.tumor_radius, units_button11, desc_button11] 
        row12 = [param_name12, self.tumor_mean_immunogenicity, units_button12, desc_button12] 
        row13 = [param_name13, self.tumor_immunogenicity_standard_deviation, units_button13, desc_button13] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.immune_activation_time.value = float(uep.find('.//immune_activation_time').text)
        self.save_interval_after_therapy_start.value = float(uep.find('.//save_interval_after_therapy_start').text)
        self.SVG_interval_after_therapy_start.value = float(uep.find('.//SVG_interval_after_therapy_start').text)
        self.immune_o2_relative_uptake.value = float(uep.find('.//immune_o2_relative_uptake').text)
        self.immune_relative_adhesion.value = float(uep.find('.//immune_relative_adhesion').text)
        self.immune_relative_repulsion.value = float(uep.find('.//immune_relative_repulsion').text)
        self.number_of_immune_cells.value = int(uep.find('.//number_of_immune_cells').text)
        self.initial_min_immune_distance_from_tumor.value = float(uep.find('.//initial_min_immune_distance_from_tumor').text)
        self.thickness_of_immune_seeding_region.value = float(uep.find('.//thickness_of_immune_seeding_region').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.tumor_mean_immunogenicity.value = float(uep.find('.//tumor_mean_immunogenicity').text)
        self.tumor_immunogenicity_standard_deviation.value = float(uep.find('.//tumor_immunogenicity_standard_deviation').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//immune_activation_time').text = str(self.immune_activation_time.value)
        uep.find('.//save_interval_after_therapy_start').text = str(self.save_interval_after_therapy_start.value)
        uep.find('.//SVG_interval_after_therapy_start').text = str(self.SVG_interval_after_therapy_start.value)
        uep.find('.//immune_o2_relative_uptake').text = str(self.immune_o2_relative_uptake.value)
        uep.find('.//immune_relative_adhesion').text = str(self.immune_relative_adhesion.value)
        uep.find('.//immune_relative_repulsion').text = str(self.immune_relative_repulsion.value)
        uep.find('.//number_of_immune_cells').text = str(self.number_of_immune_cells.value)
        uep.find('.//initial_min_immune_distance_from_tumor').text = str(self.initial_min_immune_distance_from_tumor.value)
        uep.find('.//thickness_of_immune_seeding_region').text = str(self.thickness_of_immune_seeding_region.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//tumor_mean_immunogenicity').text = str(self.tumor_mean_immunogenicity.value)
        uep.find('.//tumor_immunogenicity_standard_deviation').text = str(self.tumor_immunogenicity_standard_deviation.value)
