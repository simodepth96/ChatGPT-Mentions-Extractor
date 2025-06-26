import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="ChatGPT Mentions & Traffic Referrals Analysis",
    layout="wide"
)

# App title and description
st.title("ChatGPT Mentions & Traffic Referrals Analysis")
st.markdown("Upload your Excel file and analyze brand mentions across different sources")

# Sidebar for inputs
st.sidebar.header("Configuration")

# File upload
uploaded_file = st.sidebar.file_uploader(
    "Upload Excel file",
    type=['xlsx', 'xls'],
    help="Upload your Excel file containing the data to analyze"
)

# Brand search input
brand_search = st.sidebar.text_input(
    "Brand to search for",
    help="Enter the brand/domain you want to search for in the 'additional info' column"
)

# Color scheme selection
color_scheme = st.sidebar.selectbox(
    "Color scheme for heatmap",
    ["Viridis", "Blues", "Reds", "Greens", "Plasma", "Inferno", "Cividis"],
    index=0
)

# Process data when file is uploaded
if uploaded_file is not None:
    try:
        with st.spinner("Loading data..."):
            df = pd.read_excel(uploaded_file)
            df.columns = df.columns.str.lower()

        if 'additional info' not in df.columns:
            st.error("❌ Column 'additional info' not found in the uploaded file. Please check your data.")
            st.write("Available columns:", list(df.columns))
        else:
            with st.spinner("Processing data..."):
                df['brand mentions'] = df['additional info'].astype(str).str.contains(
                    brand_search, case=False, na=False
                ).map({True: 'Yes', False: 'No'})

                col_str = df['additional info'].astype(str).str.lower()
                conditions = [
                    col_str.str.contains('youtube.com', na=False),
                    col_str.str.contains('facebook.com', na=False),
                    col_str.str.contains('instagram.com', na=False),
                    col_str.str.contains('reddit.com', na=False),
                    col_str.str.contains('quora.com', na=False),
                    col_str.str.contains('wikipedia.org', na=False),
                    col_str.str.contains('tiktok.com', na=False)
                ]
                choices = ['YouTube', 'Facebook', 'Instagram', 'Reddit', 'Quora', 'Wikipedia', 'TikTok']
                df['source mention'] = np.select(conditions, choices, default='Organic')

            col1, col2 = st.columns([2, 1])

            with col1:
                st.subheader("📈 Brand Mentions vs Source Mentions Heatmap")
                heatmap_data = pd.crosstab(df['source mention'], df['brand mentions'])
                fig = go.Figure(data=go.Heatmap(
                    z=heatmap_data.values,
                    x=heatmap_data.columns,
                    y=heatmap_data.index,
                    colorscale=color_scheme,
                    text=heatmap_data.values,
                    texttemplate="%{text}",
                    textfont={"size": 12},
                    hoverongaps=False,
                    hovertemplate='<b>Source:</b> %{y}<br>' +
                                  '<b>Brand Mention:</b> %{x}<br>' +
                                  '<b>Count:</b> %{z}<br>' +
                                  '<extra></extra>'
                ))
                fig.update_layout(
                    xaxis_title=f'Brand Mentions ({brand_search})',
                    yaxis_title='Source Mentions',
                    height=500,
                    font=dict(size=11)
                )
                st.plotly_chart(fig, use_container_width=True)

            col_stats, col_chart = st.columns([1, 1])

            with col_stats:
                st.subheader("📊 Summary Statistics")
                total_records = len(df)
                brand_mentions_yes = len(df[df['brand mentions'] == 'Yes'])
                brand_mentions_no = len(df[df['brand mentions'] == 'No'])
                brand_mention_rate = (brand_mentions_yes / total_records * 100) if total_records > 0 else 0
                st.metric("Total Records", total_records)
                st.metric("Brand Mentions (Yes)", brand_mentions_yes)
                st.metric("Brand Mentions (No)", brand_mentions_no)
                st.metric("Brand Mention Rate", f"{brand_mention_rate:.1f}%")

            with col_chart:
                st.subheader("📱 Source Distribution")
                source_counts = df['source mention'].value_counts()
                fig_pie = px.pie(
                    values=source_counts.values,
                    names=source_counts.index,
                    title="Distribution by Source"
                )
                fig_pie.update_layout(height=400, font=dict(size=10))
                st.plotly_chart(fig_pie, use_container_width=True)

            st.subheader("📋 Data Overview")
            tab1, tab2, tab3 = st.tabs(["Raw Data Preview", "Crosstab Results", "Source Breakdown"])

            with tab1:
                st.write("**First rows of processed data:**")
                display_cols = ['additional info', 'brand mentions', 'source mention']
                available_cols = [col for col in display_cols if col in df.columns]
                st.dataframe(df[available_cols].head(50), use_container_width=True)

            with tab2:
                st.write("**Crosstab: Brand Mentions vs Source Mentions**")
                st.dataframe(heatmap_data, use_container_width=True)

            with tab3:
                st.write("**Detailed Source Breakdown**")
                breakdown_df = df.groupby(['source mention', 'brand mentions']).size().reset_index(name='count')
                breakdown_pivot = breakdown_df.pivot(index='source mention', columns='brand mentions', values='count').fillna(0)
                breakdown_pivot['Total'] = breakdown_pivot.sum(axis=1)
                breakdown_pivot = breakdown_pivot.sort_values('Total', ascending=False)
                st.dataframe(breakdown_pivot, use_container_width=True)

            st.subheader("💾 Download Processed Data")
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="Download processed data as CSV",
                data=csv_data,
                file_name=f"processed_data_{brand_search.replace('.', '_')}.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")
        st.write("Please check that your file is a valid Excel file with the correct format.")

else:
    st.info("👆 Please upload an Excel file to start the analysis")
    st.markdown("""
    ### Instructions:
    1. **Upload your Excel file** using the file uploader in the sidebar
    2. **Enter the brand/domain** you want to search for 
    3. **Choose a color scheme** for the heatmap visualization
    4. The app will automatically process your data and generate:
       - Interactive heatmap showing brand mentions vs source mentions
       - Summary statistics and metrics
       - Source distribution pie chart
       - Detailed data tables

    ### Required Data Format:
    - Your Excel file should contain a column named **'Prompt'**, **'Content'**, or **'Additional info'**
    - The headers are left unchanged from an export of search queries using the [ for Search Chrome Extension](https://chromewebstore.google.com/detail/-path/kiopibcjdnlpamdcdcnphaajccobkban)

    ### Supported Sources:
    - YouTube, Facebook, Instagram, Reddit, Quora, Wikipedia, TikTok
    - All other sources are categorized as 'Organic'
    """)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by [SEO Depths](https://seodepths.com/)")
