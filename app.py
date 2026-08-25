import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

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

df = pd.read_csv(
    "Employee_Performance_Dataset - Nettech_Employee_Performance_Dataset (1).csv"
)


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
    st.title(
        "\n To The Nettech Employee Dashboard Analytics",
    )

    st.write(
        "An interactive employee analytics platform to explore "
        "workforce performance, attendance, productivity and salary."
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown(
                "### :material/groups: Employee Insights"
            )
            st.write(
                "Explore employee performance and workforce metrics "
                "through interactive visualizations."
            )

    with col2:
        with st.container(border=True):
            st.markdown(
                "### :material/dashboard: Interactive Dashboard"
            )
            st.write(
                "Filter employees by department and performance category "
                "to explore detailed insights."
            )

    with col3:
        with st.container(border=True):
            st.markdown(
                "### :material/upload_file: CSV Analysis"
            )
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

    st.markdown(
        "### :material/download: Export Dashboard Summary"
    )

    dashboard_report = StringIO()

    dashboard_report.write(
        "NETTECH EMPLOYEE ANALYTICS\n"
    )

    dashboard_report.write(
        "DASHBOARD SUMMARY REPORT\n\n"
    )

    dashboard_report.write(
        "Applied Filters\n"
    )

    dashboard_report.write(
        f"Department,{selected_department}\n"
    )

    dashboard_report.write(
        f"Performance Category,{selected_category}\n\n"
    )

    dashboard_report.write(
        "Key Performance Indicators\n"
    )

    dashboard_report.write(
        f"Total Employees,{total_employees}\n"
    )

    dashboard_report.write(
        f"Average Attendance,{average_attendance:.2f}%\n"
    )

    dashboard_report.write(
        f"Average Performance,{average_performance:.2f}\n"
    )

    dashboard_report.write(
        f"Average Salary,₹{average_salary:,.0f}\n"
    )

    dashboard_report.write(
        f"Total Projects,{total_projects:,.0f}\n\n"
    )

    dashboard_report.write(
        "Department Analysis\n"
    )

    department_summary = (
        filtered_df
        .groupby("Department")
        .agg(
            Employees=("Employee Name", "count"),
            Average_Performance=("Performance Score", "mean"),
            Average_Attendance=("Attendance %", "mean"),
            Total_Projects=("Projects Completed", "sum"),
            Average_Salary=("Salary", "mean")
        )
        .round(2)
    )

    dashboard_report.write(
        department_summary.to_csv()
    )

    dashboard_report.write(
        "\nPerformance Category Distribution\n"
    )

    category_summary = (
        filtered_df["Performance Category"]
        .value_counts()
        .rename_axis("Performance Category")
        .reset_index(name="Employees")
    )

    dashboard_report.write(
        category_summary.to_csv(index=False)
    )

    dashboard_report.write(
        "\nCorrelation Matrix\n"
    )

    numeric_columns = filtered_df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric_columns) >= 2:

        correlation_matrix = (
            filtered_df[numeric_columns]
            .corr()
            .round(2)
        )

        dashboard_report.write(
            correlation_matrix.to_csv()
        )

    st.download_button(
        label=":material/download: Download Dashboard Summary",
        data=dashboard_report.getvalue(),
        file_name="Nettech_Dashboard_Summary_Report.csv",
        mime="text/csv"
    )

    st.write("")

    st.markdown(
        "### :material/bar_chart: Department Analysis"
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        with st.container(border=True):

            st.markdown(
                "#### :material/groups: Employee Distribution"
            )

            department_counts = (
                filtered_df["Department"]
                .value_counts()
            )

            fig, ax = plt.subplots(
                figsize=(3.2, 1.9)
            )

            fig.patch.set_facecolor(
                chart_background
            )

            ax.set_facecolor(
                chart_background
            )

            department_counts.plot(
                kind="bar",
                ax=ax,
                color=royal_blue,
                width=0.58
            )

            ax.set_xlabel(
                "Department",
                color=chart_text,
                fontsize=7
            )

            ax.set_ylabel(
                "Employees",
                color=chart_text,
                fontsize=7
            )

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=6
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=6
            )

            for spine in ax.spines.values():
                spine.set_color(
                    chart_grid
                )

            fig.tight_layout(
                pad=0.35
            )

            st.pyplot(
                fig,
                width="content"
            )

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

            fig, ax = plt.subplots(
                figsize=(3.2, 1.9)
            )

            fig.patch.set_facecolor(
                chart_background
            )

            ax.set_facecolor(
                chart_background
            )

            avg_performance_department.plot(
                kind="bar",
                ax=ax,
                color=royal_blue,
                width=0.58
            )

            ax.set_xlabel(
                "Department",
                color=chart_text,
                fontsize=7
            )

            ax.set_ylabel(
                "Performance Score",
                color=chart_text,
                fontsize=7
            )

            ax.set_ylim(
                0,
                10
            )

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=6
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=6
            )

            for spine in ax.spines.values():
                spine.set_color(
                    chart_grid
                )

            fig.tight_layout(
                pad=0.35
            )

            st.pyplot(
                fig,
                width="content"
            )

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

            fig, ax = plt.subplots(
                figsize=(3.2, 2.1)
            )

            fig.patch.set_facecolor(
                chart_background
            )

            ax.set_facecolor(
                chart_background
            )

            wedges, _ = ax.pie(
                category_counts.values,
                startangle=90,
                radius=0.78,
                wedgeprops={
                    "width": 0.38,
                    "edgecolor": chart_background,
                    "linewidth": 1
                }
            )

            total_categories = category_counts.sum()

            legend_labels = [
                f"{category}  {value / total_categories * 100:.1f}%"
                for category, value in category_counts.items()
            ]

            legend = ax.legend(
                wedges,
                legend_labels,
                title="Performance Category",
                loc="center left",
                bbox_to_anchor=(1.00, 0.50),
                fontsize=6.5,
                title_fontsize=7,
                frameon=False,
                labelcolor=chart_text
            )

            plt.setp(
                legend.get_title(),
                color=chart_text
            )

            ax.text(
                0,
                0.08,
                "Performance",
                ha="center",
                va="center",
                fontsize=8,
                fontweight="bold",
                color=chart_text
            )

            ax.text(
                0,
                -0.10,
                "Distribution",
                ha="center",
                va="center",
                fontsize=7,
                color=chart_text
            )

            ax.set_aspect("equal")

            fig.tight_layout(
                pad=0.3
            )

            st.pyplot(
                fig,
                width="content"
            )

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
                height=175
            )

    st.write("")

    st.markdown(
        "### :material/compare_arrows: Performance Relationships"
    )

    relation_col1, relation_col2 = st.columns(2)

    with relation_col1:
        with st.container(border=True):

            st.markdown(
                "#### :material/event_available: Attendance vs Performance"
            )

            fig, ax = plt.subplots(
                figsize=(3.2, 1.9)
            )

            fig.patch.set_facecolor(
                chart_background
            )

            ax.set_facecolor(
                chart_background
            )

            ax.scatter(
                filtered_df["Attendance %"],
                filtered_df["Performance Score"],
                color=royal_blue,
                alpha=0.7,
                s=18
            )

            ax.set_xlabel(
                "Attendance %",
                color=chart_text,
                fontsize=7
            )

            ax.set_ylabel(
                "Performance Score",
                color=chart_text,
                fontsize=7
            )

            ax.set_ylim(
                0,
                10
            )

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=6
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=6
            )

            for spine in ax.spines.values():
                spine.set_color(
                    chart_grid
                )

            fig.tight_layout(
                pad=0.35
            )

            st.pyplot(
                fig,
                width="content"
            )

            plt.close(fig)

    with relation_col2:
        with st.container(border=True):

            st.markdown(
                "#### :material/task_alt: Projects vs Performance"
            )

            fig, ax = plt.subplots(
                figsize=(3.2, 1.9)
            )

            fig.patch.set_facecolor(
                chart_background
            )

            ax.set_facecolor(
                chart_background
            )

            ax.scatter(
                filtered_df["Projects Completed"],
                filtered_df["Performance Score"],
                color=royal_blue,
                alpha=0.7,
                s=18
            )

            ax.set_xlabel(
                "Projects Completed",
                color=chart_text,
                fontsize=7
            )

            ax.set_ylabel(
                "Performance Score",
                color=chart_text,
                fontsize=7
            )

            ax.set_ylim(
                0,
                10
            )

            ax.tick_params(
                axis="x",
                colors=chart_text,
                labelsize=6
            )

            ax.tick_params(
                axis="y",
                colors=chart_text,
                labelsize=6
            )

            for spine in ax.spines.values():
                spine.set_color(
                    chart_grid
                )

            fig.tight_layout(
                pad=0.35
            )

            st.pyplot(
                fig,
                width="content"
            )

            plt.close(fig)

    st.write("")

    st.markdown(
        "### :material/grid_on: Correlation Heatmap"
    )

    numeric_columns = filtered_df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric_columns) >= 2:

        correlation_matrix = (
            filtered_df[numeric_columns]
            .corr()
        )

        fig, ax = plt.subplots(
            figsize=(5.5, 2.8)
        )

        fig.patch.set_facecolor(
            chart_background
        )

        ax.set_facecolor(
            chart_background
        )

        heatmap = ax.imshow(
            correlation_matrix,
            cmap="Blues",
            vmin=-1,
            vmax=1
        )

        ax.set_xticks(
            range(len(correlation_matrix.columns))
        )

        ax.set_yticks(
            range(len(correlation_matrix.columns))
        )

        ax.set_xticklabels(
            correlation_matrix.columns,
            rotation=45,
            ha="right",
            fontsize=7,
            color=chart_text
        )

        ax.set_yticklabels(
            correlation_matrix.columns,
            fontsize=7,
            color=chart_text
        )

        for i in range(
            len(correlation_matrix.columns)
        ):
            for j in range(
                len(correlation_matrix.columns)
            ):
                ax.text(
                    j,
                    i,
                    f"{correlation_matrix.iloc[i, j]:.2f}",
                    ha="center",
                    va="center",
                    fontsize=7,
                    color=chart_text
                )

        fig.colorbar(
            heatmap,
            ax=ax,
            fraction=0.035,
            pad=0.04
        )

        fig.tight_layout(
            pad=0.5
        )

        st.pyplot(
            fig,
            width="content"
        )

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

            st.markdown(
                "### :material/summarize: Dataset Summary"
            )

            st.dataframe(
                summary,
                use_container_width=True
            )

            report = StringIO()

            report.write(
                "NETTECH EMPLOYEE ANALYTICS - SUMMARY REPORT\n\n"
            )

            report.write(
                "Dataset Overview\n"
            )

            report.write(
                f"Rows,{len(uploaded_df)}\n"
            )

            report.write(
                f"Columns,{len(uploaded_df.columns)}\n"
            )

            report.write(
                f"Missing Values,{int(uploaded_df.isnull().sum().sum())}\n\n"
            )

            report.write(
                "Numeric Summary\n"
            )

            summary.to_csv(
                report
            )

            st.download_button(
                label=":material/save: Download Summary Report",
                data=report.getvalue(),
                file_name="Summary_Report.csv",
                mime="text/csv"
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
        "### :material/note:NOTE:"
    )

    st.write(
        "THE DATASET USED IN THIS PROJECT TO MAKE THE DASHBOARD IS CREATED BY VARIOUS SOURCES AND IS NOT THE ACTUAL DATA"
    )
