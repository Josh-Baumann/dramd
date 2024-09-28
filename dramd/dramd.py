"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .views.navbar import navbar
from .views.sidebar import sidebar_bottom_profile


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.box(
            rx.hstack(
                sidebar_bottom_profile(),
                rx.hstack(
                    rx.badge(
                        rx.icon(tag="glass-water", size=28),
                        rx.heading(
                            "dramd",
                            size="6",
                            justify="end",
                        ),
                        variant="surface",
                        radius="large",
                    ),
                    padding="0.5rem",
                ),
                align_items="center",
                width="100%",
                justify="between",
            ),
            bg=rx.color("accent", 3),
            width="100%",
        ),
        rx.container(
            rx.vstack(
                rx.heading("Welcome to dramd!", size="9"),
                rx.text(
                    "Get started by editing ",
                    rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                rx.link(
                    rx.button("Check out our docs!"),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True,
                ),
                spacing="5",
                justify="top",
                min_height="85vh",
            ),
        ),
    )


app = rx.App(theme=rx.theme(appearance="dark", accent_color="purple"))
app.add_page(index)
