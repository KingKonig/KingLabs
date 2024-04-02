import os
import streamlit as st
from modules import kingfiles, kingfunction, kingdatagenerator


if __name__ == "__main__":
    graph = False
    plot_type = ""
    post_processor = ""
    processor_arguments = ""

    with st.sidebar:
        # Uploader
        with st.expander("Upload"):
            uploaded_files = st.file_uploader("Upload a CSV", type="csv", accept_multiple_files=True)

            # load data
            data = kingfiles.file_processor(uploaded_files, interpolate=False, export=False)

        # Plot tab
        with st.expander("Plot"):
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

                # Choose bounds
                bounds = st.slider(
                    "Crop Data:",
                    0,
                    data.shape[0],
                    (0, data.shape[0])
                )
                data = data[bounds[0]:bounds[1]]
                data = data.reset_index()

                # Processor arguments
                if post_processor == "Moving Average":
                    processor_arguments = tuple((st.slider("N for moving average:", 2, 100, 2, 1),))

                elif post_processor == "Lowpass":
                    freq_cutoff = st.slider("Frequency cutoff (hz):", 1, 100, 1, 1)
                    order = st.slider("Filter order:", 1, 10, 4, 1)
                    processor_arguments = freq_cutoff, order

                elif post_processor == "FFT":
                    processor_arguments = st.slider("Frequency Range:", 0, 100, (1, 20), 1)

                # Quality slider
                dpi = st.slider("Plot DPI:", 10, 600, 100, 10)

            else:
                st.write("Please upload a file first.")

        # data Generator tab
        with st.expander("Generate"):
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
                gen_data, fig = kingdatagenerator.express_gen(
                    gen_ex,
                    gen_min,
                    gen_max,
                    gen_n,
                    gen_type,
                    gen_label
                )

                # Show plot
            if submitted:
                st.pyplot(fig)

            # with col_download:
            # Save to nameable csv
            with st.form("Download"):
                filepath = os.getcwd() + "/data/" + gen_label + ".csv"

                if st.form_submit_button("Download"):
                    gen_data.to_csv(filepath, index=False)

    # Plot the data when an update occurs
    with st.spinner("Matplotlib is thinking really hard..."):
        if uploaded_files:
            st.pyplot(kingfunction.auto_plot(data, plot_type, post_processor, processor_arguments), dpi=dpi)
