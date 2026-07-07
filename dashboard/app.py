from dash import Dash
import dash_bootstrap_components as dbc

from dashboard.layout import create_layout

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY]
)

app.layout = create_layout()

if __name__ == "__main__":
    app.run(debug=True)