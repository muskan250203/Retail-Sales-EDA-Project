import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. PARENT CLASS: Base Data Handler ---
class DatasetManager:
    def __init__(self, raw_data):
        print("--- Step 1: Initializing Retail Sales Dataset via Parent Class ---")
        self.raw_data = raw_data
        self.df = pd.DataFrame(self.raw_data)

    def clean_data(self):
        # Data Cleaning & Validation check (using re-assignment)
        self.df = self.df.dropna()
        return self.df

# --- 2. CHILD CLASS: Inherits from DatasetManager (Inheritance Concept) ---
class RetailSalesAnalyzer(DatasetManager):
    def __init__(self, raw_data):
        # Inherit initialization from Parent Class using super()
        super().__init__(raw_data)
        # Automatically clean data upon creation
        self.clean_data()

    def compute_statistics(self):
        print("\n--- Step 2: Statistical Computations using NumPy & Pandas ---")
        total_revenue = np.sum(self.df['Sales_Revenue'])
        mean_revenue = np.mean(self.df['Sales_Revenue'])
        median_revenue = np.median(self.df['Sales_Revenue'])
        std_revenue = np.std(self.df['Sales_Revenue'])

        print(f"Total Annual Revenue: ${total_revenue}")
        print(f"Mean Monthly Revenue: ${mean_revenue:.2f}")
        print(f"Median Monthly Revenue: ${median_revenue:.2f}")
        print(f"Standard Deviation of Revenue: ${std_revenue:.2f}")

    def generate_visualizations(self):
        print("\n--- Step 3: Generating Visualizations using Matplotlib ---")
        # Setting up a 2x2 grid for subplots
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Retail Sales & Customer Behavior EDA Dashboard', fontsize=16, fontweight='bold')

        # Simplified color list using easy-to-read names
        my_colors = ['lightcoral', 'skyblue', 'lightgreen']

        # 1. Line Plot: Sales Trends Over Time
        axs[0, 0].plot(self.df['Month'], self.df['Sales_Revenue'], marker='o', color='blue', linewidth=2)
        axs[0, 0].set_title('Sales Revenue Trend Over Time')
        axs[0, 0].set_xlabel('Month')
        axs[0, 0].set_ylabel('Revenue ($)')
        axs[0, 0].grid(True, linestyle='--', alpha=0.6)
        axs[0, 0].tick_params(axis='x', rotation=45)

        # 2. Bar Plot: Sales Performance Across Categories
        category_sales = self.df.groupby('Product_Category')['Sales_Revenue'].sum()
        category_sales.plot(kind='bar', ax=axs[0, 1], color=my_colors)
        axs[0, 1].set_title('Total Sales by Product Category')
        axs[0, 1].set_xlabel('Product Category')
        axs[0, 1].set_ylabel('Revenue ($)')
        axs[0, 1].grid(axis='y', linestyle='--', alpha=0.6)

        # 3. Pie Chart: Distribution of Sales by Category
        axs[1, 0].pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140, 
                     colors=my_colors)
        axs[1, 0].set_title('Sales Distribution Percentage by Category')

        # 4. Scatter Plot: Customer Age vs Sales Revenue Correlation
        axs[1, 1].scatter(self.df['Customer_Age'], self.df['Sales_Revenue'], color='purple', s=100, edgecolor='black')
        axs[1, 1].set_title('Customer Age vs Sales Revenue Correlation')
        axs[1, 1].set_xlabel('Customer Age')
        axs[1, 1].set_ylabel('Revenue ($)')
        axs[1, 1].grid(True, linestyle='--', alpha=0.6)

        # Adjust layout for neat presentation
        plt.tight_layout(pad=3.0, w_pad=4.0, h_pad=3.0, rect=[0, 0.03, 1, 0.93])

        print("\n--- Step 4: Displaying Graphs ---")
        plt.show()

# --- 3. MAIN EXECUTION ---
if __name__ == "__main__":
    # Your exact raw data dictionary kept completely as it is
    data = {
        'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Product_Category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home', 
                             'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home'],
        'Sales_Revenue': [12000, 15000, 11000, 18000, 22000, 25000, 27000, 24000, 21000, 26000, 30000, 35000],
        'Units_Sold': [120, 150, 100, 180, 210, 240, 260, 230, 200, 250, 290, 340],
        'Customer_Age': [25, 30, 22, 35, 40, 28, 26, 32, 45, 29, 38, 33]
    }

    # Creating an object of the child class and calling its methods
    analyzer = RetailSalesAnalyzer(data)
    analyzer.compute_statistics()
    analyzer.generate_visualizations()