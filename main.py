import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to The Jaybrary! 👋")

    st.sidebar.success("Select a tool above.")

    st.markdown(
        """
        Your central hub for data automation!\n\n
        Say goodbye to repetitive tasks and hello to efficiency.\n\n 
        The Jaybrary brings Benefitmall's custom-built automation tools into one convenient app, to make your workflows faster, and easier.\n\n
        
        If you have an automation request, or a tool you would like to see in the Jaybrary,\n\n
        Please email: jethro.bizumuremyi@benefitmall.com\n\n
         
        **👈 Select an app from the sidebar!** 
    """
    )


if __name__ == "__main__":
    run()
