# Imports
from modules import kingfiles, kingstats, kingfunky, kingdatagen
import streamlit as st
import os


if __name__ == "__main__":
    # Setup tabs
    tab_upload, tab_generate, tab_plot = st.tabs(["Upload", "Data Generator", "Plot"])

    # Upload tab
    with tab_upload:
        uploaded_files = st.file_uploader("Upload a CSV", type="csv", accept_multiple_files=True)

    # data Generator tab
    with tab_generate:
        col_param, col_download = st.columns(2)

        with col_param:
            # Set params
            with st.form("Generation Parameters"):
                st.write("Generation Parameters")

                gen_type = st.checkbox("Scatter-plot")
                gen_ex = st.text_input("Expression (python):")
                gen_min = int(st.text_input("Minimum:", value=0))
                gen_max = int(st.text_input("Maximum", value=1))
                gen_n = int(st.text_input("n Points", value=10))

                submitted = st.form_submit_button("Generate")

                if submitted:
                    st.write(f"f(x) = {gen_ex}, starting at {gen_min} and ending at {gen_max}.")

            # Send to generator
            gen_data, fig = kingdatagen.express_gen(gen_ex, gen_min, gen_max, gen_n, gen_type)

            # Show plot
        if submitted:
            st.pyplot(fig)

        with col_download:
            # Save to nameable csv
            with st.form("Download"):
                file_name = st.text_input("File name (don't forget the .csv):")
                filepath = (os.getcwd() + "/data/" + file_name)

                if st.form_submit_button("Download"):
                    gen_data.to_csv(filepath, index=False)

    # Plot tab
    with tab_plot:
        if uploaded_files:
            if st.button("Display Graphs"):
                # Vars for crop
                start = 0
                end = 100

                # data processing
                data = kingfiles.file_processor(uploaded_files, export=True)
                data = kingfunky.na_dropper(data, threshold=100, export=True)

                # Plot the data
                st.pyplot(kingfunky.auto_plot(data))
        else:
            st.write("You need to upload data before trying to plot!")
