from dash import html


def create_layout():

    return html.Div(

        [

            html.H1("Smart Factory Dashboard"),

            html.Hr(),

            html.Div(
                id="factory-content"
            )

        ]

    )