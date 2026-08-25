import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NETTECH EMPLOYEE ANALYTICS",
    page_icon=":material/analytics:",
    layout="wide",
    initial_sidebar_state="expanded"
)

theme = st.get_option("theme.base")

if theme == "dark":
    chart_background = "#0F172A"
    chart_text = "#F8FAFC"
    chart_grid = "#475569"
    filter_icon_color = "#CBD5E1"
    royal_blue = "#60A5FA"
else:
    chart_background = "#FFFFFF"
    chart_text = "#1E293B"
    chart_grid = "#CBD5E1"
    filter_icon_color = "#1E3A8A"
    royal_blue = "#1E3A8A"

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        min-width: 250px;
        max-width: 250px;
        border-right: 1px solid rgba(148, 163, 184, 0.35);
    }

    .brand-title {
        font-size: 21px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 4px;
    }

    .brand-subtitle {
        font-size: 12px;
        color: #64748B;
        margin-bottom: 25px;
    }

    .kpi-card {
        background: var(--secondary-background-color);
        color: var(--text-color);
        padding: 18px 12px;
        border-radius: 14px;
        border: 1px solid rgba(148, 163, 184, 0.35);
        text-align: center;
        min-height: 95px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .kpi-title {
        color: var(--text-color);
        font-size: 13px;
        line-height: 1.3;
        margin-bottom: 8px;
    }

    .kpi-value {
        color: #1E3A8A;
        font-size: 26px;
        font-weight: 700;
        line-height: 1.2;
    }

    .section-title {
        font-size: 22px;
        font-weight: 650;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown(
        """
        <div class="brand-title">NETTECH ANALYTICS</div>
        <div class="brand-subtitle">MENU</div>
        """,
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Dashboard",
            "Upload CSV",
            "About"
        ],
        label_visibility="collapsed"
    )

df = pd.read_csv("Employee_Performance_Dataset - Nettech_Employee_Performance_Dataset (1).csv")

def categorize_performance(score):
    if score >= 7:
        return "Excellent"
    elif score >= 6:
        return "Very Good"
    elif score >= 5:
        return "Good"
    elif score >= 4:
        return "Average"
    else:
        return "Needs Improvement"


df["Performance Category"] = df["Performance Score"].apply(
    categorize_performance
)


if page == "Home":
    
    st.title("!!WELCOME!!")
    st.title("\n To The Nettech Employee Dashboard Analytics",)

    st.write(
        "An interactive employee analytics platform to explore "
        "workforce performance, attendance, productivity and salary."
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### :material/groups: Employee Insights")
            st.write(
                "Explore employee performance and workforce metrics "
                "through interactive visualizations."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### :material/dashboard: Interactive Dashboard")
            st.write(
                "Filter employees by department and performance category "
                "to explore detailed insights."
            )

    with col3:
        with st.container(border=True):
            st.markdown("### :material/upload_file: CSV Analysis")
            st.write(
                "Upload an employee dataset and generate an automated "
                "summary and visual analysis that makes the data easier "
                "to understand."
            )

    st.write("")

    st.info(
        "Use the navigation menu on the left to access the Dashboard, "
        "upload a CSV file, or learn more about the project."
    )


elif page == "Dashboard":

    st.title("Employee Performance Dashboard")

    st.write(
        "Explore employee performance, attendance, projects completed "
        "and salary using interactive filters."
    )

    st.markdown(
        "### :material/filter_alt: Filters"
    )

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        selected_department = st.selectbox(
            "Department",
            ["All Departments"] +
            sorted(df["Department"].unique().tolist())
        )

    with filter_col2:
        selected_category = st.selectbox(
            "Performance Category",
            ["All Categories"] +
            sorted(df["Performance Category"].unique().tolist())
        )

    filtered_df = df.copy()

    if selected_department != "All Departments":
        filtered_df = filtered_df[
            filtered_df["Department"] == selected_department
        ]

    if selected_category != "All Categories":
        filtered_df = filtered_df[
            filtered_df["Performance Category"] == selected_category
        ]

    total_employees = len(filtered_df)

    average_attendance = (
        filtered_df["Attendance %"].mean()
        if len(filtered_df) > 0
        else 0
    )

    average_performance = (
        filtered_df["Performance Score"].mean()
        if len(filtered_df) > 0
        else 0
    )

    average_salary = (
        filtered_df["Salary"].mean()
        if len(filtered_df) > 0
        else 0
    )

    total_projects = (
        filtered_df["Projects Completed"].sum()
        if len(filtered_df) > 0
        else 0
    )

    st.write("")

    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

    with kpi_col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Total Employees</div>
                <div class="kpi-value">{total_employees}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi_col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Average Attendance</div>
                <div class="kpi-value">{average_attendance:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi_col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Average Performance</div>
                <div class="kpi-value">{average_performance:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    kpi_col4, kpi_col5 = st.columns(2)

    with kpi_col4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Average Salary</div>
                <div class="kpi-value">₹{average_salary:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi_col5:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Total Projects</div>
                <div class="kpi-value">{total_projects:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.markdown("### :material/bar_chart: Department Analysis")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        with st.container(border=True):

            st.markdown("#### :material/groups: Employee Distribution")

            department_counts = filtered_df["Department"].value_counts()

            fig, ax = plt.subplots(figsize=(4.2, 2.6))

            fig.patch.set_facecolor(chart_background)
            ax.set_facecolor(chart_background)

            department_counts.plot(
                kind="bar",
                ax=ax,
                color=royal_blue,
                width=0.62
            )

            ax.set_xlabel(
                "Department",
                color=chart_text,
                fontsize=9
            )

            ax.set_ylabel(
                "Employees",
                color=chart_text,
                fontsize=9
            )

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=8
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=8
            )

            for spine in ax.spines.values():
                spine.set_color(chart_grid)

            fig.tight_layout(pad=0.7)

            st.pyplot(fig, width="content")

            plt.close(fig)

    with chart_col2:
        with st.container(border=True):

            st.markdown(
                "#### :material/analytics: Department Performance"
            )

            avg_performance_department = (
                filtered_df
                .groupby("Department")["Performance Score"]
                .mean()
                .sort_values(ascending=False)
            )

            fig, ax = plt.subplots(figsize=(4.2, 2.6))

            fig.patch.set_facecolor(chart_background)
            ax.set_facecolor(chart_background)

            avg_performance_department.plot(
                kind="bar",
                ax=ax,
                color=royal_blue,
                width=0.62
            )

            ax.set_xlabel(
                "Department",
                color=chart_text,
                fontsize=9
            )

            ax.set_ylabel(
                "Performance Score",
                color=chart_text,
                fontsize=9
            )

            ax.set_ylim(0, 10)

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=8
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=8
            )

            for spine in ax.spines.values():
                spine.set_color(chart_grid)

            fig.tight_layout(pad=0.7)

            st.pyplot(fig, width="content")

            plt.close(fig)

    st.write("")

    analysis_col1, analysis_col2 = st.columns(2)

    with analysis_col1:
        with st.container(border=True):

            st.markdown(
                "#### :material/donut_large: Performance Distribution"
            )

            category_counts = (
                filtered_df["Performance Category"]
                .value_counts()
            )

            fig, ax = plt.subplots(figsize=(4.2, 2.6))

            fig.patch.set_facecolor(chart_background)
            ax.set_facecolor(chart_background)

            ax.pie(
                category_counts.values,
                labels=category_counts.index,
                autopct="%1.1f%%",
                startangle=90,
                radius=0.82,
                wedgeprops={
                    "edgecolor": chart_background,
                    "linewidth": 0.6
                },
                textprops={
                    "fontsize": 8,
                    "color": chart_text
                }
            )

            ax.set_aspect("equal")

            fig.tight_layout(pad=0.4)

            st.pyplot(fig, width="content")

            plt.close(fig)

    with analysis_col2:
        with st.container(border=True):

            st.markdown(
                "#### :material/emoji_events: Top 10 Performers"
            )

            top_performers = (
                filtered_df
                .sort_values(
                    "Performance Score",
                    ascending=False
                )
                .head(10)
            )

            st.dataframe(
                top_performers[
                    [
                        "Employee Name",
                        "Department",
                        "Performance Score",
                        "Performance Category"
                    ]
                ],
                use_container_width=True,
                hide_index=True,
                height=220
            )

    st.write("")
    st.markdown("### :material/compare_arrows: Performance Relationships")

    relation_col1, relation_col2 = st.columns(2)

    with relation_col1:
        with st.container(border=True):

            st.markdown(
                "#### :material/event_available: Attendance vs Performance"
            )

            fig, ax = plt.subplots(figsize=(4.2, 2.6))

            fig.patch.set_facecolor(chart_background)
            ax.set_facecolor(chart_background)

            ax.scatter(
                filtered_df["Attendance %"],
                filtered_df["Performance Score"],
                color=royal_blue,
                alpha=0.7,
                s=28
            )

            ax.set_xlabel(
                "Attendance %",
                color=chart_text,
                fontsize=9
            )

            ax.set_ylabel(
                "Performance Score",
                color=chart_text,
                fontsize=9
            )

            ax.set_ylim(0, 10)

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=8
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=8
            )

            for spine in ax.spines.values():
                spine.set_color(chart_grid)

            fig.tight_layout(pad=0.7)

            st.pyplot(fig, width="content")

            plt.close(fig)

    with relation_col2:
        with st.container(border=True):

            st.markdown(
                "#### :material/task_alt: Projects vs Performance"
            )

            fig, ax = plt.subplots(figsize=(4.2, 2.6))

            fig.patch.set_facecolor(chart_background)
            ax.set_facecolor(chart_background)

            ax.scatter(
                filtered_df["Projects Completed"],
                filtered_df["Performance Score"],
                color=royal_blue,
                alpha=0.7,
                s=28
            )

            ax.set_xlabel(
                "Projects Completed",
                color=chart_text,
                fontsize=9
            )

            ax.set_ylabel(
                "Performance Score",
                color=chart_text,
                fontsize=9
            )

            ax.set_ylim(0, 10)

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=8
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=8
            )

            for spine in ax.spines.values():
                spine.set_color(chart_grid)

            fig.tight_layout(pad=0.7)

            st.pyplot(fig, width="content")

            plt.close(fig)


elif page == "Upload CSV":

    st.title("Upload Employee Dataset")

    st.write(
        "Upload a CSV file to generate an automatic summary "
        
    )

    st.markdown(
        "### :material/upload_file: Upload CSV File"
    )

    uploaded_file = st.file_uploader(
        "Choose & Upload a CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        uploaded_df = pd.read_csv(uploaded_file)

        st.success("CSV file uploaded successfully.")

        st.markdown(
            "### :material/description: Dataset Overview"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Rows",
                len(uploaded_df)
            )

        with col2:
            st.metric(
                "Columns",
                len(uploaded_df.columns)
            )

        with col3:
            st.metric(
                "Missing Values",
                int(uploaded_df.isnull().sum().sum())
            )

        st.write("")

        st.markdown(
            "### :material/table_view: Data Preview"
        )

        st.dataframe(
            uploaded_df.head(10),
            use_container_width=True,
            hide_index=True
        )


        numeric_columns = uploaded_df.select_dtypes(
            include=np.number
        ).columns

        if len(numeric_columns) > 0:

            summary = uploaded_df[numeric_columns].describe().T

            st.dataframe(
                summary,
                use_container_width=True
            )

        
        
elif page == "About":

    st.title("About Nettech Employee Analytics")

    st.write(
        "Nettech Employee Analytics is an interactive Python-based "
        "dashboard designed to analyze employee performance and "
        "workforce-related metrics."
    )

    st.markdown(
        "### :material/flag: Project Objective"
    )

    st.write(
        "The project aims to transform employee data into meaningful "
        "visual insights that can support performance analysis and "
        "workforce decision-making."
    )

    st.markdown(
        "### :material/code: Technology"
    )

    st.write(
        "Python, Pandas, NumPy, Matplotlib(for visualizations) and Streamlit"
    )

    st.markdown(
        "### :material/analytics: Key Analysis Areas"
    )

    st.write(
        "Employee distribution, attendance, performance, projects "
        "completed, salary and performance."
    )

    st.markdown(
        "### :material/dashboard: Dashboard Features"
    )

    st.write(
        "Interactive filtering, KPI cards, data visualizations, "
        "top-performer analysis."
        "Charts like Bar chart,pie chart,scatter plot chart is used."
    )
    
    st.markdown(
        "### :material/create: CREATED BY:"
    )

    st.write(
        "Miss.Riya Bhosle ,"
        "NetTech-India Data-analyst Intern."
    )

    st.markdown(
        "### :material/extra:NOTE:"
    )
    st.write(
        "THE DATASET USED IN THIS PROJECT TO MAKE THE DASHBOARD IS CREATED BY VARIOUS SOURCES AND IS NOT THE ACTUAL DATA"
    )
