import reflex as rx

def create_hover_link(hover_styles, link_url, link_content):
    """Create a hyperlink with hover effects."""
    return rx.el.a(
        link_content, href=link_url, _hover=hover_styles
    )


def create_overlay():
    """Create a semi-transparent black overlay."""
    return rx.box(
        position="absolute",
        background_color="#000000",
        top="0",
        right="0",
        bottom="0",
        left="0",
        opacity="0.5",
    )


def create_styled_button(
    hover_styles, bg_color, text_color, button_content
):
    """Create a styled button with hover effects and transitions."""
    return rx.el.a(
        button_content,
        href="#contact",
        background_color=bg_color,
        transition_duration="300ms",
        _hover=hover_styles,
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        color=text_color,
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_section_heading(bottom_margin, heading_text):
    """Create a centered section heading with custom bottom margin."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom=bottom_margin,
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_icon(alt_text, icon_name):
    """Create an icon with specified dimensions and bottom margin."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="3rem",
        margin_bottom="1rem",
        width="3rem",
    )


def create_custom_heading(
    heading_level, font_size, bottom_margin, heading_text
):
    """Create a custom heading with specified font size, weight, and bottom margin."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=bottom_margin,
        font_size=font_size,
        line_height="1.75rem",
        as_=heading_level,
    )


def create_text(text_content):
    """Create a simple text element."""
    return rx.text(text_content)


def create_feature_box(
    icon_alt, icon_name, feature_title, feature_description
):
    """Create a feature box with an icon, title, and description."""
    return rx.box(
        create_icon(alt_text=icon_alt, icon_name=icon_name),
        create_custom_heading(
            heading_level="h3",
            font_size="1.25rem",
            bottom_margin="0.5rem",
            heading_text=feature_title,
        ),
        create_text(text_content=feature_description),
        background_color="#F3F4F6",
        padding="1.5rem",
        border_radius="0.5rem",
    )


def create_process_step_circle(step_number):
    """Create a circular element for displaying process step numbers."""
    return rx.flex(
        step_number,
        background_color="#059669",
        display="flex",
        height="4rem",
        align_items="center",
        justify_content="center",
        margin_bottom="1.5rem",
        margin_left="auto",
        margin_right="auto",
        border_radius="9999px",
        color="#ffffff",
        width="4rem",
    )


def create_process_step_box(
    step_number, step_title, step_description
):
    """Create a box displaying a process step with number, title, and description."""
    return rx.box(
        create_process_step_circle(step_number=step_number),
        create_custom_heading(
            heading_level="h3",
            font_size="1.25rem",
            bottom_margin="1rem",
            heading_text=step_title,
        ),
        create_text(text_content=step_description),
        background_color="#ffffff",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        text_align="center",
        width=rx.breakpoints(
            {"0px": "100%", "768px": "33.333333%"}
        ),
    )


def create_small_icon(alt_text, icon_name):
    """Create a small icon with right margin."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="1.25rem",
        margin_right="0.5rem",
        width="1.25rem",
    )


def create_text_span(span_content):
    """Create a text span element."""
    return rx.text.span(span_content)


def create_icon_text(icon_alt, icon_name, text_content):
    """Create a flex container with an icon and text."""
    return rx.text(
        create_small_icon(
            alt_text=icon_alt, icon_name=icon_name
        ),
        create_text_span(span_content=text_content),
        display="flex",
        align_items="center",
        justify_content="center",
        margin_bottom="0.5rem",
    )


def create_medium_icon(alt_text, icon_name):
    """Create a medium-sized icon."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="1.5rem",
        width="1.5rem",
    )


def create_social_link(hover_styles, icon_alt, icon_name):
    """Create a social media link with an icon and hover effect."""
    return rx.el.a(
        create_medium_icon(
            alt_text=icon_alt, icon_name=icon_name
        ),
        href="#",
        _hover=hover_styles,
    )


def create_nav_item(link_url, link_text):
    """Create a navigation item with a hover effect."""
    return rx.el.li(
        create_hover_link(
            hover_styles={"color": "#34D399"},
            link_url=link_url,
            link_content=link_text,
        )
    )


def create_header():
    """Create the main header with logo and navigation items."""
    return rx.flex(
        rx.el.a(
            "ServicePro",
            href="#",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            color="#059669",
        ),
        rx.box(
            create_hover_link(
                hover_styles={"color": "#059669"},
                link_url="#welcome",
                link_content="Inicio",
            ),
            create_hover_link(
                hover_styles={"color": "#059669"},
                link_url="#services",
                link_content="Servicios",
            ),
            create_hover_link(
                hover_styles={"color": "#059669"},
                link_url="#process",
                link_content="Proceso",
            ),
            create_hover_link(
                hover_styles={"color": "#059669"},
                link_url="#contact",
                link_content="Contacto",
            ),
            display=rx.breakpoints(
                {"0px": "none", "768px": "flex"}
            ),
            column_gap="1.5rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )


def create_sticky_header():
    """Create a sticky header with responsive styling."""
    return rx.box(
        rx.box(
            create_header(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
            padding_top="0.75rem",
            padding_bottom="0.75rem",
        ),
        background_color="#ffffff",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        position="sticky",
        width="100%",
        z_index="10",
    )


def create_hero_content():
    """Create the hero section content with title, subtitle, and CTA button."""
    return rx.box(
        rx.heading(
            "Bienvenido a ServicePro",
            font_weight="700",
            margin_bottom="1rem",
            font_size="3rem",
            line_height="1",
            color="#ffffff",
            as_="h1",
        ),
        rx.text(
            "Soluciones innovadoras para las necesidades de tu negocio",
            margin_bottom="2rem",
            color="#ffffff",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_styled_button(
            hover_styles={"background-color": "#047857"},
            bg_color="#059669",
            text_color="#ffffff",
            button_content="Empezar",
        ),
        position="relative",
        text_align="center",
        z_index="10",
    )


def create_hero_section():
    """Create the full hero section with background image and overlay."""
    return rx.flex(
        create_overlay(),
        create_hero_content(),
        class_name="h-[50vh]",
        id="welcome",
        background_image="url('https://images.pexels.com/photos/130621/pexels-photo-130621.jpeg')",
        background_position="center",
        background_size="cover",
        display="flex",
        align_items="center",
        justify_content="center",
        position="relative",
    )


def create_services_section():
    """Create the services section with title and feature boxes."""
    return rx.box(
        create_section_heading(
            bottom_margin="2rem",
            heading_text="Nuestros Servicios",
        ),
        rx.box(
            create_feature_box(
                icon_alt="Icono de Analítica",
                icon_name="bar-chart",
                feature_title="Analítica de Datos",
                feature_description="Desbloquea insights de tus datos para impulsar el crecimiento del negocio.",
            ),
            create_feature_box(
                icon_alt="Icono de Desarrollo",
                icon_name="code",
                feature_title="Desarrollo Web",
                feature_description="Crea sitios web impresionantes y responsivos adaptados a tus necesidades.",
            ),
            create_feature_box(
                icon_alt="Icono de Marketing",
                icon_name="target",
                feature_title="Marketing Digital",
                feature_description="Aumenta tu presencia en línea y alcanza a tu audiencia objetivo.",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_process_section():
    """Create the process section with title and step boxes."""
    return rx.box(
        create_section_heading(
            bottom_margin="3rem",
            heading_text="Cómo lo Hacemos",
        ),
        rx.flex(
            create_process_step_box(
                step_number="1",
                step_title="Consulta",
                step_description="Discutimos tus necesidades y objetivos para entender tu visión.",
            ),
            create_process_step_box(
                step_number="2",
                step_title="Ejecución",
                step_description="Implementamos la solución con precisión y cuidado.",
            ),
            create_process_step_box(
                step_number="3",
                step_title="Revisión",
                step_description="Analizamos y optimizamos los resultados para una mejora continua.",
            ),
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "768px": "row"}
            ),
            align_items="center",
            justify_content="space-between",
            gap=rx.breakpoints(
                {"0px": "2rem", "768px": "0"}
            ),
            column_gap=rx.breakpoints({"768px": "2rem"}),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_social_links():
    """Create a section with social media links."""
    return rx.box(
        create_custom_heading(
            heading_level="h4",
            font_size="1.125rem",
            bottom_margin="0.5rem",
            heading_text="Síguenos",
        ),
        rx.flex(
            create_social_link(
                hover_styles={"color": "#059669"},
                icon_alt="Facebook",
                icon_name="facebook",
            ),
            create_social_link(
                hover_styles={"color": "#059669"},
                icon_alt="Twitter",
                icon_name="twitter",
            ),
            create_social_link(
                hover_styles={"color": "#059669"},
                icon_alt="Instagram",
                icon_name="instagram",
            ),
            create_social_link(
                hover_styles={"color": "#059669"},
                icon_alt="LinkedIn",
                icon_name="linkedin",
            ),
            display="flex",
            justify_content="center",
            column_gap="1rem",
        ),
        margin_top="1.5rem",
    )


def create_contact_info():
    """Create a contact information section with email, phone, and website."""
    return rx.flex(
        rx.box(
            create_custom_heading(
                heading_level="h3",
                font_size="1.25rem",
                bottom_margin="1rem",
                heading_text="Ponte en Contacto",
            ),
            create_icon_text(
                icon_alt="Email",
                icon_name="mail",
                text_content="info@servicepro.com",
            ),
            create_icon_text(
                icon_alt="Teléfono",
                icon_name="phone",
                text_content="+1 (123) 456-7890",
            ),
            create_icon_text(
                icon_alt="Sitio Web",
                icon_name="globe",
                text_content="www.servicepro.com",
            ),
            create_social_links(),
            text_align="center",
        ),
        display="flex",
        flex_direction="column",
        align_items="center",
    )


def create_contact_section():
    """Create the full contact section with title and contact information."""
    return rx.box(
        rx.box(
            create_section_heading(
                bottom_margin="3rem",
                heading_text="Contáctanos",
            ),
            create_contact_info(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
        ),
        id="contact",
        background_color="#ffffff",
        padding_top="5rem",
        padding_bottom="5rem",
    )


def create_cta_section():
    """Create a call-to-action section with title, subtitle, and button."""
    return rx.box(
        rx.heading(
            "¿Listo para empezar?",
            font_weight="700",
            margin_bottom="1rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        rx.text(
            "Transformemos tu negocio juntos",
            margin_bottom="2rem",
        ),
        create_styled_button(
            hover_styles={"background-color": "#F3F4F6"},
            bg_color="#ffffff",
            text_color="#059669",
            button_content="Contáctanos Ahora",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        position="relative",
        text_align="center",
        z_index="10",
    )


def create_main_content():
    """Create the main content of the page, including all sections."""
    return rx.box(
        create_hero_section(),
        rx.box(
            create_services_section(),
            id="services",
            background_color="#ffffff",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_process_section(),
            id="process",
            background_color="#F3F4F6",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        create_contact_section(),
        rx.box(
            create_overlay(),
            create_cta_section(),
            background_image="url('https://images.pexels.com/photos/130621/pexels-photo-130621.jpeg')",
            background_position="center",
            background_size="cover",
            padding_top="5rem",
            padding_bottom="5rem",
            position="relative",
            color="#ffffff",
        ),
    )


def create_footer_branding():
    """Create the branding section for the footer."""
    return rx.box(
        rx.heading(
            "ServicePro",
            font_weight="700",
            margin_bottom="0.5rem",
            font_size="1.5rem",
            line_height="2rem",
            as_="h3",
        ),
        create_text(
            text_content="Soluciones innovadoras para las necesidades de tu negocio"
        ),
        margin_bottom=rx.breakpoints(
            {"0px": "1.5rem", "768px": "0"}
        ),
        width=rx.breakpoints(
            {"0px": "100%", "768px": "33.333333%"}
        ),
    )


def create_footer_content():
    """Create the main content of the footer, including branding, quick links, and social links."""
    return rx.flex(
        create_footer_branding(),
        rx.box(
            create_custom_heading(
                heading_level="h4",
                font_size="1.125rem",
                bottom_margin="1rem",
                heading_text="Enlaces Rápidos",
            ),
            rx.list(
                create_nav_item(
                    link_url="#welcome", link_text="Inicio"
                ),
                create_nav_item(
                    link_url="#services",
                    link_text="Servicios",
                ),
                create_nav_item(
                    link_url="#process", link_text="Proceso"
                ),
                create_nav_item(
                    link_url="#contact",
                    link_text="Contacto",
                ),
            ),
            margin_bottom=rx.breakpoints(
                {"0px": "1.5rem", "768px": "0"}
            ),
            width=rx.breakpoints(
                {"0px": "100%", "768px": "33.333333%"}
            ),
        ),
        rx.box(
            create_custom_heading(
                heading_level="h4",
                font_size="1.125rem",
                bottom_margin="1rem",
                heading_text="Síguenos",
            ),
            rx.flex(
                create_social_link(
                    hover_styles={"color": "#34D399"},
                    icon_alt="Facebook",
                    icon_name="facebook",
                ),
                create_social_link(
                    hover_styles={"color": "#34D399"},
                    icon_alt="Twitter",
                    icon_name="twitter",
                ),
                create_social_link(
                    hover_styles={"color": "#34D399"},
                    icon_alt="Instagram",
                    icon_name="instagram",
                ),
                create_social_link(
                    hover_styles={"color": "#34D399"},
                    icon_alt="LinkedIn",
                    icon_name="linkedin",
                ),
                display="flex",
                column_gap="1rem",
            ),
            width=rx.breakpoints(
                {"0px": "100%", "768px": "33.333333%"}
            ),
        ),
        display="flex",
        flex_wrap="wrap",
        align_items="center",
        justify_content="space-between",
    )


def create_footer():
    """Create the full footer section with content and copyright notice."""
    return rx.box(
        create_footer_content(),
        rx.box(
            create_text(
                text_content="© 2023 ServicePro. Todos los derechos reservados."
            ),
            border_color="#374151",
            border_top_width="1px",
            margin_top="2rem",
            padding_top="2rem",
            text_align="center",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_page_layout():
    """Create the overall page layout, including header, main content, and footer."""
    return rx.box(
        create_sticky_header(),
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="2rem",
            padding_bottom="2rem",
            color="#ffffff",
        ),
        background_color="#ffffff",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        color="#000000",
    )


def create_page():
    """Create the complete page with necessary styles and layout."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        create_page_layout(),
    )