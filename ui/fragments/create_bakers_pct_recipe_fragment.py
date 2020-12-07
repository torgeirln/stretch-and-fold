import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo, showerror


from domain.types.ingredient_types import IngredientTypes
from domain.models.response_models import ResponseStates
from domain.models.recipe_models import NewRecipe
from ui.items.inputs.dough_size_input import DoughSizeInput
from ui.items.inputs.ingredients_pcts_input import IngredientsPctsInputItem
from ui.items.inputs.ingredient_type_combobox import LeaveningAgentFlags
from ui.items.inputs.levain_pcts_input import LevainPctsInputItem
from ui.items.inputs.overview_input import OverviewInputItem
from ui.items.presenters.ingredients_weights_presenter import IngredientsWeightsPresenterItem
from ui.items.presenters.levain_weigts_presenter import LevainWeightsPresenterItem
from ui.base.scrollable_frame import ScrollableFrame
from ui.styles.recipe_styles import header_style, ingredient_style


class CreateBakersPctRecipeFragment(ScrollableFrame):
    def __init__(self, parent, view_model, *args, **kwargs):
        super().__init__(parent, *args, padding="20 20 20 20", **kwargs)
        self.parent = parent
        self.view_model = view_model
        self.rowconfigure(0, minsize=20)
        self.columnconfigure(1, weight=1)
        self.n_ingredients = 0
        self.ingredients = []
        self.n_init_rows = 1
        self.init_constants()
        self.create_content()

    def init_constants(self):
        self.levain_visible = False
        self.row_spacing = 5
        
    def create_content(self):
        ttk.Label(self.scrollable_frame, text='Recipe title: ', style=ingredient_style()).grid(
            row=0, column=0, sticky="nsew", pady=self.row_spacing)
        self.title_entry = ttk.Entry(self.scrollable_frame)
        self.title_entry.grid(row=0, column=1, columnspan=5, sticky="nsew", pady=self.row_spacing)

        ttk.Label(self.scrollable_frame, text='Category: ', style=ingredient_style()).grid(
            row=1, column=0, sticky='news', pady=self.row_spacing)
        self.category_entry = ttk.Entry(self.scrollable_frame)
        self.category_entry.grid(row=1, column=1, columnspan=5, sticky='nsew', pady=self.row_spacing)

        ttk.Label(self.scrollable_frame, text='Description: ', style=ingredient_style()).grid(
            row=2, column=0, sticky='new'
        )
        self.description_entry = ScrolledText(self.scrollable_frame, width=70, height=7)
        self.description_entry.grid(row=2, column=1, columnspan=5, sticky='nsew', pady=self.row_spacing)

        self.add_image_button = ttk.Button(
            self.scrollable_frame, 
            text='Add image', 
            command=self.on_add_image_button_clicked
        )
        self.add_image_button.grid(row=4, column=0, sticky='w', pady=self.row_spacing)
        self.add_image_label = ttk.Label(self.scrollable_frame, text='Default')
        self.add_image_label.grid(row=4, column=1, columnspan=5, sticky='w')

        self.overview_input_frame = OverviewInputItem(
            self.scrollable_frame
        )
        self.overview_input_frame.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=10)

        self.levain_frame = LevainPctsInputItem(self.scrollable_frame)
        self._show_levain_frame()
        
        self.ingredients_frame = IngredientsPctsInputItem(
            self.scrollable_frame, 
            self.on_leavening_agent_changed
            )
        self.ingredients_frame.grid(row=11, column=0, columnspan=6, sticky='nsew', pady=10)
        
        self.dough_size_input = DoughSizeInput(self.scrollable_frame)
        self.dough_size_input.grid(row=12, column=0, columnspan=2, sticky='nsew', pady=10)

        self.button_frame = ttk.Frame(self.scrollable_frame)
        self.show_weights_button = ttk.Button(
            self.button_frame, 
            text='Show weights',
            command=self.on_show_weights_clicked
        )
        self.show_weights_button.grid(row=0, column=0, sticky='new')
        self.save_button = ttk.Button(
            self.button_frame, 
            text='Save recipe',
            command=self.on_save_recipe_clicked
        )
        self.save_button.grid(row=0, column=1, sticky='e', padx=5)
        self.button_frame.grid(row=13, column=0, sticky='new', pady=10)

        self.on_show_weights_clicked()

    def show_weights(self, ingreidents_weights, levain):
        total_dough_weight = 0
        for ingredient in ingreidents_weights:
            total_dough_weight += ingredient.amount
            print(f'{ingredient.name} {ingredient.type_} {ingredient.amount}')
        print(f'total_dough_weight = {total_dough_weight}')
        if levain is not None:
            self.levain_weights_frame = LevainWeightsPresenterItem(self.scrollable_frame, levain)
            self.levain_weights_frame.grid(row=15, column=0, columnspan=6, sticky='nsew', pady=10)
        else:
            try:
                self.levain_weights_frame.grid_forget()
            except:
                print('Failed to hide levain_weights_frame. It might be None.')
        self.ingredients_weights_frame = IngredientsWeightsPresenterItem(
            self.scrollable_frame,
            ingreidents_weights
        )
        self.ingredients_weights_frame.grid(row=16, column=0, columnspan=2, sticky='nsew', pady=10)

    def on_leavening_agent_changed(self, flag, *data):
        print('on_leavening_agent_changed!')
        print(f'*data = {data}')
        if flag == LeaveningAgentFlags.levain_added or flag == LeaveningAgentFlags.levain_updated:
            self.overview_input_frame.update_leavening_agent(IngredientTypes.levain, *data)
            self._show_levain_frame()
            if not self.ingredients_frame.contains_ingredient_with_type(IngredientTypes.yeast):
                # The yeast might have been replaced by levain. Make sure yeast pct is 0 in overview.
                self.overview_input_frame.update_leavening_agent(IngredientTypes.yeast, 0)
        elif flag == LeaveningAgentFlags.levain_removed:
            self.overview_input_frame.update_leavening_agent(IngredientTypes.levain, 0)
            self._hide_levain_frame()
        elif flag == LeaveningAgentFlags.yeast_added or flag == LeaveningAgentFlags.yeast_updated:
            self.overview_input_frame.update_leavening_agent(IngredientTypes.yeast, *data)
            if not self.ingredients_frame.contains_ingredient_with_type(IngredientTypes.levain):
                # The levain might have been replaced by yeast. Make sure levain pct is 0 in overview.
                self.overview_input_frame.update_leavening_agent(IngredientTypes.levain, 0)
                self._hide_levain_frame()
        elif flag == LeaveningAgentFlags.yeast_removed:
            self.overview_input_frame.update_leavening_agent(IngredientTypes.yeast, 0)

    #     if self.sourdough_recipe_checkbox_var.get() == 0:
    #         print('- Removing sourdough items')
    #         self.overview_input_frame.hide_levain_input()
    #         self._hide_levain_frame()
    #         self.ingredients_frame.hide_levain()
    #     else:
    #         print('- Adding sourdough items')
    #         self.overview_input_frame.show_levain_input()
    #         self._show_levain_frame()
    #         self.ingredients_frame.show_levain()
        
    def on_show_weights_clicked(self, *args):
        print('Show weights button clicked!')
        overview = self.overview_input_frame.get_overview()
        ingredients_pct = self.ingredients_frame.get_ingredients()
        levain = self.levain_frame.get_levain() if self.levain_visible else None
        leavening_agents = self.ingredients_frame.get_leavening_agents()
        self.view_model.compute_recipe_weights(
            self.show_weights,
            self.dough_size_input.get_total_dough_weight(),
            overview,
            ingredients_pct, 
            levain,
            leavening_agents
        )

    def on_save_recipe_clicked(self, *args):
        print('Save recipe button clicked!')
        recipe = self.get_recipe()
        self.view_model.save_recipe(
            self.on_save_recipe_finished,
            recipe
        )

    def on_save_recipe_finished(self, response):
        if response.state == ResponseStates.successful:
            print('Recipe saved!')
            self.parent.show_summary_fragment()
        elif response.state == ResponseStates.error:
            print(f'ERROR during saving of recipe! {response.message}')
            showerror("Error", 
            f'An error occured while saving your recipe! \nMessage:\n {response.message}')
        else:
            print('Did not recognize response state!')

    def get_recipe(self):
        new_recipe = NewRecipe(
            title=self.title_entry.get(),
            category=self.category_entry.get(),
            description=self.description_entry.get("1.0", tk.END),
            image_path='data/local/included/images/sourdough_bread.jpg',
            is_sourdough=self.levain_visible,
            ingredients=self.ingredients_frame.get_ingredients(),
            levain=self.levain_frame.get_levain(),
            overview=self.overview_input_frame.get_overview(),
            dough_size=self.dough_size_input.get_dough_size(),
            leavening_agents=self.ingredients_frame.get_leavening_agents()
        )
        return new_recipe

    def on_add_image_button_clicked(self, *args):
        print('Add image button clicked!')
        # path_to_image = ...
        # self.add_image_label.configure(text=path_to_image)

    def _show_levain_frame(self):
        self.levain_visible = True
        self.levain_frame.grid(row=5, column=1, columnspan=2, sticky='nsew', pady=10)

    def _hide_levain_frame(self):
        self.levain_visible = False
        self.levain_frame.grid_forget()
