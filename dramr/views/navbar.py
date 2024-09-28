import reflex as rx


def navbar():
    return rx.flex(
        rx.hstack(
            rx.hstack(
                rx.icon(tag="glass-water", size=28),
                rx.heading("dramr", size="6"),
                align_items="center",
            ),
            rx.menu.root(
                rx.menu.trigger(rx.icon("menu", size=30)),
                rx.menu.content(
                    rx.menu.item("Home"),
                    rx.menu.item("About"),
                    rx.menu.separator(),
                    rx.menu.item("Log in"),
                    rx.menu.item("Sign up"),
                ),
                justify="end",
            ),
            justify="between",
            align_items="center",
        ),
        bg=rx.color("accent", 3),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="right",
        width="100%",
        top="0px",
        padding="1em",
    )
