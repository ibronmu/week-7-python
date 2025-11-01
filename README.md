# Iris Dataset Analysis Project

A comprehensive data analysis project exploring the famous Iris flower dataset using Python. This project demonstrates data loading, cleaning, exploratory data analysis, and visualization techniques.

## 📋 Project Overview

This project performs a complete analysis of the Iris dataset, which contains measurements of 150 iris flowers from three different species:
- Setosa
- Versicolor
- Virginica

The analysis includes statistical summaries, data visualizations, and insights about the relationships between different flower characteristics.

## 🛠️ Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)

## 📦 Installation

1. **Clone or download this project** to your local machine

2. **Install required Python packages** by running:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Alternatively, you can install all packages at once:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, create one with the following content:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
```

## 🚀 How to Run

### Method 1: Python Script (Recommended)

1. **Save the code** as `iris_analysis.py`

2. **Open terminal/command prompt** and navigate to the project directory

3. **Run the script**:

```bash
python iris_analysis.py
```

On some systems, you might need to use:

```bash
python3 iris_analysis.py
```

or on Windows:

```bash
py iris_analysis.py
```

### Method 2: Jupyter Notebook

If you prefer using Jupyter Notebook:

1. **Install Jupyter**:

```bash
pip install jupyter
```

2. **Start Jupyter**:

```bash
jupyter notebook
```

3. **Create a new Python 3 notebook** and copy the code from the script

4. **Run each code cell** sequentially

## 📊 Project Structure

The analysis is organized into three main tasks:

### Task 1: Data Loading and Cleaning
- Load the Iris dataset from scikit-learn
- Inspect data structure and quality
- Check for missing values
- Prepare data for analysis

### Task 2: Basic Data Analysis
- Compute descriptive statistics
- Group data by species
- Calculate mean values for each species
- Identify patterns and insights

### Task 3: Data Visualization

Create four main visualizations:

1. **Line Chart**: Trends of measurements across samples
2. **Bar Chart**: Average petal length by species
3. **Histogram**: Distribution of sepal length
4. **Scatter Plot**: Relationship between sepal and petal length

Additional visualizations include:
- Pairplot showing all variable relationships
- Boxplot of petal width by species

## 📈 Key Findings

After running the analysis, you'll discover:

- **Clear species separation**: Each iris species has distinct measurement patterns
- **Petal characteristics**: Most effective for distinguishing species
- **Measurement correlations**: Strong relationships between different flower parts
- **Statistical insights**: Detailed descriptive statistics for each species

## 🖼️ Output Files

When you run the script, it will generate:

- **Console output**: Statistical summaries and insights
- **iris_analysis.png**: Main visualization dashboard
- **iris_pairplot.png**: Additional relationship visualizations

## 🐛 Troubleshooting

### Common Issues and Solutions

**1. "ModuleNotFoundError"**

```bash
# Solution: Install missing packages
pip install pandas matplotlib seaborn scikit-learn
```

**2. "Python not found"**

```bash
# On Windows, try:
py -m pip install pandas matplotlib seaborn scikit-learn
py iris_analysis.py

# On Mac/Linux, try:
python3 -m pip install pandas matplotlib seaborn scikit-learn
python3 iris_analysis.py
```

**3. Matplotlib display issues**

```bash
# Install tkinter backend
# On Ubuntu/Debian:
sudo apt-get install python3-tk

# On Windows, it's usually included
# On Mac:
brew install python-tk
```

**4. Permission errors**

```bash
# On Mac/Linux, use sudo if needed
sudo pip install pandas matplotlib seaborn scikit-learn
```

## 📚 Learning Objectives

This project helps you learn:

- Data manipulation with pandas
- Statistical analysis techniques
- Data visualization with matplotlib and seaborn
- Exploratory Data Analysis (EDA) workflow
- Working with real-world datasets

## 🔧 Customization

You can modify the code to:

- Use a different dataset (replace the Iris dataset)
- Add more visualizations
- Perform additional statistical tests
- Export results to CSV/Excel
- Create interactive plots with Plotly

## 📞 Support

If you encounter any issues:

1. Check that all required packages are installed
2. Ensure you're using a compatible Python version
3. Verify the file path and naming
4. Check the console for specific error messages

## 📄 License

This project is for educational purposes. The Iris dataset is publicly available and commonly used for machine learning and data analysis demonstrations.

## 🎯 Next Steps

After completing this analysis, you can:

- Try the same analysis with different datasets
- Add machine learning classification models
- Create interactive dashboards with Plotly Dash
- Export your findings to a report
- Deploy as a web application

---

**Happy Analyzing! 🌸**
