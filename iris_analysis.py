# iris_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

def main():
    print("🚀 Starting Iris Dataset Analysis...")
    
    # Load data
    try:
        iris = load_iris()
        iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        iris_df['species'] = iris.target
        iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        print("✅ Iris dataset loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return
    
    # Display basic info
    print(f"\nDataset shape: {iris_df.shape}")
    print(f"Columns: {list(iris_df.columns)}")
    print(f"\nFirst 5 rows:")
    print(iris_df.head())
    
    # Analysis
    print("\n📈 Basic Statistics:")
    print(iris_df.describe())
    
    print("\n🌿 Mean values by species:")
    print(iris_df.groupby('species').mean())
    
    # Create visualizations
    create_visualizations(iris_df)
    
    print("\n✅ Analysis completed successfully!")

def create_visualizations(iris_df):
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create main figure
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Iris Dataset Analysis', fontsize=16, fontweight='bold')
    
    # 1. Line chart
    axes[0, 0].plot(iris_df.index, iris_df['sepal length (cm)'], label='Sepal Length')
    axes[0, 0].plot(iris_df.index, iris_df['petal length (cm)'], label='Petal Length')
    axes[0, 0].set_title('1. Line Chart: Measurements Trend')
    axes[0, 0].set_xlabel('Sample Index')
    axes[0, 0].set_ylabel('Length (cm)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Bar chart
    species_means = iris_df.groupby('species')['petal length (cm)'].mean()
    bars = axes[0, 1].bar(species_means.index, species_means.values, alpha=0.7)
    axes[0, 1].set_title('2. Bar Chart: Average Petal Length by Species')
    axes[0, 1].set_xlabel('Species')
    axes[0, 1].set_ylabel('Average Petal Length (cm)')
    
    # 3. Histogram
    axes[1, 0].hist(iris_df['sepal length (cm)'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    axes[1, 0].set_title('3. Histogram: Sepal Length Distribution')
    axes[1, 0].set_xlabel('Sepal Length (cm)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Scatter plot
    for species in iris_df['species'].unique():
        species_data = iris_df[iris_df['species'] == species]
        axes[1, 1].scatter(species_data['sepal length (cm)'], 
                          species_data['petal length (cm)'], 
                          label=species, alpha=0.7)
    axes[1, 1].set_title('4. Scatter Plot: Sepal vs Petal Length')
    axes[1, 1].set_xlabel('Sepal Length (cm)')
    axes[1, 1].set_ylabel('Petal Length (cm)')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('iris_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Additional plots
    sns.pairplot(iris_df, hue='species', palette='viridis')
    plt.suptitle('Pairplot: All Variables by Species', y=1.02)
    plt.savefig('iris_pairplot.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()