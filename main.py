import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class NPVApp(App):
    def build(self):
        self.title = 'NPV Calculator'
        layout = BoxLayout(orientation='vertical')

        # Input for Initial Investment
        self.initial_investment_input = TextInput(hint_text='Initial Investment', multiline=False)
        layout.add_widget(self.initial_investment_input)

        # Input for Cash Flows
        self.cash_flows_input = TextInput(hint_text='Cash Flows (comma separated)', multiline=False)
        layout.add_widget(self.cash_flows_input)

        # Input for Discount Rate
        self.discount_rate_input = TextInput(hint_text='Discount Rate', multiline=False)
        layout.add_widget(self.discount_rate_input)

        # Button to Calculate NPV
        calculate_button = Button(text='Calculate NPV')
        calculate_button.bind(on_press=self.calculate_npv)
        layout.add_widget(calculate_button)

        # Label to display the result
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)

        return layout

    def calculate_npv(self, instance):
        initial_investment = float(self.initial_investment_input.text)
        cash_flows = list(map(float, self.cash_flows_input.text.split(',')))
        discount_rate = float(self.discount_rate_input.text)
        
        npv = self.calculate_npv_value(initial_investment, cash_flows, discount_rate)
        self.result_label.text = f'NPV: {npv}'

    def calculate_npv_value(self, initial_investment, cash_flows, discount_rate):
        npv = -initial_investment
        for i, cash_flow in enumerate(cash_flows):
            npv += cash_flow / ((1 + discount_rate) ** (i + 1))
        return npv

if __name__ == '__main__':
    NPVApp().run()
