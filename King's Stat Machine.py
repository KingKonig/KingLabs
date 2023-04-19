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
        # col_param, col_download = st.columns(2)

        # with col_param:
        # Set params
        with st.form("Generation Parameters"):
            st.write("Generation Parameters")

            gen_type = st.checkbox("Scatter-plot")
            gen_label = st.text_input("Data label:", value="Data")
            gen_ex = st.text_input("Expression (python):", value="x")
            gen_min = int(st.text_input("Minimum:", value=0))
            gen_max = int(st.text_input("Maximum", value=1))
            gen_n = int(st.text_input("n points", value=10))

            submitted = st.form_submit_button("Generate")

            if submitted:
                st.write(f"f(x) = {gen_ex}, starting at {gen_min} and ending at {gen_max}.")

            # Send to generator
            gen_data, fig = kingdatagen.express_gen(gen_ex, gen_min, gen_max, gen_n, gen_type, gen_label)

            # Show plot
        if submitted:
            st.pyplot(fig)

        # with col_download:
        # Save to nameable csv
        with st.form("Download"):
            filepath = (os.getcwd() + "/data/" + gen_label + ".csv")

            if st.form_submit_button("Download"):
                gen_data.to_csv(filepath, index=False)

    # Plot tab
    with tab_plot:
        # load data
        data = kingfiles.file_processor(uploaded_files, interpolate=False, export=True)
        # Vars for crop
        # start = -9
        # end = 9
        # data = kingfunky.na_dropper(data, threshold=1, export=True)
        # data = kingfunky.data_cropper(data, start, end)

        if uploaded_files:
            processor_arguments = tuple
            # Graph Type Drop Down
            plot_type = st.selectbox(
                "Plot Style:",
                ("Line", "Scatter")
            )

            # Data processing drop down
            post_processor = st.selectbox(
                "Data Post-Processor:",
                ("None", "Moving Average", "Lowpass", "FFT")
            )

            # Processor arguments
            if post_processor == "Moving Average":
                processor_arguments = tuple((st.slider("N for moving average", 1, 1000, 1, 10),))

            elif post_processor == "Lowpass":
                freq_cutoff = st.slider("Frequency cutoff (hz):", 1, 1000, 1, 10)
                order = st.slider("Filter order:", 1, 10, 4, 1)
                processor_arguments = freq_cutoff, order

            # Graph Button
            if st.button("Display Graphs"):
                # Plot the data
                st.pyplot(kingfunky.auto_plot(data, plot_type, post_processor, processor_arguments))
        else:
            st.write("You need to upload data before trying to plot!")
